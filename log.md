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

## [2026-11-18] schema | 新增每日 7 篇選題配額與研究導向重點萃取標準至 AGENTS.md
- 於 `AGENTS.md` 新增第 5.5 節，明訂每日 1+2+2+1+1（含 AI 國際焦點盲盒）共 7 篇之選題配額，並搭配 `scripts/fetch_candidates.py` 之 RSS 兩段式候選流程。
- 確立研究導向文章重點萃取標準：常規新聞必抓「硬數據與預期差、因果傳導鏈、知識庫連貫與衝突、1–3 天短線催化劑」；盲盒新聞必抓「入選理由、核心事實與量化規模、跨市場外溢風險」。

## [2026-11-18] slide & schema | 升級簡報為 6 頁宏觀到微觀漏斗模板並重製 11-18 簡報
- 更新 `AGENTS.md` 第 5.2.5 節，確立「6 頁宏觀到微觀漏斗架構（封面 → 宏觀與匯市 → 全球產業與科技核心主線 → 台股與供應鏈 → 盲盒 → 催化劑）」，並要求頁內附 `[原文]`/`[Wiki]` 小標籤連結、支援內嵌向量圖表及標註來源之 `.callout` 延伸見解。
- 重製 `slides/drafts/11-18-daily-report-slides.md` 與 `slides/html/11-18-daily-report-slides.html`（納入封面金融 K 線背景圖、輝達營收趨勢與台股四萬點攻防兩張內嵌 SVG 圖表，以及跨日對照見解）。

## [2026-11-19] ingest | 匯入 2026-11-19 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 依 `raw/candidates_11-19.json` 經使用者確認選出 7 篇全文存檔至 `raw/`（`walmart-q3-earnings-us-consumer-2026-11-19.md`、`tw-stock-plunge-1768-2026-11-19.md`、`nand-flash-2027-oversupply-2026-11-19.md`、`anthropic-record-ipo-2026-11-19.md`、`trump-blackwell-china-policy-2026-11-19.md`、`gold-silver-fed-minutes-2026-11-19.md`、`trump-putin-apec-meeting-2026-11-19.md`）。
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax 與跨日雙向交叉連結），並更新 `index.html`。

## [2026-11-19] note & slide | 產出 2026-11-19 全球金融市場日報與 6 頁漏斗簡報
- 嚴格依據 `wiki/` 萃取產出 `notes/11-19-daily-report.md`，全篇標註 `[條目名稱](../wiki/xxx.html)` 來源連結，並於文末附上待擴充參考文獻與 Ingest 指令。
- 產出 6 頁漏斗大綱 `slides/drafts/11-19-daily-report-slides.md` 及 Reveal.js + MathJax 網頁簡報 `slides/html/11-19-daily-report-slides.html`（含頁內雙標籤、兩張深色內嵌 SVG 圖表及 `.callout` 跨日／外溢評估）。


## [2026-11-20] ingest | 匯入 2026-11-20 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 執行 `scripts/fetch_candidates.py` 產出 `raw/candidates_11-20.json`（共 54 則候選新聞），依 `AGENTS.md` 第 5.5 節標準自主遴選 7 篇核心文章存檔至 `raw/`（`fed-paulson-interest-rate-guidance-2026-11-20.md`、`phison-nand-flash-ai-growth-2026-11-20.md`、`intel-18a-emib-five-year-contract-tsmc-2026-11-20.md`、`tsmc-samsung-halt-china-chips-us-curbs-2026-11-20.md`、`anthropic-nasdaq-debut-valuation-check-2026-11-20.md`、`gold-slump-dollar-four-week-rally-2026-11-20.md`、`california-subpoena-nvidia-nsa-disruption-2026-11-20.md`）。
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax LaTeX 公式渲染、語意標籤與跨日/跨條目雙向交叉連結），並更新 `index.html` 首頁目錄與最新日報連結。

## [2026-11-20] note & slide | 產出 2026-11-20 全球金融市場日報與 6 頁漏斗簡報
- 嚴格依據 `wiki/` 既有條目萃取產出 `notes/11-20-daily-report.md`，全篇每一論點皆標註 `[條目名稱](../wiki/xxx.html)` 來源標籤，並於文末附上待擴充外部參考文獻與 Ingest 指令。
- 產出 6 頁宏觀到微觀漏斗大綱 `slides/drafts/11-20-daily-report-slides.md` 及 Reveal.js + MathJax 網頁簡報 `slides/html/11-20-daily-report-slides.html`（含封面深色金融背景圖、頁內雙標籤、兩張深色內嵌 SVG 圖表及具類型標註之 `.callout` 見解卡片）。

## [2026-11-20] slide & schema | 重製 11-20 簡報為深度內容版（11 頁）並升級 AGENTS.md 規則
- **用戶需求**：(1) 修正空白過多／內容偏下的排版問題；(2) 每個重點深化為「主標題＋2–3 行敘述＋傳導鏈推論＋台股量化影響估算」；(3) 取消固定 6 頁限制，改為「每主題 1–3 頁，總頁數 < 15 頁」；(4) 其他頁面適當加背景圖。
- **CSS 修復（`assets/slides.css`）**：加入 `display: block !important; top: 0 !important;` 覆蓋 Reveal.js 主題的垂直置中機制，新增 `.supplement` 輔助類別用於傳導鏈與量化說明文字。
- **規則更新（`AGENTS.md` 第 5.2.5 節）**：廢除「固定 6 頁」限制，確立「每主題 1–3 頁彈性、總頁數 ≤ 15、傳導鏈推論為必要項目、量化影響不硬湊、不硬湊無效 URL」的新規範。
- **重製簡報（`slides/html/11-20-daily-report-slides.html`）**：擴充為 11 頁深度版，每頁涵蓋完整傳導鏈推論與台股量化情境分析，各主題頁加入低透明度 Unsplash 主題背景圖，新增輝達傳票 2 頁情境分析矩陣、英特爾封裝格局 SVG 對照表與台股限空令多空情境估算。

## [2026-11-20] slide & style | 解除 SVG 高度限制並大幅放大圖表字級
- **問題診斷**：`assets/slides.css` 內原先設定 `.reveal svg { max-height: 120px; }`，導致 HTML 設定更大 height 時仍被 CSS 硬鎖在 120px，文字縮小難以辨識。
- **樣式修復**：修改 `assets/slides.css` 將 SVG `max-height` 放寬至 `280px`，表格字級提升至 `0.82em`。
- **圖表重繪**：重構黃金破位走勢圖（height: 180px, 字級 13–16px, 粗折線與大數據點）與英特爾封裝對照表（height: 185px, 字級 13.5–16px），確保視覺清晰大方。
- **規則手冊**：同步更新 `AGENTS.md` 圖表字級標準（13.5px–16px）。


## [2026-11-21] ingest | 匯入 2026-11-21 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 執行 `scripts/fetch_candidates.py` 產出 `raw/candidates_11-21.json`（共 54 則候選新聞），依 `AGENTS.md` 第 5.5 節標準自主遴選 7 篇核心文章存檔至 `raw/`（`us-market-correction-nasdaq-ai-rout-2026-11-21.md`、`tw-otc-defaults-four-days-ginko-2026-11-21.md`、`trump-backs-huang-nvidia-second-chance-2026-11-21.md`、`nvidia-post-huang-credit-exposure-taiwan-2026-11-21.md`、`lam-research-zhunan-rd-center-advanced-packaging-2026-11-21.md`、`fed-warsh-communications-rate-hike-pricing-2026-11-21.md`、`trump-penalties-overseas-datacenters-blindbox-2026-11-21.md`）。
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax LaTeX 公式渲染、標準語意標籤與雙向交叉連結），並更新 `index.html` 首頁目錄與最新日報連結。

## [2026-11-21] note & slide | 產出 2026-11-21 全球金融市場日報與 6 頁漏斗簡報
- 嚴格依據 `wiki/` 既有條目萃取產出 `notes/11-21-daily-report.md`，全篇每一論點皆標註 `[條目名稱](../wiki/xxx.html)` 來源標籤，並於文末附上待擴充外部參考文獻與 Ingest 指令。
- 產出 6 頁宏觀到微觀漏斗大綱 `slides/drafts/11-21-daily-report-slides.md` 及 Reveal.js + MathJax 網頁簡報 `slides/html/11-21-daily-report-slides.html`（含封面深色金融背景圖、頁內雙標籤、兩張深色內嵌 SVG 圖表及具類型標註之 `.callout` 見解卡片）。

## [2026-11-21] slide & schema | 診斷 6 頁成因、修正 sidecar 與 AGENTS.md 規範並重製 11-21 簡報為 11 頁深度版
- **問題診斷**：(1) 排程自動化設定檔 `~/.gemini/config/sidecars/daily-rss-candidate-fetcher/sidecar.json` 內的 Prompt 原先仍寫著 `5. 6-Page Funnel Slides ...`，導致每日 8:30 自動被喚醒的 Agent 嚴格執行該 6 頁指令；(2) `AGENTS.md` 主題列表原先編號為 1~6，易導致模型誤判為固定 6 頁。
- **排程與手冊修正**：
  - 更新 `sidecar.json` 提示詞為 `Multi-Page In-Depth Funnel Slides (10–13 slides, maximum 15 slides; strictly do NOT compress into 6 slides)`。
  - 更新 `AGENTS.md` 第 5.2.5 節，明確列出 10–13 頁的推薦結構（封面 1 頁、宏觀 2 頁、匯市 1 頁、美股主線 2 頁、台廠落地 3 頁、盲盒 2 頁、催化劑 1 頁），並嚴禁將日報壓縮為 6 頁。
- **重製 11-21 簡報**：
  - 將 `slides/drafts/11-21-daily-report-slides.md` 與 `slides/html/11-21-daily-report-slides.html` 擴充重構為 **11 頁深度架構**。
  - 完整展開美股三大指數破 200 DMA 修正、櫃買市場連四日違約交割潮、輝達 2,000 億美元信用擔保曝險傳導、科林研發竹南萬坪中心動土，以及川普無預警海外資料中心懲罰盲盒之外溢風險矩陣與情境分析表。


## [2026-11-22] ingest | 匯入 2026-11-22 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 執行 `scripts/fetch_candidates.py` 產出 `raw/candidates_11-22.json`（共 54 則候選新聞），依 `AGENTS.md` 第 5.5 節標準自主遴選 7 篇核心文章存檔至 `raw/`：
  1. 美國總經與政策：`bis-us-ai-chip-curbs-southeast-asia-data-centers-2026-11-22.md`
  2. 台股大盤與核心半導體：`tw-led-cpo-expansion-45b-dingyuan-lige-whitetech-2026-11-22.md`
  3. 台股大盤與核心半導體：`nvidia-sc26-vera-rubin-platform-supercomputing-2026-11-22.md`
  4. 前瞻科技與台廠供應鏈：`anthropic-record-ipo-collides-wall-street-worst-week-2026-11-22.md`
  5. 前瞻科技與台廠供應鏈：`spacex-goldman-apollo-44b-bonds-nvidia-ai-chips-2026-11-22.md`
  6. 國際匯市與大宗避險資產：`gold-xau-usd-breaks-multi-year-uptrend-rate-hike-fear-2026-11-22.md`
  7. 🔮 AI 焦點盲盒：`anthropic-claude-helps-solve-riemann-hypothesis-blindbox-2026-11-22.md`
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax LaTeX 公式渲染、標準語意標籤與雙向交叉連結），並更新 `index.html` 首頁目錄與最新日報簡報連結。

## [2026-11-22] note & slide | 產出 2026-11-22 全球金融市場日報與 11 頁深度漏斗簡報
- 嚴格依據 `wiki/` 既有條目萃取產出 `notes/11-22-daily-report.md`，全篇每一論點皆標註 `[條目名稱](../wiki/xxx.html)` 來源標籤，並於文末附上待擴充外部參考文獻與 Ingest 指令。
- 產出 11 頁宏觀到微觀深度漏斗大綱 `slides/drafts/11-22-daily-report-slides.md` 及 Reveal.js + MathJax 網頁簡報 `slides/html/11-22-daily-report-slides.html`（含封面深色金融背景圖、頁內雙標籤、兩張深色內嵌 SVG 圖表【黃金破位走勢圖、台廠 CPO 45 億元矩陣】及具類型標註之 `.callout` 見解卡片）。

## [2026-11-22] weekly & schema | 建立金融週報規範並首發 2026 年第 47 週全球金融週報（15 頁）
- **規範升級（`AGENTS.md`）**：確立金融週報標準架構，納入「🇺🇸 美股深度體檢（200 DMA破位/板塊避險/估值壓縮）」與「一週 7 大 AI 焦點盲盒外溢評級計分板」，不設頁數限制，深度貫通本週 42 篇 `wiki/` 知識庫。
- **產出深度研究筆記**：生成 `notes/weekly-2026-W47.md`，涵蓋全週利率定價演進、美股三大指數修正、櫃買違約交割潮、盲盒三大灰犀牛聚類與下週戰術作戰地圖，全篇維持 100% 交叉引用。
- **產出 Reveal.js 週報簡報**：生成 `slides/html/weekly-2026-W47-slides.html`（共 15 頁深度架構），包含全週 12 月升息機率位移 SVG、盲盒外溢評級計分板、跨市場催化劑日程表與多空攻防關鍵分水嶺。
- **首頁更新**：於 `index.html` 新增「最新金融週報（Weekly Strategic Report）」專區與跳轉連結。

## [2026-11-22] schema | 週報防單句壓縮與重大事件獨立成頁鐵則寫入 AGENTS.md
- **規範永久固化（`AGENTS.md` 5.6 節）**：
  1. **重大事件獨立成頁原則（One Major Event Per Slide）**：嚴禁將多個獨立重大事件（如輝達 SC26 Vera Rubin 架構與 SpaceX 440 億美元發債買 GPU）強行壓縮於單頁以一句話帶過；凡重大架構發表、巨額融資、監管新規、重大代工長約，一律獨立成專頁充分展開。
  2. **關鍵硬數據、技術規格與結構性條款必留原則**：嚴禁定性空話，強制保留 CUDA 核心數、NVLink 交換機頻寬、MLPerf 效率、Saturn SPV 隔離破產機制、8.05% 利率、防升空贖回條款等核心量化與結構性細節。
  3. **徹底解除頁數天花板（No Artificial Page Cap）**：週報不設頁數上限，依內容深度自然展開為 18–25 頁或更多。
- **自動化排程同步**：更新 `~/.gemini/config/sidecars/weekly-financial-report/sidecar.json` 之每週日 20:00 自動編譯提示詞，強制要求遵循 AGENTS.md 5.6 防壓縮規範。
- **週報簡報實作驗證**：已將 `slides/html/weekly-2026-W47-slides.html` 由 15 頁擴充重製為 19 頁完整獨立版，實踐新版規範標準。

## [2026-11-23] ingest | 匯入 2026-11-23 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 執行 `scripts/fetch_candidates.py` 產出 `raw/candidates_11-23.json`（共 54 則候選新聞），依 `AGENTS.md` 第 5.5 節標準自主遴選 7 篇核心文章存檔至 `raw/`：
  1. 美國總經與政策：`bessent-warns-fed-overtightening-financial-stress-2026-11-23.md`
  2. 台股大盤與核心半導體：`tw-stock-plunge-short-selling-ban-stabilization-fund-2026-11-23.md`
  3. 台股大盤與核心半導體：`us-ai-export-curbs-neocloud-datasection-taiwan-odm-2026-11-23.md`
  4. 前瞻科技與台廠供應鏈：`rapidus-2nm-sram-yield-zero-bottleneck-2026-11-23.md`
  5. 前瞻科技與台廠供應鏈：`softbank-1-trillion-sk-hynix-buyout-explored-2026-11-23.md`
  6. 國際匯市與大宗避險資產：`crude-oil-slides-bessent-challenges-fed-hawkish-rates-2026-11-23.md`
  7. 🔮 AI 焦點盲盒：`blindbox-jensen-huang-affair-megaspeed-chip-smuggling-probe-2026-11-23.md`
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax LaTeX 公式渲染、標準語意標籤與雙向交叉連結），並更新 `index.html` 首頁目錄與最新日報簡報連結。

## [2026-11-23] note & slide | 產出 2026-11-23 全球金融市場日報與 12 頁深度漏斗簡報
- 嚴格依據 `wiki/` 既有條目萃取產出 `notes/11-23-daily-report.md`，全篇每一論點皆標註 `[條目名稱](../wiki/xxx.html)` 來源標籤，並於文末附上待擴充外部參考文獻與 Ingest 指令。
- 產出 12 頁宏觀到微觀深度漏斗大綱 `slides/drafts/11-23-daily-report-slides.md` 及 Reveal.js + MathJax 網頁簡報 `slides/html/11-23-daily-report-slides.html`（含封面深色金融背景圖、頁內雙標籤、兩張深色內嵌 SVG 圖表【原油走跌與美債殖利率回穩對照圖、台股大盤跌點與金管會平盤禁空/國安基金雙軌穩市防線】及具類型標註之 `.callout` 見解卡片）。


## [2026-11-24] ingest | 匯入 2026-11-24 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 執行 `scripts/fetch_candidates.py` 產出 `raw/candidates_11-24.json`（共 54 則候選新聞），依 `AGENTS.md` 第 5.5 節標準自主遴選 7 篇核心文章存檔至 `raw/`：
  1. 美國總經與政策：`fed-oig-probes-bowman-quiet-period-bofa-dinner-2026-11-24.md`
  2. 台股大盤與核心半導體：`tw-stock-rebound-nvidia-huang-reinstated-sox-surge-2026-11-24.md`
  3. 台股大盤與核心半導體：`openai-proposes-perplexity-compute-caps-ai-safety-2026-11-24.md`
  4. 前瞻科技與台廠供應鏈：`us-bis-blacklists-megaspeed-chip-smuggling-taiwan-kyc-2026-11-24.md`
  5. 前瞻科技與台廠供應鏈：`anthropic-launches-claude-ship-autonomous-pr-agents-2026-11-24.md`
  6. 國際匯市與大宗避險資產：`gold-holds-gains-above-3600-huang-rally-risk-hedging-2026-11-24.md`
  7. 🔮 AI 焦點盲盒：`blindbox-republicans-break-trump-huang-smuggling-subpoena-2026-11-24.md`
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax LaTeX 公式渲染、標準語意標籤與雙向交叉連結），並更新 `index.html` 首頁目錄與最新日報簡報連結。

## [2026-11-24] note & slide | 產出 2026-11-24 全球金融市場日報與 12 頁深度漏斗簡報
- 嚴格依據 `wiki/` 既有條目萃取產出 `notes/11-24-daily-report.md`，全篇每一論點皆標註 `[條目名稱](../wiki/xxx.html)` 來源標籤，並於文末附上待擴充外部參考文獻與 Ingest 指令。
- 產出 12 頁宏觀到微觀深度漏斗大綱 `slides/drafts/11-24-daily-report-slides.md` 及 Reveal.js + MathJax 網頁簡報 `slides/html/11-24-daily-report-slides.html`（含封面深色金融背景圖、頁內雙標籤、兩張深色內嵌 SVG 圖表【黃金現貨企穩 3,600 關卡 vs 美元指數回吐走勢、費城半導體指數 vs 台指期夜盤暴衝走勢】及具類型標註之 `.callout` 見解卡片）。

## [2026-11-25] ingest | 匯入 2026-11-25 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 執行 `scripts/fetch_candidates.py` 產出 `raw/candidates_11-25.json`（共 54 則候選新聞），依 `AGENTS.md` 第 5.5 節標準自主遴選 7 篇核心文章存檔至 `raw/`：
  1. 美國總經與政策：`us-macro-pce-anticipation-tech-pullback-2026-11-25.md`
  2. 台股大盤與核心半導體：`tw-stock-historic-rebound-40k-tsmc-supply-chain-2026-11-25.md`
  3. 台股大盤與核心半導體：`nvidia-new-huang-era-500b-financing-platform-2026-11-25.md`
  4. 前瞻科技與台廠供應鏈：`dell-q3-fy27-ai-server-surge-25b-buyback-2026-11-25.md`
  5. 前瞻科技與台廠供應鏈：`anthropic-breaks-83-ipo-price-insider-sales-2026-11-25.md`
  6. 國際匯市與大宗避險資產：`gold-slips-below-3600-us-tariffs-rate-hike-bets-2026-11-25.md`
  7. 🔮 AI 焦點盲盒：`blindbox-trump-open-to-pardoning-huang-15m-gain-2026-11-25.md`
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax LaTeX 公式渲染、標準語意標籤與跨日／跨條目雙向交叉連結），並更新 `index.html` 首頁目錄與最新日報簡報連結。

## [2026-11-25] note & slide | 產出 2026-11-25 全球金融市場日報與 11 頁深度漏斗簡報
- 嚴格依據 `wiki/` 既有條目萃取產出 `notes/11-25-daily-report.md`，全篇每一論點皆標註 `[條目名稱](../wiki/xxx.html)` 來源標籤，並於文末附上待擴充外部參考文獻與 Ingest 指令。
- 產出 11 頁宏觀到微觀深度漏斗大綱 `slides/drafts/11-25-daily-report-slides.md` 及 Reveal.js + MathJax 網頁簡報 `slides/html/11-25-daily-report-slides.html`（含封面深色金融背景圖、頁內雙標籤、三張深色內嵌 SVG 圖表【黃金 3,600 關卡反轉攻防 vs 12 月升息定價、AI 軟硬體雙極化定價對照、台股 11/19–11/24 V 型收復四萬點走勢】及具類型標註之 `.callout` 見解卡片）。


## [2026-11-26] ingest | 匯入 2026-11-26 五大類 7 篇財經新聞（含 AI 國際焦點盲盒）
- 執行 `scripts/fetch_candidates.py` 產出 `raw/candidates_11-26.json`（共 54 則候選新聞），依 `AGENTS.md` 第 5.5 節標準自主遴選 7 篇核心文章存檔至 `raw/`：
  1. 美國總經與政策：`us-macro-oct-pce-beige-book-dow-v-reversal-2026-11-26.md`
  2. 台股大盤與核心半導體：`tw-stock-plunge-1926-301-tariffs-taiwan-15-cap-2026-11-26.md`
  3. 台股大盤與核心半導體：`tsmc-arizona-expansion-ceremony-trump-dec4-2026-11-26.md`
  4. 前瞻科技與台廠供應鏈：`sp-nvidia-credit-downgrade-review-ai-cds-surge-2026-11-26.md`
  5. 前瞻科技與台廠供應鏈：`spacex-fcc-1m-orbital-ai-satellites-starmind-2026-11-26.md`
  6. 國際匯市與大宗避險資產：`gold-falls-below-3500-one-year-low-hot-pce-tariffs-2026-11-26.md`
  7. 🔮 AI 焦點盲盒：`blindbox-pentagon-dpa-vance-alice-huang-270m-china-2026-11-26.md`
- 編譯產出對應 7 篇 `wiki/*.html` 頁面（含 MathJax LaTeX 公式渲染、標準語意標籤與跨日／跨條目雙向交叉連結），並更新 `index.html` 首頁目錄與最新日報簡報連結。

## [2026-11-26] note & slide | 產出 2026-11-26 全球金融市場日報與 11 頁深度漏斗簡報
- 嚴格依據 `wiki/` 既有條目萃取產出 `notes/11-26-daily-report.md`，全篇每一論點皆標註 `[條目名稱](../wiki/xxx.html)` 來源標籤，並於文末附上待擴充外部參考文獻與 Ingest 指令。
- 產出 11 頁宏觀到微觀深度漏斗大綱 `slides/drafts/11-26-daily-report-slides.md` 及 Reveal.js + MathJax 網頁簡報 `slides/html/11-26-daily-report-slides.html`（含封面深色金融背景圖、頁內雙標籤、三張深色內嵌 SVG 圖表【黃金貫破 3,500 美元 vs 12 月升息完全定價、AI 信用市場 CDS 利差與違約風險壓力表、台股寬幅巨震與外資連 8 賣籌碼對照】及具類型標註之 `.callout` 見解卡片）。