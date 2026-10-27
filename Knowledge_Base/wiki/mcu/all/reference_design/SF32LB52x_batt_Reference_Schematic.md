---
title: SF32LB52x(电池) 参考设计原理图
type: reference_design
aliases: ["SF32LB52x_batt_Reference_Schematic","SF32LB52x参考设计","电池系列参考板原理图"]
tags: ["企业MCU","参考设计","SF32LB52x","电池供电系列","原理图"]
sources: [[raw/mcu/ref_design/SF32LB52x_batt/SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]]
mcu_family: ["SF32LB52"]
series_applicability: ["SF32LB52x(电池)"]
mcu_model: ["SF32LB52x家族"]
hardware_version: ["QFN68L","Reference-SCH-V1.0.0"]
created: 2026-08-13
updated: 2026-08-13
---

# SF32LB52x（电池供电）参考设计原理图

> 本页为 **SF32LB52x（电池系列）官方参考设计原理图**的结构化提炼，作为原理图 AI 审图、硬件设计参考的**黄金样板（Golden Reference）**。
> 原始 PDF（只读）：[[raw/mcu/ref_design/SF32LB52x_batt/SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]]
> 文本提取（方案A 矢量解析）：`review_schematic/output/SF32LB52x_batt_ref/schematic_struct_text.txt`
> 配套 3.3V 系列参考设计见 [[SF32LB52X_3V3_Reference_Schematic]]。

## 1. 设计定位与 MCU
- 芯片：**SF32LB52x**（电池系列，QFN68L，Big Core PA00–PA44，**共 44 GPIO（无 PA21，pin24 为电源引脚 VCC）**）。
- **内置 ≤560mA 锂电线性充电器**，支持满电电压 **4.2V~4.45V**；主电 VBAT 3.2~4.7V（单节锂电）。
- 与 3.3V 系列核心差异：**无 PA21、无外部 VDD_SIP 引脚**（片内 VDD18_VOUT 由内部 LDO 输出）；合封存储供电控制改用 **PA11**。

## 2. 电源架构（Golden）
- **输入保护（OVP）**：VBUS 经 OVP 后给系统。选型必要条件：
  - **VBUS 供电范围 4.6V~5.5V**；VBUS 在芯片管脚处须 **≥4.6V**（POGO PIN/走线压降要小）。
  - OVP 器件示例：**ETA7112**（内置 Vin 保护阈值 5.5V，Vout=5.4~5.7V）、**LP5305AQVF**（Vout=5.1V）；P-Ch MOSFET 内阻 **<250mΩ**、响应时间 **<100ns**。
  - 须做 **ESD 与防反接保护**；尽量减小 POGO PIN→芯片 VBUS 走线阻抗（避免压降致 VBUS<4.6V）。
- **电池**：VBAT 到电池焊点走线阻抗尽量小；VBAT 与 VCC 接在一起使用（待机=deepsleep，关机=Hibernate）。
- **电源树（内置 LDO 输出）**：
  - **VSYS_3V3**：**仅能供 MCU 内部使用**，不给外设。
  - **VDD33_VOUT1**：最大电流 **150mA**，推荐给**外部 Flash 和 Sensor** 供电。
  - **VDD33_VOUT2**：最大电流 **150mA**，可单独给**马达**供电。
  - **VSYS_3V3 + VDD33_VOUT1 + VDD33_VOUT2 外挂电容之和 < 9.6µF**。
  - **AVDD_BRF 由 VSYS_3V3 供电**；**AVDD33_AUD 由 VDD33_VOUT1 供电**。
- **VDD18_VOUT（pin23，内部 LDO 输出）**：走线**寄生电容 < 10pF、立体包地处理**；SF32LB520 须焊接 R0106，SF32LB523/5/7 按型号处理。
- **船运/关机模式**：MCU 处于 Hibernate 时，仅 VSYS_3V3 有输出，其他 VBAT 下游器件电源默认关闭。

## 3. 时钟
- **48MHz 主晶振**：负载电容 **8.8pF**，ΔF/F0 ≤ ±20ppm。
- **32.768kHz RTC 晶振（可选）**：CL 7–12pF（推荐 8.8pF），ESR ≤ 80KΩ（推荐 38KΩ），ΔF/F0 ≤ ±10ppm。
- L0100、Y0100、Y0101 为关键物料，须按参数选型。

## 4. 关键 BOM（参考选型）
| 功能 | 参考器件 | 备注 |
|---|---|---|
| OVP | ETA7112 / LP5305AQVF | Vout 5.1~5.7V，P-Ch MOSFET Rds<250mΩ |
| BUCK | L0100（4.7µH 绕线电感） | Isat≥450mA，DCR≤0.4Ω |
| LDO | BL8077CB5TR33 | 低 Iq LDO（LCD/HR/Flash 供电） |
| 音频功放 | AW8155B FCR | Class A/B；开关/电荷泵类远离模拟与射频 |
| G-Sensor | STK8321 | I2C，INT 抬腕唤醒可用 PA33（不用可省） |
| 地磁 | QMC6310 | I2C 0x1C/0x3C |
| 外挂 Flash | W25Q256JVEIQ（WSON8） | 外部 Flash 接口电压须为 3.3V |
| 调试 | PA18/SWDIO、PA19/SWCLK | 默认下载/DEBUG 接口 |

## 5. 设计要点与对应审图规则
### 5.1 外挂存储供电控制（电池系列用 PA11）
- 电池系列**无 PA21**，合封存储供电控制改用 **PA11**（MPI2_VDD_EN/SD_VDD_EN，**默认 PU**，复位/启动早期维持确定电平）。
- **Nor Flash** 待机功耗低，可不加电源控制（常供电）。
- **SPI Nand / SD Nand** 待机功耗高，须由 **PA11 控制 VDD_MEM 电源开关**（见 [[CR_RefDesign_ExternalFlash_Power]]、[[CR_Hibernate_SiP_Supply]]）。
- 外部 Flash 与 eMMC 二选一；eMMC/SD Nand 的 PA13/PA15/PA17 须加 7.5K 上拉（见 [[CR_RefDesign_EMMC_SD_Pullup]]）。

### 5.2 接口电平与 EMI
- 所有外设接口电压**必须匹配 VDDIOA**（见 [[CR_RefDesign_Interface_VoltageMatch]]）。
- **外部 Flash 接口电压必须是 3.3V**。
- LCD FPC 排线 EMI：排线短、远离天线、走内层包地、时钟/数据线预留 RC、Flash 入屏蔽罩（见 [[CR_RefDesign_LCD_FPC_EMI]]）。
- HR 接口电源用 VDD33_VOUT1，LED 电源用 VBAT；LCD 电源须用低 Iq LDO。

### 5.3 调试 / 唤醒 / 其他
- PA18/PA19 复用 DBG_UART，为默认下载/DEBUG/RF 认证接口（见 [[CR_DebugInterface_PA18_PA19]]）。
- PA28–PA34 共 7 个 GPIO 可复用 GPADC，输入范围 0~3.3V。
- 长按复位键高有效 PA34；VBAT 管脚到电池焊点走线阻抗尽量小；4G 唤醒 MCU=PA35，GPS 唤醒=PA27。

## 6. 关联页面
- 芯片实体：[[SF32LB52x_batt]]｜3.3V 系列参考设计：[[SF32LB52X_3V3_Reference_Schematic]]
- 电源/充电：[[SF32LB52_Peripheral_Power]]、[[CR_RefDesign_Batt_OVP_Charger]]、[[CR_RefDesign_Batt_PowerTree]]
- 审图规则库：[[index_MCU_ALL#2-pdf-原理图-ai-审图|校验规则总览]]
