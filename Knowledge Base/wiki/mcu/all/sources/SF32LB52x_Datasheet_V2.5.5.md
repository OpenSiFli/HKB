---
title: SF32LB52x Datasheet V2.5.5 来源摘要
type: mcu_source
aliases: ["SF32LB52x规格书V2.5.5","DS5201-SF32LB52x-EN V2.5.5"]
tags: ["企业MCU","芯片系列-SF32LB52","型号-SF32LB52家族","原始资料","原理图审图/故障分析/报告输出"]
sources: [[raw/mcu/all_chip/datasheets/DS5201-SF32LB52x-Datasheet V2p5p5.pdf]]
mcu_family: ["SF32LB52"]
mcu_series: ["电池供电系列"]
mcu_model: ["SF32LB52x电池系列","SF32LB520U36","SF32LB523UB6","SF32LB525UC6","SF32LB527UD6","SF32LB523LUB6"]
hardware_version: ["QFN68L"]
created: 2026-08-10
updated: 2026-08-10
---

## 摘要
SiFli（思澈科技）SF32LB52x（小写 x）电池供电系列 MCU 原厂规格书 **V2.5.5（英文版，DS5201-SF32LB52x-EN，Release 正式发布版）**，覆盖一款带双模 BT5.3 的超低功耗 AIoT MCU 全量硬件信息：双核 Cortex-M33 STAR-MC1、576KB SRAM、QFN68L 封装、44 GPIO（无 PA21），适用于可穿戴/智能 HMI/工业传感。本页为该规格书的结构化来源索引，绑定原始 PDF 双链，并标注相对 V0.2.6 的**新增/变更/冲突**要点（命名体系、VBAT 范围、IO 驱动表、充电器全参数、音频 DAC/ADC 实测指标）。

> **版本定位**：V2.5.5 为 Release 正式版（文档状态规则：1.0.0~1.9.9 为 Official release）。修订史末条 2025-12-10「Updated the ordering information for 523LUB6 in table 5-7」。与既有 V0.2.6（DS5202）相比，**订购型号命名体系已变更**，需保留两套并核对映射。
>
> **系列归属**：本规格书描述 **SF32LB52x（小写 x）电池供电系列**（内置 560mA 锂电充电，电源引脚 VBUS/VBAT/VSYS/VCC）。原厂文档标题即为「SF32LB52x」（小写 x），与芯片命名（小写 x=电池）**一致**。同家族 3.3V 系列（DS5202，大写 X）见 [[SF32LB52X_Datasheet_V0.2.6]]。

## 来源基本信息
- 原始文件：[[raw/mcu/all_chip/datasheets/DS5201-SF32LB52x-Datasheet V2p5p5.pdf]]
- 文档类型：MCU 原厂 Datasheet
- 厂商：SiFli Technologies (Nanjing) Co., Ltd.（思澈科技）
- 文档版本 / 编号：V2.5.5 / DS5201-SF32LB52x-EN
- 生效硬件版本：QFN68L 封装全系
- 适配 MCU 系列 / 型号：SF32LB52X 家族（具体型号见订购信息表 5-7，V2.5.5 官方订购码见下）

## 核心硬件内容（摘要摘录）
- 双核 big.LITTLE：HCPU Cortex-M33 STAR-MC1 @240MHz（32KB I-Cache + 16KB D-Cache，512KB SRAM）+ LCPU @24MHz（64KB SRAM），合计 576KB SRAM；性能 984 CoreMark、1.5 DMIPS/MHz、4.02 CoreMark/MHz。
- 无线：双模 BT5.3（BLE/BR/EDR），芯片集成 Balun；BLE 灵敏度 ‑100dBm(1Mbps) / ‑95.5dBm(EDR2)，最大 Tx 13dBm(EDR2)，Rx 2.4mA@3.8V。
- 封装 QFN68L（7×7×0.85mm，0.35mm pitch），**44 GPIO（电池系列无 PA21；Features「Others」标 44 GPIO 与正文 Table 5-2 一致，既往「以 Table 5-2 的 45 为准」为误判，计数差异已澄清：电池系列共 44 GPIO、无 PA21）**。
- 多电源域：PVDD / VDDIOA / AVDD33 / AVDD33_AUD / AVDD_BRF / VDD_SIP / VDD_RET / VDD_RTC；锂电版 VBUS/VBAT/VCC 体系（详见电源页）。
- 外设：**44 GPIO（无 PA21）**、3×UART、4×I2C、2×SPI、1×I2S、1×PDM、USB2.0 FS、12-bit GPADC(8ch)、24-bit Audio DAC/ADC、TIM/PWM、DMA、MPI/SDMMC、LCD/GPU、安全加速。
- 极限电气：供电 1.71~3.63V（PVDD 随型号 3.3V/1.8V），绝对最大 +3.63V，ESD HBM ±4kV / CDM ±1kV。
- SiP 存储接口频率：NOR-Flash 最高 96MHz（支持 DTR）；OPI-PSRAM 最高 144MHz（Table 3-1 / Features）。

## 手册关键章节页码索引（datasheet 印刷页码，便于溯源）
| 主题 | 章节 | 页码(印刷) |
|------|------|------|
| 特性总览 Features（CPU/存储/外设/电源/Others） | §1 之前 | P3–P6 |
| 修订历史 Revision History | — | P2 |
| 系统架构 / 总线 / 时钟 / 存储类型 | §1.1–§1.3 | P1–P13 |
| 存储器映射 Address Mapping | Table 1-1 | P4 |
| 中断列表 Interrupt List | Table 1-2 | P6 |
| 外设详述（UART/I2C/SPI/MPI/存储/GPADC/音频/USB 等） | §3 | P14–P28 |
| GPADC 规格 | Table 3-1 | P14 |
| 常用接口速率 Common Interface Rates | Table 3-2 | P29 |
| 电气特性 Electrical Characteristics | §4 / Table 4-1~4-19 | P30–P38 |
| 推荐工作条件 / 绝对最大额定值 | Table 4-1 / 4-2 | P30 |
| I/O 特性 @3.3V | Table 4-3 | P30 |
| 可靠性 Reliability（ESD/Latch-up/MSL 等） | Table 4-4 | P31 |
| 处理器功耗 / BT&BLE 功耗 | Table 4-5 / 4-6 | P32 |
| BLE/经典蓝牙 RF 特性 | Table 4-7~4-15 | P33–P36 |
| 音频 ADC 特性 | Table 4-16 | P37 |
| 音频 DAC 特性 | Table 4-17 | P37 |
| 充电器特性 Charger | Table 4-18 | P38 |
| IO 驱动强度 IO Drive Strength（DS1/DS0 四档） | Table 4-19 | P38 |
| 封装与硬件 Packaging and Hardware | §5 | P39–P51 |
| 引脚类型 Pin Types | Table 5-1 | P40 |
| 引脚布局 Pinout（图 5-1） | Fig 5-1 | P39 |
| GPIO(PA) 引脚表 | Table 5-2 | P41–P47 |
| 专用引脚表（电源/RF/模拟/IO） | Table 5-3 | P48 |
| 封装尺寸 / 载带 / 卷盘 / 回流焊 | Table 5-2~5-6 | P49–P51 |
| 订购信息 Ordering Information | Table 5-7 | P51 |

## 相对 V0.2.6 的新增 / 变更 / 冲突要点
1. **订购型号命名体系变更（重要）**：V2.5.5 Table 5-7 官方订购码为 `SF32LB520U36 / SF32LB523UB6 / SF32LB525UC6 / SF32LB527UD6 / SF32LB523LUB6`（5 款，分别对应 8/32/64/128/32Mb 存储）；而 V0.2.6（DS5202）订购表为 `SF32LB52BU36/BU56/DUB6/EUB6/GUC6/JUD6`（6 款）体系。**两套命名不同，跨版本型号映射待核实**，两版均保留不覆盖。
2. **VBAT 电池电源输入范围**：V2.5.5「Others」明确 `VBAT voltage range: 3.2V–4.7V`；既有实体页/电源页记 `VBATS(20)` 为电池**电压测量**输入 0~4.7V。二者为不同引脚/含义，电池主电输入范围以 V2.5.5 为准，与锂电版 `VBAT(4V 充电输出)` 的关系待核实。
3. **IO 驱动能力两系列一致（非冲突）**：V2.5.5 Table 4-19 可配置四档驱动（DS1/DS0：2/4/8/12 mA）测试条件为 **VOH=0.9×VDDIO**；V0.2.6 文本 `@3.3V 最大 12/30/38 mA（min/typ/max）` 测试条件为 **VOH=0.8×VDDIO**。两组为同一驱动电路在两种 VOH 测试条件下的结果，**两系列 IO 驱动能力完全相同**（见 GPIO 页与两实体页）。
4. **充电器全参数（新增细节）**：V2.5.5 Table 4-18 补全 Vbus 4.6–5.5V、Itri 0.5–56mA、Vcc(trickle→const) 3V、Vrechg Vcv‑0.15V、Vhigh 4.5V、Ileak 30nA、Icc 5–560mA、Vcv 4.2–4.45V、Iend 10%×Icc（既有实体页仅有 560mA/4.2–4.45V 概要）。
5. **音频 DAC/ADC 实测指标（新增）**：V2.5.5 Table 4-16/4-17 给出 Audio DAC 24-bit、Output Swing 1.1Vrms、THD+N ‑102dB、Dynamic Range 109dB、Noise Floor 3.7µVrms、SNR 109dB；Audio ADC 24-bit、Gain ‑6~18dB(6dB/step)、Input R 23kΩ、DR 99dB、THD+N ‑76dB。
6. **GPIO 数量（已澄清）**：Features「Others」写 44 GPIO，正文 Table 5-2 列 PA00–PA44（**不含 PA21**），电池系列无 PA21，共 44 GPIO，与 Features 一致；既往「以 Table 5-2 的 45 为准」为误判，实际电池系列为 44 GPIO（无 PA21），3.3V 系列 SF32LB52X 才为 45 GPIO（含 PA21）。

## 关联页面
- 芯片实体（电池系列）：[[SF32LB52x_batt|SF32LB52x]]｜3.3V 系列实体：[[SF32LB52X]]｜家族总览：[[SF32LB52]]｜3.3V 系列规格书：[[SF32LB52X_Datasheet_V0.2.6]]
- 外设专项：[[SF32LB52_Peripheral_GPIO]]、[[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_Clock]]、[[SF32LB52_Peripheral_GPADC]]、[[SF32LB52_Peripheral_BLE_RF]]、[[SF32LB52_Peripheral_USB]]、[[SF32LB52_Peripheral_Serial]]、[[SF32LB52_Peripheral_Audio]]、[[SF32LB52_Peripheral_Memory]]、[[SF32LB52_Peripheral_Timer_PWM]]、[[SF32LB52_Peripheral_I2S_PDM]]
- 校验规则：见 `wiki/mcu/all/check_rules/` 下 CR_* 系列

## 原始来源完整引用
1. [DS5201-SF32LB52x-Datasheet V2p5p5.pdf]，Raw 存储路径：raw/mcu/all_chip/datasheets/DS5201-SF32LB52x-Datasheet V2p5p5.pdf，关键页码/条款：Table 4-1~4-19（P30–P38）、Table 4-17/4-18/4-19（P37–P38）、Table 5-2（P41–P47）、Table 5-3（P48）、Table 5-7（P51）

## 待核实问题
1. **订购型号跨版本映射**：V2.5.5 命名（520/523/525/527）与 V0.2.6（52B/52D/52E/52G/52J）体系不同，具体哪款对应哪款需核对 SiFli 官方型号对照或 errata（待核实）。
2. **VBAT 与 VBATS 关系**：V2.5.5「Others」VBAT 3.2–4.7V（电源输入） vs 既有 VBATS(20) 0–4.7V（测量输入）为不同引脚；锂电版 `VBAT(4V 充电输出)` 与 V2.5.5「VBAT 3.2–4.7V」是否同一网络/不同工况，待核实。
3. **大量电气/引脚表为图片**：Table 4-1~4-19 中多数值表、Table 5-2/5-3 引脚细节、封装尺寸图 5-2 等为位图，pypdf 仅能提取文本骨架，**具体数值需 OCR 或人工核对**，禁止据此编造未提取到的参数。
4. **GPIO 计数**：Features 标 44、Table 5-2 实列 45，以 Table 5-2 为准，差异待官方澄清。
5. **独立 errata 勘误手册**：是否已存在独立勘误手册，建议放入 raw/mcu/all_chip/errata/ 后补充勘误页（待核实）。
