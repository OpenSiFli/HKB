# HKB —— SiFli 硬件知识库（Hardware Knowledge Base）

> 一个**可直接下载到本地、供 AI 工具检索与原理图评审使用**的 SiFli（思澈科技）MCU 硬件知识库。
> **无网页版、不走文档站点构建**——本仓库的目的就是让你 `git clone` 下来，用本地 AI 助手 / RAG 直接读取，回答硬件设计问题、评审原理图。

---

## 一、这是什么

HKB（Hardware Knowledge Base）把分散在规格书、用户手册、硬件设计指南、参考设计、官方 Checklist、AVL 物料清单与工程复盘中的 SiFli MCU 硬件知识，结构化沉淀为一套**纯文本 / Markdown 知识资产**，供开发者在本地离线使用：

- **AI 硬件问答**：把本仓库作为上下文喂给 AI 助手，检索封装、引脚、电气参数、外设、电源架构、约束禁忌等问题。
- **原理图评审（Schematic Review）**：依据仓库内的校验规则（`check_rules`）与设计规范（`design_rules`）、参考设计（黄金样板），让 AI 对照检查你的原理图 PDF。

本仓库**不是**网页文档站，也不含任何构建流水线；它只是把内部知识库（Obsidian Vault）的**结构化产物**原样分发，让你在本地直接打开或喂给 AI。

---

## 二、仓库内容总览

仓库根目录只有三样东西：`LICENSE`、`README.md`，以及承载全部知识的 **`Knowledge Base/`** 文件夹。

> `Knowledge Base/` 本身就是一份独立 **Obsidian Vault** 的内容根目录——你可以直接用 Obsidian 打开它，也可以用任意编辑器 / AI 把整个文件夹当上下文读取。

```
HKB/
├── LICENSE
├── README.md
└── Knowledge Base/                         ← 知识库主体（可整体作为 AI 上下文）
    ├── wiki/                               ← 结构化知识层（114 篇 Markdown）
    │   ├── mcu/all/                        ← MCU 全系列硬件知识
    │   │   ├── chip_entity/                芯片实体（封装/引脚/电气参数/约束/勘误）           8 篇
    │   │   ├── peripheral/                 外设专项（GPIO/电源/时钟/ADC/USB/串口/音频/存储…） 23 篇
    │   │   ├── pinmux/                     引脚复用矩阵（SF32LB52 / SF32LB57）
    │   │   ├── check_rules/                原理图 AI 审图校验规则（CR_* 等）                 42 条
    │   │   ├── design_rules/               设计规范（电源/GPIO/复位/调试/BOOT/PA34…）
    │   │   ├── fault_case/                 故障案例（I2C 卡死/调试失效/漏电/SDMMC 溢出…）
    │   │   ├── hardware_design_guide/       官方硬件设计指南（3.3V 与 电池 两系列各一份）
    │   │   ├── reference_design/            官方参考设计原理图（黄金样板）
    │   │   ├── avl/                        AVL 合格物料库（全系列通用，晶体/Buck/Nor Flash/…）
    │   │   ├── sources/                    原始资料来源摘要页（永久保留 Raw 双链溯源）
    │   │   ├── concepts/                   硬件基础概念
    │   │   ├── report_template/             评审 / 故障报告模板
    │   │   └── summary_topic/              综合主题综述（同系列对比/改版差异）
    │   └── dev_board/all/                  开发板知识库（与 MCU 平级，以原理图为主要依据）
    │       ├── board_entity/               板卡实体（11 项核心参数）
    │       ├── schematics/                 原理图结构化提取
    │       └── sources/                    来源摘要
    ├── cmd/                                ← 18 条"入库指令"提示词（新增/更新各类资料的标准 SOP）
    ├── .workbuddy/skills/                  ← 3 个 WorkBuddy 自定义技能（随仓库拷贝即用）
    │   ├── eda-schematic-review             EDA 原理图 PDF 评审（核心：对照 check_rules 出分级报告）
    │   ├── kb-ingest-dispatch              知识库入库总调度（自然语言 → 路由到 cmd/ 指令）
    │   └── sf32lb52-hw-design-guide-ingest  SF32LB52 家族硬件设计指南入库
    ├── .obsidian/                          ← Obsidian Vault 配置（用 Obsidian 打开即得一致体验）
    ├── AGENTS_MCU_ALL.md                   ← 知识库运维规范（13 条强制约束 + Schema 三层架构）
    ├── AGENTS_INGEST_MCU.md                ← 规格书自动入库工作流（七步 SOP）
    ├── index_MCU_ALL.md                    ← MCU 知识库全局导航索引
    ├── index_DEVBOARD_ALL.md               ← 开发板知识库全局导航索引
    ├── log_MCU_ALL.md                      ← MCU 变更日志（仅追加）
    ├── log_DEVBOARD_ALL.md                 ← 开发板变更日志（仅追加）
    ├── 调用指令参考提示词.md                ← 入库调度路由表（18 条指令总入口）
    ├── EDA原理图PDF识别提示词.md            ← 原理图/PCB PDF 高精度文字提取方法（方案A 矢量 / 方案B OCR）
    ├── _gen_checklist_cr.py                ← 从官方 Checklist 生成 CR_Checklist_* 审图规则的脚本
    └── _gen_sf32lb57_pinmux.py             ← 从官方 pinmux xlsx 生成 SF32LB57_Pinmux.md 的脚本
```

---

## 三、覆盖的芯片家族

知识库按两大家族组织，每族各含**两个独立系列，不能合并看待**（文档大小写与命名严格对应）：

| 家族 | 系列 | 供电特征 |
| --- | --- | --- |
| **SF32LB52** | `SF32LB52X`（大写 X）= 3.3V 供电系列 | 无充电电路，主电 PVDD，GPIO 由 VDDIOA 供电 |
| | `SF32LB52x`（小写 x）= 电池供电系列 | 内置 560mA 充电，电源引脚 VBUS/VBAT/VCC |
| **SF32LB57** | `SF32LB57X`（大写 X）= 3.3V 供电系列 | 无充电电路，主电 PVDD，GPIO 由 VDDIOA 供电 |
| | `SF32LB57x`（小写 x）= 电池供电系列 | 内置充电模块，电源引脚 VBUS/VBAT/VCC/VSYS |

> 📌 文档标题大小写与芯片系列**一致**：3.3V 系列用大写 X（如 DS5202-SF32LB52X），电池系列用小写 x（如 DS5201-SF32LB52x）。

---

## 四、给开发者的使用方法

```bash
git clone https://github.com/OpenSiFli/HKB.git
```

克隆后，把 **`Knowledge Base/`** 整个文件夹作为上下文提供给你的 AI 工具即可，**无需任何构建步骤**。

### 方式 A：用 Obsidian 打开
直接用 Obsidian 打开 `Knowledge Base/` 文件夹，即可获得双链、反向链接与图谱视图（Vault 配置已随 `.obsidian/` 一起分发）。

### 方式 B：喂给任意 AI / RAG
把 `Knowledge Base/` 作为项目上下文（WorkBuddy、Claude、本地模型、MCP 知识源等），直接提问：
- "SF32LB52x 电池系列的电源引脚有哪些？充电电流多大？"
- "SF32LB57X 的 GPIO 默认上下拉状态是什么？"
- "Audio ADC 单端输入需要多大的隔直电容？"

### 方式 C：原理图 AI 评审（推荐 WorkBuddy）
把本仓库作为 WorkBuddy 项目打开，`.workbuddy/skills/eda-schematic-review` 会被**自动发现并加载**。上传你的原理图 PDF 并要求"评审原理图"，技能会：
1. 用 `EDA原理图PDF识别提示词.md` 的方案A（pdfplumber 矢量文本）提取位号/参数/网络/坐标；
2. 先判定 MCU 型号与版本（锂电版 / 常规版，误判会推翻整份报告）；
3. 逐条对照 `wiki/mcu/all/check_rules/`（42 条规则）给出 **通过 / 命中 / 待核实 / 不适用** 分级结论与整改建议；
4. 产出带风险分级的评审报告（Markdown + PDF）。

> 评审依赖 Python 环境：`pdfplumber` + `fpdf2`（技能 `SKILL.md` 内有建 venv 与中文字体的详细说明）。

### 方式 D：入库新资料（需在拥有完整 Vault 的环境）
参考 `调用指令参考提示词.md` 路由表，用 `kb-ingest-dispatch` 技能以自然语言触发对应 `cmd/` 指令（如"新增 xxx 规格书"）。**注意**：入库流程依赖 `raw/` 原始资料层，而本仓库**不含 `raw/`**（见下节），因此方式 D 仅适用于你本地拥有完整知识库 Vault 的环境，普通下载用户无需使用。

---

## 五、本仓库「不含」的内容（分发时已排除）

为了保证仓库轻量且规避内部资料外泄，以下两个目录**刻意未随本仓库分发**：

- **`raw/`**（源库约 56MB）：规格书 PDF、数据表、参考设计、企业规范、故障原始复盘等**唯一事实源头**。
- **`review_schematic/`**（源库约 2.1MB）：原理图评审的中间产物（提取 JSON、文本、图片、报告草稿）。

`wiki/` 中的每篇页面都已**永久保留对 `raw/` 原始资料的双链溯源引用**，但原始文件本身不在仓库内。如果你需要原始资料或更完整的入库/评审能力，请在内部知识库环境中操作。

---

## 六、技能与依赖

- `Knowledge Base/.workbuddy/skills/` 下的 3 个技能随仓库分发，**拷贝到 WorkBuddy 项目即自动加载**，无需机器专属配置。
- `eda-schematic-review` 评审需要 Python 3 + `pdfplumber` + `fpdf2`。
- `_gen_checklist_cr.py` / `_gen_sf32lb57_pinmux.py` 是知识库生成期的辅助脚本（从官方 Checklist / pinmux xlsx 产出 `wiki/` 规则与矩阵），随仓库提供以备复现，日常问答/评审不依赖它们。

---

## 七、备注

- `Knowledge Base/` 文件夹名含空格，若你的脚本/工具对空格敏感，可重命名为 `Knowledge_Base` 或 `knowledge-base`（同步更新 README 内提及路径即可）。
- `.obsidian/workspace.json` 是个人视图状态，若不想沿用仓库默认布局可删除，其余 Vault 配置建议保留。
- 所有页面以 Obsidian 风格双链（`[[...]]`）互相关联；不支持双链的查看器也能正常做纯文本检索。

---

## 八、相关资源

- SiFli 官网：<https://www.sifli.com/>
- 芯片选型与开发板 Wiki：<https://wiki.sifli.com/> 、<https://wiki.sifli.com/en/>
- SDK 文档：<https://docs.sifli.com/>
- SiFli SDK（GitHub）：<https://github.com/OpenSiFli/SiFli-SDK>
- 官方论坛（BBS）：<https://bbs.sifli.com/>
- 商务联系：sales@sifli.com

---

## 九、License

本仓库文档采用 **Apache License 2.0**，详见 [LICENSE](./LICENSE)。
