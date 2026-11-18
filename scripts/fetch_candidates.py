#!/usr/bin/env python3
"""
fetch_candidates.py
-------------------
Daily RSS candidate fetcher for the Quant & Finance Archive (LLM-wiki) pipeline.
Uses only Python 3 standard library (zero external dependencies).

Fetches headlines, short summaries (<= 300 chars), timestamps, and URLs
from pre-approved public RSS feeds across 5 categories, deduplicates them,
applies a 24h window (with 48h fallback if < 4 items), and saves a lightweight
JSON file to `raw/candidates_MM-DD.json`.

Usage:
    python3 scripts/fetch_candidates.py
    python3 scripts/fetch_candidates.py --output raw/candidates_test.json
"""

from __future__ import annotations

import argparse
import email.utils
import html
import json
import re
import ssl
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

# Taipei timezone (UTC+8)
TAIPEI_TZ = timezone(timedelta(hours=8))

# Polite User-Agent to avoid default urllib blocks
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml;q=0.9, */*;q=0.8",
}

TIMEOUT_SECONDS = 12
REQUEST_DELAY_SECONDS = 0.5
SUMMARY_MAX_CHARS = 300
MIN_ITEMS_BEFORE_FALLBACK = 4

# Pre-approved public RSS sources grouped by the 5 target categories
CATEGORIES: dict[str, dict[str, Any]] = {
    "1_us_macro": {
        "label": "美國總經與政策",
        "target_pick": 1,
        "candidate_cap": 10,
        "feeds": [
            {
                "source": "CNBC Business",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10001147",
            },
            {
                "source": "CNBC Top Stories",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114",
            },
            {
                "source": "Bloomberg Economics",
                "url": "https://feeds.bloomberg.com/economics/news.rss",
            },
            {
                "source": "Reuters (Google News 24h)",
                "url": "https://news.google.com/rss/search?q=when:24h+site:reuters.com&hl=en-US&gl=US&ceid=US:en",
            },
        ],
    },
    "2_tw_semis": {
        "label": "台股大盤與核心半導體",
        "target_pick": 2,
        "candidate_cap": 12,
        "feeds": [
            {
                "source": "中央社 產經證券",
                "url": "https://feeds.feedburner.com/rsscna/finance",
            },
            {
                "source": "經濟日報 證券台股",
                "url": "https://money.udn.com/rssfeed/news/1001/5590/11074?ch=money",
            },
            {
                "source": "經濟日報 產經",
                "url": "https://money.udn.com/rssfeed/news/1001/5591/5612?ch=money",
            },
            {
                "source": "Google News (TSMC / Nvidia)",
                "url": "https://news.google.com/rss/search?q=when:24h+(TSMC+OR+Nvidia)&hl=en-US&gl=US&ceid=US:en",
            },
        ],
    },
    "3_tech_supply_chain": {
        "label": "前瞻科技與台廠供應鏈",
        "target_pick": 2,
        "candidate_cap": 12,
        "feeds": [
            {
                "source": "TechNews 科技新報",
                "url": "https://technews.tw/feed/",
            },
            {
                "source": "中央社 科技",
                "url": "https://feeds.feedburner.com/rsscna/technology",
            },
            {
                "source": "CNBC Technology",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19854910",
            },
            {
                "source": "TechCrunch AI",
                "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
            },
        ],
    },
    "4_fx_commodities": {
        "label": "國際匯市與大宗避險資產",
        "target_pick": 1,
        "candidate_cap": 10,
        "feeds": [
            {
                "source": "Google News (Gold / Oil / Forex)",
                "url": "https://news.google.com/rss/search?q=when:24h+(gold+OR+crude+oil+OR+forex+OR+dollar)&hl=en-US&gl=US&ceid=US:en",
            },
            {
                "source": "CNBC World",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100727362",
            },
            {
                "source": "MarketWatch Top Stories",
                "url": "https://feeds.content.dowjones.io/public/rss/mw_topstories",
            },
            {
                "source": "Bloomberg Markets",
                "url": "https://feeds.bloomberg.com/markets/news.rss",
            },
        ],
    },
    "5_ai_blindbox": {
        "label": "AI 國際焦點盲盒",
        "target_pick": 1,
        "candidate_cap": 10,
        "feeds": [
            {
                "source": "BBC Business",
                "url": "https://feeds.bbci.co.uk/news/business/rss.xml",
            },
            {
                "source": "BBC World",
                "url": "https://feeds.bbci.co.uk/news/world/rss.xml",
            },
            {
                "source": "The Guardian World",
                "url": "https://www.theguardian.com/world/rss",
            },
            {
                "source": "中央社 國際",
                "url": "https://feeds.feedburner.com/rsscna/intworld",
            },
        ],
    },
}


def clean_text(raw: str | None, max_chars: int | None = None) -> str:
    """Strip HTML tags, unescape entities, normalize whitespace, and optionally truncate."""
    if not raw:
        return ""
    text = html.unescape(raw)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if max_chars and len(text) > max_chars:
        text = text[: max_chars - 3].rstrip() + "..."
    return text


def parse_datetime(date_str: str | None) -> datetime | None:
    """Parse RFC 2822 (RSS) or ISO 8601 (Atom) timestamps into UTC datetime."""
    if not date_str:
        return None
    date_str = date_str.strip()

    # Try RFC 2822 first
    try:
        dt = email.utils.parsedate_to_datetime(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError):
        pass

    # Try ISO 8601
    try:
        iso_str = date_str.replace("Z", "+00:00")
        dt = datetime.fromisoformat(iso_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


def local_tag(elem: ET.Element) -> str:
    """Return tag name without XML namespace prefix."""
    return elem.tag.split("}", 1)[-1].lower()


def find_child_text(parent: ET.Element, names: tuple[str, ...]) -> str:
    """Find first matching child element's text ignoring XML namespaces."""
    for child in parent:
        if local_tag(child) in names and child.text:
            return child.text.strip()
    return ""


def extract_link(entry: ET.Element) -> str:
    """Extract article URL from RSS <link> or Atom <link href='...'>."""
    for child in entry:
        if local_tag(child) == "link":
            href = child.attrib.get("href")
            if href:
                return href.strip()
            if child.text:
                return child.text.strip()
    return ""


def fetch_xml(url: str) -> bytes:
    """Fetch raw XML bytes from URL with polite headers and timeout."""
    req = urllib.request.Request(url, headers=REQUEST_HEADERS)
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS, context=ctx) as resp:
        return resp.read()


def parse_feed(source_name: str, url: str) -> list[dict[str, Any]]:
    """Download and parse an RSS 2.0 or Atom feed into normalized candidate dicts."""
    raw_bytes = fetch_xml(url)
    root = ET.fromstring(raw_bytes)
    items: list[dict[str, Any]] = []

    # Support both RSS (<item>) and Atom (<entry>)
    entries = [el for el in root.iter() if local_tag(el) in ("item", "entry")]

    for entry in entries:
        title = clean_text(find_child_text(entry, ("title",)))
        link = extract_link(entry)
        if not title or not link:
            continue

        raw_summary = find_child_text(entry, ("description", "summary", "content"))
        summary = clean_text(raw_summary, max_chars=SUMMARY_MAX_CHARS)

        raw_date = find_child_text(entry, ("pubdate", "published", "updated", "date"))
        dt_utc = parse_datetime(raw_date)

        items.append(
            {
                "source": source_name,
                "title": title,
                "published_at": dt_utc.astimezone(TAIPEI_TZ).isoformat() if dt_utc else None,
                "_dt_utc": dt_utc,
                "summary": summary,
                "url": link,
            }
        )

    return items


def normalize_title_key(title: str) -> str:
    """Create a loose key for headline deduplication."""
    return re.sub(r"[\W_]+", "", title.lower())[:48]


def select_candidates_for_category(
    cat_key: str,
    cat_cfg: dict[str, Any],
    now_utc: datetime,
    seen_urls: set[str],
    seen_titles: set[str],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Fetch, filter by 24h (with 48h fallback), interleave by source, and cap items."""
    cutoff_24h = now_utc - timedelta(hours=24)
    cutoff_48h = now_utc - timedelta(hours=48)

    per_feed_24h: list[list[dict[str, Any]]] = []
    per_feed_48h: list[list[dict[str, Any]]] = []
    feed_errors: list[dict[str, str]] = []

    for feed in cat_cfg["feeds"]:
        source_name = feed["source"]
        feed_url = feed["url"]
        try:
            parsed = parse_feed(source_name, feed_url)
        except (urllib.error.URLError, urllib.error.HTTPError, ET.ParseError, TimeoutError, Exception) as exc:
            feed_errors.append({"source": source_name, "error": str(exc)})
            continue
        finally:
            time.sleep(REQUEST_DELAY_SECONDS)

        items_24h: list[dict[str, Any]] = []
        items_48h: list[dict[str, Any]] = []

        for item in parsed:
            dt = item["_dt_utc"]
            # If feed lacks timestamp, keep as recent candidate; otherwise enforce cutoff
            if dt is None or dt >= cutoff_24h:
                items_24h.append(item)
            elif dt >= cutoff_48h:
                items_48h.append(item)

        items_24h.sort(key=lambda x: x["_dt_utc"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
        items_48h.sort(key=lambda x: x["_dt_utc"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
        per_feed_24h.append(items_24h)
        per_feed_48h.append(items_48h)

    def interleave_and_dedup(
        buckets: list[list[dict[str, Any]]],
        cap: int,
        is_fallback: bool,
    ) -> list[dict[str, Any]]:
        selected: list[dict[str, Any]] = []
        max_len = max((len(b) for b in buckets), default=0)
        for idx in range(max_len):
            for bucket in buckets:
                if len(selected) >= cap:
                    return selected
                if idx >= len(bucket):
                    continue
                item = bucket[idx]
                url_key = item["url"].split("?", 1)[0] if "news.google.com" not in item["url"] else item["url"]
                title_key = normalize_title_key(item["title"])
                if url_key in seen_urls or (title_key and title_key in seen_titles):
                    continue
                seen_urls.add(url_key)
                if title_key:
                    seen_titles.add(title_key)

                clean_item = {
                    "category": cat_key,
                    "category_label": cat_cfg["label"],
                    "source": item["source"],
                    "title": item["title"],
                    "published_at": item["published_at"],
                    "summary": item["summary"],
                    "url": item["url"],
                }
                if is_fallback:
                    clean_item["fallback_48h"] = True
                selected.append(clean_item)
        return selected

    cap = cat_cfg["candidate_cap"]
    chosen = interleave_and_dedup(per_feed_24h, cap=cap, is_fallback=False)
    used_fallback = False

    if len(chosen) < MIN_ITEMS_BEFORE_FALLBACK:
        used_fallback = True
        extra = interleave_and_dedup(per_feed_48h, cap=cap - len(chosen), is_fallback=True)
        chosen.extend(extra)

    stats = {
        "label": cat_cfg["label"],
        "target_pick": cat_cfg["target_pick"],
        "candidate_count": len(chosen),
        "fallback_48h_used": used_fallback,
        "feed_errors": feed_errors,
    }
    return chosen, stats


def main() -> None:
    now_utc = datetime.now(timezone.utc)
    now_taipei = now_utc.astimezone(TAIPEI_TZ)
    default_output = Path("raw") / f"candidates_{now_taipei.strftime('%m-%d')}.json"

    parser = argparse.ArgumentParser(description="Fetch daily RSS news candidates for LLM-wiki.")
    parser.add_argument(
        "--output",
        type=Path,
        default=default_output,
        help=f"Output JSON path (default: {default_output})",
    )
    args = parser.parse_args()

    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    all_candidates: list[dict[str, Any]] = []
    category_stats: dict[str, Any] = {}

    for cat_key, cat_cfg in CATEGORIES.items():
        items, stats = select_candidates_for_category(
            cat_key=cat_key,
            cat_cfg=cat_cfg,
            now_utc=now_utc,
            seen_urls=seen_urls,
            seen_titles=seen_titles,
        )
        all_candidates.extend(items)
        category_stats[cat_key] = stats

    payload = {
        "generated_at": now_taipei.isoformat(),
        "window_hours": 24,
        "total_candidates": len(all_candidates),
        "category_stats": category_stats,
        "candidates": all_candidates,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[OK] Saved {len(all_candidates)} candidates to {args.output}")
    for cat_key, st in category_stats.items():
        fb = " (48h fallback)" if st["fallback_48h_used"] else ""
        print(f"  - {cat_key} ({st['label']}): {st['candidate_count']} items{fb}")
        for err in st["feed_errors"]:
            print(f"    [WARN] {err['source']}: {err['error']}")


if __name__ == "__main__":
    main()