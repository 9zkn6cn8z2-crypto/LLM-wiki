# 鎧俠攜手輝達以 NVMe SSD 擴充 GPU 記憶體突破 1.1 PB、支援 2 兆個向量：突破 HBM 容量天花板並重塑企業級 SSD 需求（2026-11-27）

> 來源：[TechNews 科技新報 - 鎧俠攜手輝達以 SSD 擴充 GPU 記憶體容量，突破 1 PB 並支援處理 2 兆個向量 (2026-11-27)](https://finance.technews.tw/2026/11/27/kioxia-and-nvidia-collaborate-to-expand-gpu-memory-capacity-via-ssds/)

## 核心事實與量化數據
* **鎧俠（Kioxia）與輝達（NVIDIA）聯手突破 HBM 物理容量限制**：
  * 鎧俠於 11/27 宣布與輝達展開深度技術合作，結合輝達 **NVIDIA SCADA（Scaled Accelerated Data Access）** 軟體函式庫、**Storage-Next** 計畫與鎧俠高速 NVMe SSD，將有效 GPU 記憶體容量推進至 **PB（Petabyte）等級**。
  * **核心痛點**：隨著 AI 訓練與推論資料集膨脹，GPU 內建高頻寬記憶體（HBM）面臨嚴峻容量瓶頸；若僅仰賴 HBM，工作負載必須被切分為小區段，並在記憶體與慢速儲存間反覆搬移資料（Data Thrashing），拖累吞吐效率。
* **GB200 NVL72 概念驗證（PoC）硬指標全公開（截至 2026/11/26 測試）**：
  * **測試平台架構**：採用具備 **18 個伺服器節點** 的 **NVIDIA GB200 NVL72** 機櫃級（Rack-scale）系統。
  * **SSD 配置規模**：全機櫃搭載 **144 顆 KIOXIA XD8 系列 7.68 TB E1.S NVMe SSD**（每個節點支援 **8 顆** SSD），提供近 **60 TB／節點** 的快閃記憶體擴充容量，整機櫃原始 SSD 擴充容量突破 **1.1 PB**。
  * **細粒度與向量處理極限**：透過 NVIDIA SCADA 支援 **512 位元組（512-byte）** 精細小區塊直接資料存取，單一機櫃架構即可支撐處理高達 **2 兆個（2 Trillion）512-byte 向量**，直攻超大規模向量資料庫（RAG / Vector DB）、推薦系統與圖神經網路（GNNs）。
  * **次世代產品藍圖**：鎧俠同步預告持續開發現行 **XD8 系列** 與創新 **KIOXIA GP 系列超高 IOPS SSD**，因應 AI 與 HPC 算力對極限隨機讀寫效能的需求。

## 因果傳導鏈推論
$$\text{AI 模型參數與 RAG 向量庫膨脹撞擊 HBM 容量牆} \longrightarrow \text{NVIDIA SCADA + Storage-Next 導入 512B 精細 SSD 直連存取} \longrightarrow \text{單櫃 GB200 NVL72 標配 144 顆 E1.S SSD（1.1 PB / 2 兆向量）} \longrightarrow \text{企業級 NAND/SSD 控制 IC 與高速儲存伺服器結構性放量}$$

## 知識庫連貫與衝突
* **呼應記憶體產業供需結構重塑**：
  * 本週知識庫已追蹤 [群聯深耕 AI SSD 方案對抗消費性景氣波動](phison-nand-flash-ai-growth-2026-11-20.html)、[2027 年 NAND Flash 傳統消費性過剩風險](nand-flash-2027-oversupply-2026-11-19.html) 以及 [軟銀 1 兆美元收購 SK 海力士傳聞反映 HBM 咽喉價值](softbank-1-trillion-sk-hynix-buyout-explored-2026-11-23.html)。
  * 鎧俠與輝達此次突破證實，**高階企業級 NVMe SSD（PCIe Gen5 / E1.S / 超高 IOPS）** 正在從傳統「冷儲存外設」躍升為「GPU 擴充記憶體階層（Memory Tiering）」的核心算力元件，有效對沖消費級 NAND 潛在過剩風險，並直接利多台灣 NAND 控制晶片廠（如**群聯 8299**，長期深耕企業級 PCIe Gen5 SSD 與 aiDAPTIV+ 記憶體擴充生態）、記憶體模組封測廠及高密度 E1.S 伺服器機櫃供應鏈。

## 短線催化劑
* **2026/12/01–12/03 輝達華府大會與後續 Storage-Next 合作夥伴揭露**：觀察 NVIDIA SCADA 函式庫對更多企業級 SSD 控制 IC 廠及台灣伺服器 ODM（鴻海、廣達、緯創、緯穎）GB200/GB300 機櫃設計導入（Design-in）進度。
