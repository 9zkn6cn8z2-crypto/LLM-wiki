# AGENTS.md — LLM 研究知識庫協作規則手冊

本文件為本專案的 AI 協作與知識庫維護規範（Schema），參考 Andrej Karpathy 的 **LLM Wiki** 模式設計，適用於所有協助維護本專案的 AI Agent 與開發者。

---

## 1. 專案目的

* **核心定位**：建立一個靜態網頁版的「LLM 研究知識庫（LLM Wiki）」，系統化整理與累積 LLM 相關研究知識（包含 Prompt 技巧、Agent 概念、RAG 基礎與財金／演算法研究等）。
* **運作理念（累積式知識庫）**：
  * 採用 **Raw（原始資料）→ Wiki（編譯知識）→ Schema（規則手冊）→ Derived（衍生筆記與簡報）** 的單向累積架構。
  * 人類負責蒐集與提供原始資料；AI 負責閱讀、摘要、建立雙向／交叉連結，並將知識進一步萃取為研究筆記與網頁簡報。
* **技術原則**：
  * **核心知識庫（`index.html`、`wiki/*.html`）**：堅持使用純 HTML5 與單一外部 CSS（`assets/style.css`），**不使用任何前端框架、套件管理器或建置工具**，確保任何瀏覽器都能直接開啟閱讀。
  * **網頁簡報（`slides/html/*.html`）**：允許透過 CDN 引入輕量級的 **Reveal.js** 框架以支援簡報互動性，並使用獨立樣式表 `assets/slides.css`。
  * **數學公式支援**：所有 `wiki/*.html` 頁面與 `slides/html/*.html` 簡報模板，皆須透過 CDN 引入 **MathJax**，以支援財金與演算法相關的 LaTeX 數學公式渲染。

---

## 2. 網頁的整體風格與頁面結構

* **知識庫視覺風格**：類似 Notion 與 GitHub 文件的簡潔排版，以**白底黑字**為主，輔以淺灰邊框與程式碼區塊底色，重視行距、留白與閱讀舒適度。
* **知識庫版面配置**：單欄置中閱讀區（最大寬度 `760px`），統一引入 `assets/style.css`。
* **簡報視覺風格**：獨立由 `assets/slides.css` 控制，採深色量化金融專業風格，不與 `assets/style.css` 混用，確保文件閱讀與簡報投影互不干擾。
* **全站核心結構**：
  * `index.html`：知識庫首頁與全站索引目錄（對應 LLM Wiki 的 `index.md`），依主題分類列出所有 Wiki 頁面連結與一句話摘要。
  * `wiki/*.html`：各主題與概念的獨立知識頁面，彼此透過相對路徑超連結交叉引用。
  * `log.md`：按時間順序追加（append-only）的純文字維護日誌，記錄每次匯入、整理、健檢與衍生產出的歷程。
  * `notes/*.md`：嚴格基於 `wiki/` 內容萃取的嚴謹研究筆記。
  * `slides/drafts/*.md`：由研究筆記萃取的逐頁簡報文字大綱。
  * `slides/html/*.html`：可直接在瀏覽器播放的 Reveal.js HTML 簡報檔。

---

## 3. 新增內容時要遵守的 HTML 格式

### 3.1 Wiki 知識頁面規範（`wiki/*.html`）
* **語意化標籤**：一律使用標準 HTML5 語意標籤（`<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<footer>`），**禁止使用行內樣式（inline `style`）**，所有視覺外觀交由 `assets/style.css` 控制。
* **強制交叉連結**：內文只要提及本知識庫中已存在的其他概念或頁面，必須使用相對路徑 `<a href="...">` 連向該 `.html` 頁面。
* **強制引入 MathJax**：`<head>` 內必須載入 MathJax CDN，以便正確渲染 `$...$` 或 `$$...$$` 公式。
* **標準頁面骨架**：

```html
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>頁面標題 — LLM 研究知識庫</title>
  <link rel="stylesheet" href="../assets/style.css">
  <script>
    window.MathJax = {
      tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] }
    };
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
  <header class="site-header">
    <nav class="site-nav">
      <a href="../index.html" class="site-title">LLM 研究知識庫</a>
      <a href="../index.html">返回索引</a>
    </nav>
  </header>

  <main>
    <article>
      <h1>頁面主標題</h1>
      <p class="meta">最後更新：YYYY-MM-DD ｜ 資料來源：raw/對應檔名</p>

      <section>
        <h2>核心概念</h2>
        <p>內文說明，提及既有條目時請加上 <a href="other-page.html">交叉連結</a>。</p>
      </section>

      <section>
        <h2>重點整理 / 範例</h2>
        <ul>
          <li>重點項目一</li>
          <li>重點項目二</li>
        </ul>
      </section>

      <section class="related-links">
        <h2>相關條目</h2>
        <ul>
          <li><a href="related-topic.html">相關主題名稱</a></li>
        </ul>
      </section>
    </article>
  </main>

  <footer class="site-footer">
    <p>LLM 研究知識庫 · 基於純 HTML / CSS 建置</p>
  </footer>
</body>
</html>
```

### 3.2 HTML 簡報模板規範（`slides/html/*.html`）
* 透過 CDN 引入 **Reveal.js**（核心 CSS 與 JS）與 **MathJax**，並引入專案自訂深色量化金融樣式 `../../assets/slides.css`。
* 每張投影片對應一個 `<section>`，頁數與內容須與對應的 `slides/drafts/*.md` 保持一致。
* 封面頁或需全螢幕背景圖的投影片，可搭配 `data-background-image` 與 `data-background-opacity="0.3"`，或套用 `slides.css` 定義的 `.bg-overlay` 遮罩樣式。

---

## 4. 檔案命名與資料夾結構

* **命名規範**：
  * 所有資料夾與檔案名稱一律使用 **全小寫英文字母 + 連字號（kebab-case）**，**不可包含空白或中文**（例：`rag-basics.html`、`rag-study-2026-11-17.md`、`rag-study-slides.html`）。
  * 頁面的顯示標題（`<title>` 與 `<h1>`）使用繁體中文（必要時可保留英文專有名詞）。
* **資料夾結構**：

```text
.
├── AGENTS.md              # AI 協作與維護規則手冊（本文件）
├── index.html             # 知識庫首頁與分類索引目錄
├── log.md                 # 依時間順序追加的維護紀錄
├── assets/
│   ├── style.css          # 知識庫共用的極簡白底黑字樣式表
│   ├── slides.css         # HTML 簡報專用的深色量化金融樣式表
│   └── images/            # 專屬數據截圖與分析圖表（由人類手動放入）
├── raw/                   # 原始參考資料區（文章、論文筆記、摘錄等，唯讀）
├── wiki/                  # AI 編譯與維護的正式 HTML 知識頁面
├── notes/                 # 嚴格基於 wiki/ 萃取的研究筆記（.md）
└── slides/
    ├── drafts/            # 由筆記萃取的逐頁簡報文字大綱（.md）
    └── html/              # Reveal.js 網頁簡報成品（.html）
```

* **圖片資源雙軌制規則**：
  * **裝飾性圖片與背景**：優先使用外部線上合法圖庫（如 Unsplash 等）的 URL 直接渲染，避免本機倉庫過大。
  * **專屬數據與分析圖表**：由人類手動截圖並放入 `assets/images/`，AI 在編排 `slides/html/*.html` 時須使用相對路徑（例如 `<img src="../../assets/images/xxx.png">`）引用；若位於 `wiki/*.html` 則使用 `../assets/images/xxx.png`。

---

## 5. AI 修改或新增內容時需要遵守的規則

### 5.1 權限與邊界
* **`raw/` 絕對唯讀**：`raw/` 內的檔案是知識庫的事實來源（Source of Truth），AI **只能讀取，絕對不可修改、重新命名或刪除**。
* **核心層與衍生層隔離**：
  * **核心層（`wiki/`、`index.html`）**：僅可透過 `ingest`、`query`（經確認沉澱）或 `lint` 流程更新。
  * **衍生層（`notes/`、`slides/drafts/`、`slides/html/`）**：產出筆記或簡報時，**不得逆向修改 `wiki/` 或 `index.html`**。若要將筆記中的建議文獻納入知識庫，必須另行執行標準的 `ingest` 流程。

### 5.2 五大標準作業流程（Operations）

1. **匯入新知（Ingest）**
   * 讀取 `raw/` 中的新資料，萃取核心概念與重點。
   * 在 `wiki/` 建立新頁面或更新既有頁面（依循第 3.1 節 HTML 格式並含 MathJax）。
   * 檢查並補上新舊頁面之間的交叉連結。
   * 更新 `index.html` 的分類目錄與一句話摘要。
   * 在 `log.md` 檔案最末端追加一筆 `ingest` 紀錄。

2. **問答沉澱（Query）**
   * 回答使用者的提問時，優先查閱 `index.html` 與 `wiki/` 既有頁面並附上出處。
   * 若對話中產出了有價值的比較表、綜合分析或新洞察，應主動提議（或依指示）將其整理為 `wiki/` 的新頁面。

3. **定期健檢（Lint）**
   * 檢查全站是否存在**孤兒頁面**（沒有任何其他頁面連入的條目）、**無效連結**、或**已被提及多次但尚未獨立成頁的概念**。
   * 檢查不同頁面之間是否有論點衝突或過時資訊，並回報給使用者確認。

4. **嚴謹研究筆記（Note）**
   * 儲存位置：`notes/<topic>-<YYYY-MM-DD>.md`。
   * **防腦補鐵則（100% 來自 Wiki）**：筆記正文**必須完全依賴 `wiki/` 現有內容**，嚴禁將尚未收錄進 `wiki/` 的網路搜尋結果或 AI 預訓練知識寫入正文。
   * **強制來源標記**：正文的每一段落或核心論點，皆須附上 `[條目名稱](../wiki/xxx.html)` 的來源標記。
   * **知識缺口處理**：若 `wiki/` 針對該主題資料不足或無相關條目，正文須明確標示：「**目前知識庫尚無相關收錄**」，不可自行補齊。
   * **文末擴充待辦格式**：可上網搜尋相關新資訊，但須統一置於筆記最下方的「`## 建議參考文獻與擴充方向`」區塊，每筆必須附上明確的外部 URL，並格式化為便於 AI 讀取的指令提示，例如：
     ```markdown
     - [文章標題或主題](https://example.com/article) — 簡述建議補充的重點。
       > 欲收錄此文獻，請複製此連結並要求 AI 執行 Ingest 流程。
     ```

5. **簡報生成（Slide Draft → HTML）**
   * **階段一：文字分頁草稿（`slides/drafts/<topic>-slides.md`）**
     * 依據對應的 `notes/*.md` 萃取可報告的逐頁大綱。
     * 統一使用 `---` 作為分頁分隔符號。
     * **每頁限制 3–5 個短句**，確保投影易讀性（可於頁尾附加 `Note:` 講者備忘）。
   * **階段二：HTML 網頁簡報（`slides/html/<topic>-slides.html`）**
     * 將 `slides/drafts/` 逐頁大綱轉換為 Reveal.js HTML 簡報（含 MathJax 與 `../../assets/slides.css`）。
     * 需在簡報開頭或備註標明依據之筆記與產出日期。

### 5.3 日誌格式規範（`log.md`）
每次完成操作後，須在 `log.md` 末尾追加一筆紀錄，開頭格式固定如下：

```markdown
## [YYYY-MM-DD] <ingest | query | lint | note | slide> | 操作標題
- 簡述本次新增、更新或檢查的檔案與重點。
```

### 5.4 衝突處理與漸進原則
* **衝突標註**：若新匯入的資料與既有 `wiki/` 內容矛盾，**不可靜默覆蓋**，應於頁面中明確標註來源差異與時間背景，並向使用者說明。
* **漸進修改**：每次只針對明確需求的範圍進行新增或微調，未經使用者同意，不得擅自重構全站結構或引入額外框架／腳本。
