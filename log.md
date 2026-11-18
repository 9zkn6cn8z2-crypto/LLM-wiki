## [2026-11-17] ingest | 彰化銀行財經理財晨訊（2026-11-16）
- 將上傳的 `財經理財晨訊20261116.pdf` 完整文字與數據存檔至 `raw/chb-morning-briefing-2026-11-16.md`（唯讀來源）。
- 依 `AGENTS.md` 規範建立 `wiki/chb-morning-briefing-2026-11-16.html`，彙整美歐亞市場回顧、高盛／美銀觀點分歧與重點商品個股行情。
- 更新 `index.html`，新增「財經與市場研究」分類與頁面索引連結。

## [2026-11-17] ingest | 11/16–11/17 三大面向金融新聞匯入
- 聯網蒐集 11/16–11/17 美國總經與 Fed、台股與輝達半導體、國際匯市與原物料三篇新聞，存檔至 `raw/us-macro-fed-warsh-2026-11-16.md`、`raw/tw-stock-nvidia-2026-11-16-17.md` 與 `raw/global-fx-commodities-2026-11-16-17.md`。
- 編譯產出對應 Wiki 頁面 `wiki/us-macro-fed-warsh-2026-11-16.html`、`wiki/tw-stock-nvidia-2026-11-16-17.html`、`wiki/global-fx-commodities-2026-11-16-17.html`（含 MathJax 與雙向交叉連結），並更新 `index.html`。

## [2026-11-17] note | 11/16–11/17 全球金融市場日報統整筆記
- 嚴格依據 `wiki/` 現有 4 篇財經條目彙整產出 `notes/financial-daily-2026-11-16-17.md`，每段論點皆附上 `[條目名稱](../wiki/xxx.html)` 來源標記，並於文末列出待擴充外部文獻與 Ingest 指令。

## [2026-11-17] slide | 11/16–11/17 全球金融市場日報簡報
- 依 `notes/financial-daily-2026-11-16-17.md` 萃取 7 頁簡報大綱至 `slides/drafts/financial-daily-2026-11-16-17-slides.md`。
- 轉換產出深色量化金融風格 Reveal.js 簡報 `slides/html/financial-daily-2026-11-16-17-slides.html`（含 MathJax 公式與 `assets/slides.css`）。

## [2026-11-17] note | 2026-11-17 全球金融市場日報（11-17-daily-report.md）
- 嚴格依據 `wiki/` 現有 4 篇條目產出 `notes/11-17-daily-report.md`，並依防腦補原則明確標示「澳洲央行升息」與「美國 CPI 細項」尚無收錄，於文末附上官方與財經參考文獻連結與 Ingest 指令。

## [2026-11-17] slide | 2026-11-17 全球金融市場日報簡報（11-17-daily-report-slides.html）
- 依 `notes/11-17-daily-report.md` 萃取 7 頁分頁大綱至 `slides/drafts/11-17-daily-report-slides.md`。
- 轉換產出 Reveal.js + MathJax + `assets/slides.css` 深色風格網頁簡報 `slides/html/11-17-daily-report-slides.html`。

## [2026-11-17] ingest | 補齊 7 份原始資料配額（美國 CPI、RBA 升息紀要、比特幣重挫）
- 聯網補齊 3 篇新聞存檔至 `raw/us-cpi-oct-2026-inflation.md`、`raw/rba-rate-hike-minutes-2026-11-17.md` 與 `raw/crypto-bitcoin-market-2026-11-16-17.md`（使 `raw/` 總數達 7 份）。
- 編譯產出對應 Wiki 頁面 `wiki/us-cpi-oct-2026-inflation.html`、`wiki/rba-rate-hike-minutes-2026-11-17.html`、`wiki/crypto-bitcoin-market-2026-11-16-17.html`，並更新 `index.html` 納入全部 7 篇條目。

## [2026-11-17] note | 刷新 2026-11-17 全球金融市場日報（納入 7 篇 Wiki）
- 基於完整 7 篇 `wiki/` 重新產出 `notes/11-17-daily-report.md`，補齊美國 10 月 CPI、澳洲央行 4.85% 升息暨 11/17 會議紀要與比特幣爆倉動態，全篇嚴格標註 `[條目名稱](../wiki/xxx.html)` 來源連結。

## [2026-11-17] slide | 刷新 2026-11-17 全球金融市場日報簡報（8 頁完整版）
- 依新版 `notes/11-17-daily-report.md` 重新萃取 `slides/drafts/11-17-daily-report-slides.md`（8 頁大綱）。
- 重新生成 Reveal.js + MathJax + `assets/slides.css` 深色量化金融簡報 `slides/html/11-17-daily-report-slides.html`。

## [2026-11-18] ingest | 匯入 2026-11-18 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 透過 `scripts/fetch_candidates.py` 撈取 54 則候選新聞（`raw/candidates_11-18.json`），精選 7 篇全文存檔至 `raw/`（`apec-shenzhen-us-china-trade-2026-11-18.md`、`tw-stock-rebound-40k-2026-11-18.md`、`nvidia-q3-fy27-earnings-2026-11-18.md`、`suregiant-foplp-hydrolyzable-tape-2026-11-18.md`、`anthropic-ipo-nasdaq-2026-11-18.md`、`japan-oct-2026-trade-deficit-oil-2026-11-18.md`、`us-tech-outages-rubio-ai-patches-2026-11-18.md`）。
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax 與跨日雙向交叉連結），並更新 `index.html`。

## [2026-11-18] note | 產出 2026-11-18 全球金融市場日報（11-18-daily-report.md）
- 嚴格依據 `wiki/` 既有條目萃取產出 `notes/11-18-daily-report.md`，全篇標註 `[條目名稱](../wiki/xxx.html)` 來源連結，並於文末附上待擴充參考文獻。

## [2026-11-18] slide | 產出 2026-11-18 全球金融市場日報簡報（8 頁完整版）
- 依 `notes/11-18-daily-report.md` 萃取 8 頁逐頁簡報大綱至 `slides/drafts/11-18-daily-report-slides.md`。
- 轉換產出 Reveal.js + MathJax + `assets/slides.css` 深色風格網頁簡報 `slides/html/11-18-daily-report-slides.html`，並更新 `index.html` 最新日報連結。
