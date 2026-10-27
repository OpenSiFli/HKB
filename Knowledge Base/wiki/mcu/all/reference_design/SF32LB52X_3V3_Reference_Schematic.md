---
title: SF32LB52X(3.3V) 参考设计原理图
type: reference_design
aliases: ["SF32LB52X_3V3_Reference_Schematic","SF32LB52X参考设计","3.3V参考板原理图"]
tags: ["企业MCU","参考设计","SF32LB52X","3.3V供电系列","原理图"]
sources: [[raw/mcu/ref_design/SF32LB52X_3V3/SF32LB52X_3V3-Reference-SCH-V1.0.0_20251015.pdf]]
mcu_family: ["SF32LB52"]
series_applicability: ["SF32LB52X(3.3V)"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","Reference-SCH-V1.0.0"]
created: 2026-08-13
updated: 2026-08-13
---

# SF32LB52X（3.3V 供电）参考设计原理图

> 本页为 **SF32LB52X（3.3V 系列）官方参考设计原理图**的结构化提炼，作为原理图 AI 审图、硬件设计参考的**黄金样板（Golden Reference）**。
> 原始 PDF（只读）：[[raw/mcu/ref_design/SF32LB52X_3V3/SF32LB52X_3V3-Reference-SCH-V1.0.0_20251015.pdf]]
> 文本提取（方案A 矢量解析）：`review_schematic/output/SF32LB52X_3V3_ref/schematic_struct_text.txt`
> 配套电池系列参考设计见 [[SF32LB52x_batt_Reference_Schematic]]。

## 1. 设计定位与 MCU
- 芯片：**SF32LB52X**（3.3V 系列，QFN68L，Big Core PA00–PA44，共 **45 GPIO（含 PA21）**）。
- 供电形态：外部 5V（USB Type-C）→ BUCK/LDO 产生 3.3V/1.8V；**无内置充电器**（锂电充电器仅电池系列 SF32LB52x 才有）。
- 应用：可穿戴 / 便携 AIoT 参考板，含 LCD、Nor/SPI Nand/SD Nand Flash、G-Sensor、地磁、硅麦/ECM MIC、音频功放、GPS/4G 接口、USB Type-C。

## 2. 电源架构（Golden）
- **输入**：USB_VBUS_5V（Type-C 16P）→ 经 BUCK **TLV62569DBVR**（3.3V / 2A）得到 VDD_3V3；经 LDO **BL8077CB5TR33** 得到 VDD_1V8。
- **PVDD（核心逻辑供电，随型号变）**：
  - SF32LB52**DUB6** → PVDD = **1.8V**
  - SF32LB52**BU36 / BU56 / E / G / JUX6** → PVDD = **3.3V**
- **VDD_SIP（合封存储外部供电，pin23）**：
  - BU36 / BU56：需**外供 3.3V**
  - DUB6：需**外供 1.8V**
  - E / G / JUX6：不外加电源，仅外接去耦电容
  - 走线要求：**寄生电容 < 10pF，立体包地处理**；支持 Hibernate 关机时须由 **PA21** 控制其电源开关（否则可常供电）。
- **VDDIOA**：支持 1.8V 与 3.3V，所有外设接口电平须与其一致。
- **去耦**：每路电源按推荐容值加去耦（4.7µF/6.3V、1µF/6.3V、0.1µF 等，详见 PDF）。

## 3. 时钟
- **48MHz 主晶振**：负载电容 **8.8pF**，频偏 ΔF/F0 ≤ **±20ppm**（石英需焊负载电容；陶瓷谐振器可 DNP）。
- **32.768kHz RTC 晶振（可选）**：负载电容 CL 7–12pF（推荐 8.8pF），等效串联电阻 ESR ≤ 80KΩ（推荐 38KΩ），频偏 ΔF/F0 ≤ **±10ppm**。
- 晶振紧靠芯片、走线短且包地。

## 4. 关键 BOM（参考选型）
| 功能 | 参考器件 | 备注 |
|---|---|---|
| BUCK | TLV62569DBVR | 3.3V/2A，配 2.2µH/3.8A 电感 L0104 |
| LDO 3.3V | BL8077CB5TR33 | VDD_3V3 支线（传感器/Flash） |
| 音频功放 | AW8155B FCR | 推荐 Class A/B；开关/电荷泵类远离模拟与射频 |
| G-Sensor | STK8321 | I2C，PA39/PA40；INT 抬腕唤醒可用 PA33 |
| 地磁 | QMC6310 | I2C 0x1C/0x3C，PA28/PA29；EN=PA31 |
| 硅麦 | WMM7037ATEN03 / MEMS | 单端硅麦时 R0187 贴 0Ω |
| 外挂 Nor Flash | PY25Q128HA-WXH-IR（WSON8） | 示例；SPI 接口 |
| USB | Type-C 16P CB0810 | USB_VBUS_5V 输入 |
| 调试 | PA18/SWDIO、PA19/SWCLK（SWD）；PA18/PA19 兼 DBG_UART | 默认下载/DEBUG/RF 认证接口 |

## 5. 设计要点与对应审图规则
### 5.1 外挂存储供电控制
- SiP/合封 Flash（VDD_SIP）：3.3V 系列由 **PA21** 控制电源开关；Hibernate 关机**必须**用 PA21 断电，否则可常供电（见 [[CR_Hibernate_SiP_Supply]]、[[CR_RefDesign_ExternalFlash_Power]]）。
- 外挂 SPI Nand / SD Nand（VDD_MEM）：由 **PA11**（MPI2_VDD_EN/SD_VDD_EN，默认 PU）控制电源开关（见 [[CR_RefDesign_ExternalFlash_Power]]）。
- **Nor Flash 容量判定**：MPI 外接 **≥32MB** Nor 时供电须用 PA21 可控断电；**≤16MB** Nor 自身可 Deep Power Down（≈1µA），**可常供电**。
- 双 Nor 方案：Flash1 CS=PA12，Flash2 CS=PA26，CLK 与 D0–D3 共用。
- 外部 Flash 与 eMMC **二选一**。

### 5.2 接口电平与 EMI
- 所有外设接口电压**必须匹配 VDDIOA**（见 [[CR_RefDesign_Interface_VoltageMatch]]）。
- eMMC / SD Nand：PA13(SD_D3)、PA15(SD_CMD)、PA17(SD_D1) 均须加 **7.5K 上拉**（R0101/R0160/R0102）；eMMC 接口电压须匹配 VDDIOA（见 [[CR_RefDesign_EMMC_SD_Pullup]]）。
- LCD：FPC 排线是最主要 EMI 源——排线尽量短、远离射频天线；芯片到接插件走线走 PCB 内层并上下包地；时钟/数据线预留 RC 滤高阶谐波；Flash 芯片放屏蔽罩内（见 [[CR_RefDesign_LCD_FPC_EMI]]）。
- 4G/GPS 模块电平=3.3V 时，**PA_26_LS_EN 不需要**；电平转换 IC 使能由 PA_09_LH_EN 控制。

### 5.3 调试 / 唤醒 / 其他
- PA18/PA19 复用 DBG_UART，为默认下载/DEBUG/RF 认证接口（见 [[CR_DebugInterface_PA18_PA19]]）。
- PA28–PA34 共 7 个 GPIO 可复用 GPADC，输入范围 **0~3.3V**（见 [[CR_GPADC_SourceResistance]]）。
- 长按复位键高有效，PA34 支持唤醒 MCU；按键在子板时 10K 下拉 R0174 须在主板上。
- 原理图库 WKUP 均指 standby/Hibernate 唤醒；PA25/26/27/33/38 为预留信号，可按需接外设。

## 6. 关联页面
- 芯片实体：[[SF32LB52X]]｜电池系列参考设计：[[SF32LB52x_batt_Reference_Schematic]]
- 电源/时钟/存储外设：[[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_Clock]]、[[SF32LB52_Peripheral_Memory]]
- 审图规则库：[[index_MCU_ALL#2-pdf-原理图-ai-审图|校验规则总览]]
