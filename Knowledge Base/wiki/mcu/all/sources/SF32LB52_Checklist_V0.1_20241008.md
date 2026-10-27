---
title: SF32LB52硬件设计Checklist V0.1
type: mcu_source
aliases: ["SF32LB52_Checklist","SF32LB52设计检查表","SF32LB52硬件Checklist"]
tags: ["企业MCU","芯片系列-SF32LB52","原始资料","原理图审图/故障分析/报告输出","官方设计Checklist"]
sources: [[raw/mcu/all_chip/design_checklist/SF32LB52_Checklist_V0.1_20241008]]
mcu_family: ["SF32LB52"]
mcu_model: ["SF32LB52X家族","SF32LB52x家族"]
hardware_version: ["QFN68L"]
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
SiFli 官方 **SF32LB52 硬件设计 Checklist（V0.1，20241008）**，覆盖全系列型号的硬件设计自查清单，按「封装 / 电源 / 功耗 / 时钟 / 存储 / 射频 / 多媒体（显示·音频）/ 通用接口（按键·UART·I2C·SPI·GPADC·USB）/ 硬件外部唤醒 / 调试下载 / EOS&ESD / 产线」18 个章节、155 条核查事项，每条标注「适用芯片」（所有型号 / 电池供电系列 / 3.3V 供电系列 / SF32LB52DUB6）。本页作为官方黄金样板的来源摘要，已逐条转化为 `wiki/mcu/all/check_rules/` 下 `CR_Checklist_*` 审图规则。

## 来源基本信息
- 原始文件：[[raw/mcu/all_chip/design_checklist/SF32LB52_Checklist_V0.1_20241008]]（原件另存于全局 `D:/.workbuddy/SF32LB52_Checklist.md`，仅归档不移动）
- 文档类型：原厂官方硬件设计 Checklist（企业规范 / 参考设计类）
- 厂商 / 部门：SiFli（炬芯系 SF32LB52 平台）
- 文档版本 / 编号：V0.1
- 生效日期：20241008
- 适配 MCU 系列 / 型号：SF32LB52 全系列（SF32LB52X 3.3V 系列 + SF32LB52x 电池系列；含 DUB6 等子型号）

## 核心硬件内容（摘要摘录）
- **封装**：原理图库正确性、PCB 封装按规格书制作（所有型号）。
- **电源·供电**：VBUS/VBAT/VCC/VSYS/VDD33_VOUT1·2/PVDD/VBATS/AVDD_*/VDDIOA/VDD18_VOUT/GPADC_VREF/AUD_VREF 等各电源域的电压范围、供电来源、电容规格（容值/耐压/就近摆放）、走线线宽、BUCK 电感/反馈参数、OVP/充电器选型（电池系列）、DUB6 的 1.8V 外供要求。
- **电源·功耗**：LDO/DCDC 与 MOS 电源开关使能设计、外部启动介质电源控制（PA21）、VSYS/VDD33_VOUT 上拉功耗、I2C 上拉通断、Deep Sleep/Standby 底电流。
- **时钟**：48M 主晶振与 32.768K RTC 晶振型号合规与参数（CL/ppm/ESR）、PA24~PA27 输出 32K、布局/屏蔽/禁铺铜/间距。
- **存储**：MPI3 外接 Nor/Nand/SD Nand/eMMC 上拉（PA13/PA15/PA17 的 7.5kΩ 规则）、电源控制、AVL 型号、IO 电平匹配、双 Flash（CS=PA12/PA26）、EMC。
- **射频**：ANT 50Ω 阻抗、PI 匹配、PA00/PA01 控 RX_EN/TX_EN、RF 走线阻抗/屏蔽/地层完整性/高速与大电流隔离。
- **多媒体·显示**：QSPI/SPI/8080/JDI/EPD 引脚分配、高速信号 EMI（RC）、FPC 远天线/内层、屏电源开关、IO 电平。
- **多媒体·音频**：MEMS/ECM MIC 由 MIC_BIAS 供电、ADC 隔直电容、DAC 端阻容、ADCP/DACP/DACN 走线屏蔽与寄生电容约束、模拟电源包地。
- **通用接口**：按键（PA34 开关机/10s 复位/10kΩ 下拉主板端）、UART（交叉接线/PA35·PA36 复位态/IO 电平）、I2C（上拉/唤醒/地址）、SPI（接线/时序/电平）、GPADC（PA28~PA34/0~3.3V/分压精度1%/100nF 滤波/包地）、USB（接线/ESD/插拔检测/PA35·PA36 高阻）。
- **硬件外部唤醒**：唤醒中断仅限 PA24~PA27、PA34~PA44 共 15 路。
- **调试下载**：DBG_UART PA18(RXD)/PA19(TXD)，源端串 100Ω。
- **EOS&ESD**：充电/电池/天线/LCD·TP/心率接口 ESD 防护。
- **产线**：测试点完整性（VBAT/3.3V、GND、PA18/PA19、VSYS/VDD33_VOUT1、PA34）、布局与夹具规格。

## 关联页面
- 芯片实体：[[SF32LB52X]]、[[SF32LB52x_batt]]
- 校验规则（Checklist 衍生）：[[CR_Checklist_Package]]、[[CR_Checklist_Power]]、[[CR_Checklist_PowerConsumption]]、[[CR_Checklist_Clock]]、[[CR_Checklist_Storage]]、[[CR_Checklist_RF]]、[[CR_Checklist_Display]]、[[CR_Checklist_Audio]]、[[CR_Checklist_Interface]]、[[CR_Checklist_Wakeup]]、[[CR_Checklist_Debug]]、[[CR_Checklist_ESD]]、[[CR_Checklist_Production]]
- 既有相关 CR（已交叉引用）：[[CR_PowerDomains]]、[[CR_RefDesign_Batt_PowerTree]]、[[CR_RefDesign_Batt_OVP_Charger]]、[[CR_VBATS_Range]]、[[CR_AbsMaxRatings]]、[[CR_XTAL48M]]、[[CR_RefDesign_XTAL32K]]、[[CR_RefDesign_ExternalFlash_Power]]、[[CR_RefDesign_EMMC_SD_Pullup]]、[[CR_SDMMC_MPI2_Exclusive]]、[[CR_BLE_RF_Antenna]]、[[CR_RefDesign_LCD_FPC_EMI]]、[[CR_I2C_BusStuck]]、[[CR_USB_DPDM]]、[[CR_Reset_PWRKEY]]、[[CR_DebugInterface_PA18_PA19]]、[[CR_GPIO_Default_PUPD]]

## 原始来源完整引用
1. [SF32LB52 Checklist V0.1 20241008]，Raw：raw/mcu/all_chip/design_checklist/SF32LB52_Checklist_V0.1_20241008.md（原件 D:/.workbuddy/SF32LB52_Checklist.md），全 18 章节 155 条核查事项。

## 待核实问题
- 无（官方 Checklist 黄金样板，参数以原文为准；DUB6 的 1.8V 外供要求已在 电源 章节单列）。
