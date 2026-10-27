---
title: SF32LB52X Datasheet V0.2.6 来源摘要
type: mcu_source
aliases: ["SF32LB52X规格书V0.2.6","DS5202-SF32LB52X-EN","SF32LB52X 3.3V规格书"]
tags: ["企业MCU","芯片系列-SF32LB52","型号-SF32LB52x 3.3V系列","原始资料","原理图审图/故障分析/报告输出"]
sources: [[raw/mcu/all_chip/datasheets/DS5202-SF32LB52X-Datasheet V0p2p6.pdf]]
mcu_family: ["SF32LB52"]
mcu_series: ["3.3V供电系列"]
mcu_model: ["SF32LB52X 3.3V系列","SF32LB52BU36","SF32LB52BU56","SF32LB52DUB6","SF32LB52EUB6","SF32LB52GUC6","SF32LB52JUD6"]
hardware_version: ["QFN68L"]
created: 2026-08-10
updated: 2026-08-10
---

## 摘要
SiFli（思澈科技）**SF32LB52X（大写 X）3.3V 供电系列** MCU 原厂规格书 V0.2.6（英文版，2026-02-06），覆盖一款带双模 BT5.3 的超低功耗 AIoT MCU 全量硬件信息：双核 Cortex-M33 STAR-MC1、576KB SRAM、QFN68L 封装、45 GPIO，适用于可穿戴/智能 HMI/工业传感。本页为该规格书的结构化来源索引，绑定原始 PDF 双链。

> **系列归属**：本规格书描述 **SF32LB52X（大写 X）3.3V 供电系列**（无充电电路，主电 PVDD，GPIO 由 VDDIOA 供电）。原厂文档标题即为「SF32LB52X」（大写 X），与芯片命名（大写 X=3.3V）**一致**。同家族电池系列（DS5201，小写 x）见 [[SF32LB52x_Datasheet_V2.5.5]]。

## 来源基本信息
- 原始文件：[[raw/mcu/all_chip/datasheets/DS5202-SF32LB52X-Datasheet V0p2p6.pdf]]
- 文档类型：MCU 原厂 Datasheet
- 厂商：SiFli Technologies (Nanjing) Co., Ltd.（思澈科技）
- 文档版本 / 编号：V0.2.6 / DS5202-SF32LB52X-EN
- 生效硬件版本：QFN68L 封装全系
- 适配 MCU 系列 / 型号：SF32LB52x（小写 x）3.3V 系列（具体型号见订购信息表 5-7，PVDD 随型号 3.3V/1.8V）

## 核心硬件内容（摘要摘录）
- 双核 big.LITTLE：HCPU Cortex-M33 STAR-MC1 @240MHz（512KB SRAM）+ LCPU @24MHz（64KB SRAM），合计 576KB SRAM。
- 无线：双模 BT5.3（BLE/BR/EDR），集成 Balun 与天线匹配网络，BRF_ANT 引脚（53）。
- 封装 QFN68L（7×7×0.85mm，0.35mm pitch），含 EPAD（69）。
- 多电源域：PVDD / VDDIOA / AVDD33 / AVDD33_AUD / AVDD_BRF / VDD_SIP / VDD_RET / VDD_RTC。
- 外设：45 GPIO、3×UART(+2 LPSYS)、4×I2C、2×SPI、1×I2S、1×PDM、USB2.0 FS、12-bit GPADC(4Msps)、24-bit Audio DAC/ADC、TIM/PWM、DMA、MPI/SDMMC、LCD/GPU、安全加速。
- 极限电气：供电 1.71~3.63V（PVDD 随型号 3.3V/1.8V），绝对最大 +3.63V，ESD HBM ±4kV / CDM ±1kV。

## 手册关键章节页码索引（便于溯源）
| 主题 | 章节 | 页码 |
|------|------|------|
| 特性总览 Features | §1–§3 | P3–P28 |
| 存储器映射 Address Mapping | Table 1-1 | P4–P7 |
| 中断列表 Interrupt List | Table 1-2 | P6–P8 |
| 电源管理架构 Power Management | §1.4 / Fig 1-3 | P8–P9 |
| 外设详述（UART/I2C/SPI/I2S/PDM/USB/TIM/DMA/存储/安全） | §3.5–§3.8 | P15–P28 |
| 电气特性 Electrical Characteristics | §4 / Table 4-1~4-19 | P29–P37 |
| 推荐工作条件 / 绝对最大额定值 | Table 4-1 / 4-2 | P29 |
| I/O 特性 @3.3V / @1.8V | Table 4-3 / 4-4 | P29–P30 |
| 可靠性 Reliability（ESD/Latch-up/MSL 等） | Table 4-5 | P30 |
| 封装与硬件 Packaging | §5 | P38–P50 |
| 引脚布局 Pinout（图） | Fig 5-1 | P38 |
| GPIO(PA) 引脚表 | Table 5-2 | P40–P46 |
| 专用引脚表（电源/RF/模拟/IO） | Table 5-3 | P47 |
| 回流焊曲线 / 订购信息 | Table 5-4~5-7 | P49–P50 |

## 关联页面
- 芯片实体（3.3V 系列）：[[SF32LB52X]]｜电池系列实体：[[SF32LB52x_batt|SF32LB52x]]｜家族总览：[[SF32LB52]]｜电池系列规格书：[[SF32LB52x_Datasheet_V2.5.5]]
- 外设专项：[[SF32LB52_Peripheral_GPIO]]、[[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_Clock]]、[[SF32LB52_Peripheral_GPADC]]、[[SF32LB52_Peripheral_BLE_RF]]、[[SF32LB52_Peripheral_USB]]、[[SF32LB52_Peripheral_Serial]]、[[SF32LB52_Peripheral_Audio]]、[[SF32LB52_Peripheral_Memory]]、[[SF32LB52_Peripheral_Timer_PWM]]、[[SF32LB52_Peripheral_I2S_PDM]]
- 校验规则：见 `wiki/mcu/all/check_rules/` 下 CR_* 系列

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw 存储路径：raw/mcu/all_chip/datasheets/DS5202-SF32LB52X-Datasheet V0p2p6.pdf，关键页码/条款：Table 4-1~4-19（P29–P37）、Table 5-2（P40–P46）、Table 5-3（P47）、Table 5-7（P50）

## 待核实问题
- 文档未明确给出独立「BOOT 启动引脚配置逻辑」「复位电路标准原理图」「下载/调试接口完整标准电路」章节文本（SWD 引脚为 PA18=SWDIO、PA19=SWCLK），相关最小系统细节建议结合 SiFli 参考设计核对待核实。
- PVDD 具体电压（3.3V 或 1.8V）随订购型号而定，原理图取电需按具体型号（Table 5-7）。
- 是否已有独立勘误手册（errata）未在 datasheet 内，建议补充至 raw/mcu/all_chip/errata/。
