---
title: index_MCU_ALL
type: index
aliases: ["MCU全系列硬件知识库导航","全局索引"]
tags: ["企业MCU","全局导航","索引"]
created: 2026-08-10
updated: 2026-09-09
---

# 企业全系列 MCU 硬件综合知识库 —— 全局导航索引

> 多维分类入口：按 **芯片系列 / 外设模块 / 业务场景** 交叉检索。所有页面均以 Obsidian 双链互相关联。

---

## 一、Schema 规则层（运维入口）
- [[AGENTS_MCU_ALL]] —— 核心运维规范与 13 条强制约束
- [[AGENTS_INGEST_MCU]] —— 规格书自动入库工作流（单份 datasheet 拆解 SOP）
- [[log_MCU_ALL]] —— 变更日志（仅追加）
- 本页 —— 全局导航索引

### 入库流程快捷入口
- 新增 MCU 规格书时，按 [[AGENTS_INGEST_MCU]] 七步流程执行：检索查重 → 建来源页 → 建/补芯片实体 → 补外设页 → 生校验规则 → 更导航/日志 → 双链校验。

---

## 二、按芯片系列 / 型号检索
- 芯片实体库：`wiki/mcu/all/chip_entity/`
  - 每一款 MCU 独立页面，收录封装、引脚、电气参数、极限规格、典型电路、约束禁忌、勘误、原厂/企业规范。
  - 待补充芯片型号请在此登记，并去 `wiki/mcu/all/sources/` 建立来源摘要页。

### 已入库芯片型号（SF32LB52 家族 —— 含电池 / 3.3V 两个独立系列）
> 52 家族含**两个独立系列，不能合并看待**：**SF32LB52X（大写 X）= 3.3V 供电系列**（无充电电路，主电 PVDD，GPIO 由 VDDIOA 供电）；**SF32LB52x（小写 x）= 电池供电系列**（内置 560mA 充电，电源引脚 VBUS/VBAT/VCC）。两系列共用用户手册 [[SF32LB52X_UserManual_V0.8.8]]。📌 文档标题大小写与芯片系列**一致**：3.3V 系列写在 **DS5202-SF32LB52X**（标题大写 X）、电池系列写在 **DS5201-SF32LB52x**（标题小写 x）。
- [[SF32LB52]] —— 家族总览页（两系列导航 + 文档→系列映射说明）
- 电池系列：[[SF32LB52x_batt|SF32LB52x]]（芯片实体，来源 DS5201-SF32LB52x V2.5.5）
  - 来源摘要（电池规格书）：[[SF32LB52x_Datasheet_V2.5.5]]（DS5201-SF32LB52x-EN V2.5.5，Release：订购命名 520/523/525/527 / 充电器全参数 / 音频 DAC·ADC 实测 / IO 四档驱动）
- 3.3V 系列：[[SF32LB52X]]（芯片实体，来源 DS5202-SF32LB52X V0.2.6）
  - 来源摘要（3.3V 规格书）：[[SF32LB52X_Datasheet_V0.2.6]]（DS5202-SF32LB52X-EN V0.2.6：PVDD 供电，型号 52B/52D/52E/52G/52J，无充电电路）
- 来源摘要（用户手册，两系列共用）：[[SF32LB52X_UserManual_V0.8.8]]（UM5201-SF32LB52x-CN V0.8.8，371 页寄存器/编程型手册，补全电源双版本/复位源/BOOT寄存器/低功耗电压表/调试接口）
- 外设专项（11 页，`wiki/mcu/all/peripheral/` 下 `SF32LB52_Peripheral_*`）：GPIO / 电源 / 时钟 / GPADC / BLE-RF / USB / 串口(UART-I2C-SPI) / 音频 / 存储(MPI-SDMMC) / 定时器PWM / I2S-PDM（两系列共用；电源架构与电源专用引脚差异见 [[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_GPIO]]）
- 引脚复用矩阵（PINMUX，1 页，`wiki/mcu/all/pinmux/` 下 `SF32LB52_Pinmux.md`）：HPSYS 大核 PA00–PA44 完整复用 + LPSYS 小核 PB00–PB03（映射 PA00–PA03）+ SIP Group A 内部 PAD 说明；**以 `SF32LB52_pinmux_20230707.xlsx` 为权威依据**，并标注与规格书 Table 5-2 的差异（GPADC 通道 +1、USART1 Debug UART 缺失等）。源文件已导入 `raw/mcu/all_chip/pinmux/`。
- 硬件设计指南（Hardware Design Guide，2 页，`wiki/mcu/all/hardware_design_guide/` 下 `SF32LB52X_Hardware_Design_Guide.md` / `SF32LB52x_batt_Hardware_Design_Guide.md`）：SiFli 官方 wiki 硬件设计指南，**3.3V 系列（SF32LB52X，后缀 B/E/G/J）** 与 **电池系列（SF32LB52x，后缀 0/3/5/7）** 各一份，含封装/典型方案/原理图（电源·时钟·射频·显示·存储·按键·音频）/PCB 设计（叠层·走线·EMI/ESD）全章节与全部图片（59 张去重后本地化）。两份 1:1 忠实 PDF 见 `raw/mcu/all_chip/hw_design/`（SF32LB52X_3V3_HW_Application.pdf / SF32LB52x_batt_HW_Application.pdf），原始 HTML 同目录备份。
- 参考设计原理图（Reference Schematic，2 页，`wiki/mcu/all/reference_design/` 下 `SF32LB52X_3V3_Reference_Schematic.md` / `SF32LB52x_batt_Reference_Schematic.md`）：SF32LB52X（3.3V 系列）与 SF32LB52x（电池系列）官方参考设计原理图结构化提炼（**黄金样板**），含电源架构 / 关键 BOM / 设计要点与对应审图规则。原始 PDF 归档于 `raw/mcu/ref_design/SF32LB52X_3V3/`、`raw/mcu/ref_design/SF32LB52x_batt/`（文本提取见 `review_schematic/output/`）。
- 校验规则（38 条，`wiki/mcu/all/check_rules/` 下 `CR_*`）：多电源域 / 绝对最大额定值 / EPAD接地 / 低功耗浮空IO / GPADC源电阻 / 48M晶振 / BLE天线 / USB差分对 / 复位电平 / VBATS范围【规格书 10 条】＋ BOOT寄存器 / PWRKEY复位 / 调试接口PA18-PA19 / I2C总线卡死 / ATIM断路BKIN / SDMMC-MPI2互斥 / GPIO默认PUPD / Hibernate合封供电【用户手册 8 条】＋ 参考设计衍生 7 条：外挂存储供电(PA21/PA11) / 32K晶振 / eMMC·SD Nand上拉 / 接口电平匹配VDDIOA / LCD FPC EMI / 电池OVP充电器 / 电池电源树【参考设计 7 条】＋ 官方 Checklist 衍生 13 条（来源 [[SF32LB52_Checklist_V0.1_20241008]]）：封装 / 电源-供电(严重) / 电源-功耗 / 时钟 / 存储(严重) / 射频 / 多媒体-显示 / 多媒体-音频 / 通用接口(按键·UART·I2C·SPI·GPADC·USB) / 硬件外部唤醒 / 调试和下载 / EOS&ESD(严重) / 产线
- 设计规范（7 条，`wiki/mcu/all/design_rules/` 下 `DR_*`）：电源架构 / GPIO默认PUPD高阻 / 低功耗IO保持 / 复位设计 / 调试接口 / BOOT模式 / **PA34电源键引脚作普通GPIO使用（52/57 双家族，含 PWRKEY_CNT 与 PMUC WER.PWRKEY 关闭）**（均来自用户手册 V0.8.8，PA34 GPIO 规范含 57 规格书 V0.2）
- 故障案例（4 条，`wiki/mcu/all/fault_case/` 下 `FC_*`）：I2C总线卡死 / 调试接口失效 / Hibernate合封漏电 / SDMMC-FIFO溢出（均来自用户手册 V0.8.8 衍生复盘）
### 已入库芯片型号（SF32LB57 家族 —— 含电池 / 3.3V 两个独立系列）
> 57 家族同样含**两个独立系列，不能合并看待**：**SF32LB57X（大写 X）= 3.3V 供电系列**（无充电电路，主电 PVDD(19)，GPIO 由 VDDIOA(21) 供电）；**SF32LB57x（小写 x）= 电池供电系列**（内置充电模块，电源引脚 VBUS(21)/VBAT(20)/VCC(24)/VSYS(19)）。📌 文档标题大小写与芯片命名**一致**：3.3V 系列写在 **DS5702-SF32LB57X**（大写 X）、电池系列写在 **DS5701-SF32LB57x**（小写 x），与 52 家族规则相同。
> ⚠️ **两份规格书均为 V0.2 草稿**（2026-09-09），`Table 4-5 处理器功耗` / `Table 4-6 BT/BLE 功耗` **全部 TBD**；两册电气表共用导致 VBUS/VBAT/VCC 与 PVDD 并存，**引脚归属以各册 Table 5-3 为准**。
- [[SF32LB57]] —— 家族总览页（两系列导航 + 文档→系列映射 + 引脚差异对照表）
- 3.3V 系列：[[SF32LB57X]]（芯片实体，来源 DS5702-SF32LB57X V0.2；封装 QFN68/QFN80/BGA112，46~58 GPIO（以 pinmux 表为准；规格书标 47 待核））
  - 来源摘要：[[SF32LB57X_Datasheet_V0.2_20260909]]（DS5702-SF32LB57X-CN V0.2，84 页）
- 电池系列：[[SF32LB57x_batt|SF32LB57x]]（芯片实体，来源 DS5701-SF32LB57x V0.2；**订购信息仅列 QFN68**——DS5701 已详述 QFN80/BGA112 但料号缺失，属规格书【严重】缺陷）
  - 来源摘要：[[SF32LB57x_batt_Datasheet_V0.2_20260909]]（DS5701-SF32LB57x-CN V0.2，85 页）
  - 📌 电池系列页面文件名带 `_batt` 后缀（NTFS 不区分大小写，`SF32LB57X_*.md` 与 `SF32LB57x_*.md` 会冲突），引用写 `[[SF32LB57x_batt|SF32LB57x]]`
- 外设专项（10 页，`wiki/mcu/all/peripheral/` 下 `SF32LB57_Peripheral_*`）：电源 / GPIO / 时钟 / GPADC / 音频 / 蓝牙射频 / 串口(UART-I2C-SPI-CAN) / 存储(MPI-SD-eMMC) / 定时器PWM / 显示与图形(ePicasso·LCD·DCMI·eZip)（两系列共用；**双系列电源引脚差异见 [[SF32LB57_Peripheral_Power]]**）
- 引脚复用矩阵（PINMUX，1 页，`wiki/mcu/all/pinmux/SF32LB57_Pinmux.md`）：**已按官方 `pinmux - 202600901.xlsx` 逐行转录**——大核 GPIO Group A（PA00–PA57，QFN68=46 / QFN80·BGA112=58 GPIO）完整复用总表 + matrix index（160 交叉信号）+ LCD mux（IF_SEL/DPI）；电池与 3.3V 两系列共用同一套大核 GPIO 复用矩阵。原件已归档 `raw/mcu/all_chip/pinmux/`
- 校验规则（2 条，`wiki/mcu/all/check_rules/` 下 `CR_SF32LB57_*`）：**双系列电源引脚匹配（致命）** / **绝对最大额定值与 IO 约束（严重）**
- 通用（跨家族）校验规则（1 条）：[[CR_Audio_ADC_Input]]——**音频 ADC 输入要求**：单端/差分隔直电容（≥2.2µF）、输入范围随增益变化（单端 ±0.68V / 差分 ±1.35V @0dB，再除以增益）、IO 耐压 3.3V（绝对最大 3.63V）、信号地与芯片地共地；适用于**所有带音频 ADC 的思澈 MCU**（SF32LB52 / SF32LB57 已导入并适用）
- 尚未导入：用户手册（UM）、硬件设计指南、官方 Checklist、参考设计原理图

- AVL 合格物料库（SIFLI MCU **全系列通用**，`wiki/mcu/all/avl/` 下 `SIFLI_MCU_AVL_V0.4_20260812.md` + 6 个分类页）：SiFli 官方 **AVL 认证物料清单 V0.4（2026-08-12）**，覆盖**所有 SIFLI MCU 型号**（不限于 SF32LB52 系列）——分类含晶体 / Buck 电感 / Nor Flash / SPI Nand Flash / SD Nand Flash / LCD 驱动（TP 驱动当前为空）。原始 Excel 归档于 `raw/mcu/all_chip/avl/`，仅读取不修改；BOM 选型须从此表选取，优先级高于器件原厂规格书。

## 三、按外设模块检索
- 外设专项库：`wiki/mcu/all/peripheral/`
  - GPIO / ADC / DAC / UART / SPI / I2C / CAN / PWM / LCD / Flash / RAM / 存储接口 / 模拟前端 / 功率驱动 / 外部拓展 / 安规电路 / EMC-EMI 配套电路
- 硬件基础概念：`wiki/mcu/all/concepts/`
- 通用设计规范：`wiki/mcu/all/design_rules/`（电源、信号、接地、阻抗、高低压隔离、器件选型）

## 四、按业务场景检索
### 1. 知识全文检索
- 入口：全库向量检索；分类页见 `chip_entity`、`peripheral`、`concepts`、`design_rules`。

### 2. PDF 原理图 AI 审图
- 校验规则库：`wiki/mcu/all/check_rules/`（判定条件 / 违规现象 / 风险等级 / 整改方案 / 知识库依据）
- 企业审图标准原始资料：`raw/mcu/company_spec/hardware/`

### 3. 故障复盘 / 售后支持
- 故障案例库：`wiki/mcu/all/fault_case/`（失效现象 / 根因 / 整改 / 适用型号 / 规避规则）
- 原始故障复盘：`raw/mcu/case/fault_raw/`、`raw/mcu/test/report_raw/`

### 4. 自动输出标准化报告
- 报告模板库：`wiki/mcu/all/report_template/`（评审报告 / 故障分析报告话术与引用逻辑）
  - 评审报告模板 `[[_template|硬件评审报告模板]]` 已按 [[硬件评审报告排版与UI规范_V1.0]] 重构：三类状态分离（等级 P0-P2／事实状态／处理状态）、5 列问题总表、证据图与防视觉误导规范（附录 A/B）。
- 报告排版与 UI 规范（来源摘要）：[[硬件评审报告排版与UI规范_V1.0]]（V1.0，2026-10-16）
- 报告模板原始资料：`raw/mcu/company_spec/report/`（含《硬件评审报告排版与UI规范_V1.0》）

## 五、综合主题综述
- 同系列对比 / 改版差异 / 多型号兼容设计：`wiki/mcu/all/summary_topic/`

## 六、原始资料（Raw）导航
- 规格书/勘误：`raw/mcu/all_chip/datasheets/`、`raw/mcu/all_chip/errata/`
- 规格书内部一致性核查报告（DS5701/DS5702 V0.2）：`raw/mcu/all_chip/datasheets/一致性核查报告_V0p2-20260909.md`、`一致性核查报告_DS5702_V0p2-20260909.md`（及同名 .pdf）；含电池册订购信息缺失 QFN80/BGA112 料号【严重】项
- 官方硬件 Checklist：`raw/mcu/all_chip/design_checklist/`（SF32LB52 Checklist V0.1 20241008，衍生 13 条 `CR_Checklist_*` 审图规则）
- 硬件设计指南（Hardware Design Guide，PDF）：`raw/mcu/all_chip/hw_design/`
- 参考设计/PCB/BOM：`raw/mcu/ref_design/`
- 企业规范/报告模板：`raw/mcu/company_spec/`（评审报告排版与UI规范 V1.0：`raw/mcu/company_spec/report/硬件评审报告排版与UI规范_V1.0.md`）
- 问题/故障原始：`raw/mcu/case/`、`raw/mcu/test/`
- 评审纪要/技术问答/工程师笔记：`raw/mcu/meeting/`、`raw/mcu/tech_chat/`、`raw/mcu/engineer_notes/`
- 外围器件规格：`raw/mcu/vendor/device_spec/`

---

## 七、来源摘要页（所有 Raw 资料索引）
- `wiki/mcu/all/sources/` —— 每份原始资料对应一份摘要页，永久保留 Raw 双链。

---

> 维护约定：新增/更新页面后，须同步在此索引补充入口，并追加 [[log_MCU_ALL]] 记录（遵循 AGENTS_MCU_ALL 第 7、8 条）。
