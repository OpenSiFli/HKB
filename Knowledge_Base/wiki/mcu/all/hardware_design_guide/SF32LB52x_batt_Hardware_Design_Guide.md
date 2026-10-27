---
mcu_family: ["SF32LB52"]
mcu_series: ["电池供电系列"]
doc_type: hardware_design_guide
title: SF32LB52x 硬件设计指南（电池供电）
source_url: "https://wiki.sifli.com/hardware/SF32LB520-3-5-7-HW-Application.html"
sources:
  - "[[SF32LB52x_Datasheet_V2.5.5]]"
  - "[[SF32LB52X_UserManual_V0.8.8]]"
  - "SF32LB52x_batt_HW_Application.html"
images_dir: "raw/mcu/all_chip/hw_design/images/"
---

# SF32LB52x 硬件设计指南（电池供电）

> 原文：<https://wiki.sifli.com/hardware/SF32LB520-3-5-7-HW-Application.html>
> 原始 HTML 备份：`SF32LB52x_batt_HW_Application.html`（raw/mcu/all_chip/hw_design/）
> 适用芯片：**SF32LB52x 系列（小写 x = 电池供电）**，后缀 0 / 3 / 5 / 7，锂电池供电支持 USB 充电，供电电压 **3.2~4.7V**。
> 3.3V 系列（后缀 B/E/G/J/H）请见 [[SF32LB52X_Hardware_Design_Guide]]。

## 1. 基本介绍

帮助开发人员完成基于 SF32LB52x 系列芯片的手表方案开发，重点介绍硬件设计注意事项。

- 芯片特性：超低功耗 AIoT 高性能 MCU，Arm Cortex-M33 STAR-MC1 大小核，图形引擎、NN 加速器、双模蓝牙 5.3、音频 CODEC。
- 外设资源：**44× GPIO**（无 PA21）、3× UART、4× I2C、2× GPTIM、2× SPI、1× I2S、1× SDIO、1× PDM、差分模拟音频输出、单端模拟音频输入、SPI/JDI 显示接口等。
- 具体型号：SF32LB520U36（合封 1MB QSPI-NOR Flash）、SF32LB523UB6（合封 4MB OPI-PSRAM）、SF32LB525UC6（合封 8MB OPI-PSRAM）、SF32LB527UD6（合封 16MB OPI-PSRAM）。

> 📌 引脚差异要点（已与用户确认）：电池系列 **无 PA21**，pin24 = VCC（电源引脚），**共 44 个 GPIO**；3.3V 系列有 PA21、共 45 个 GPIO。详见 [[SF32LB52_Pinmux]]。

## 2. 封装

| 项目 | 参数 |
|---|---|
| 封装 | QFN68L |
| 尺寸 | 7 × 7 × 0.85 mm |
| 引脚间距 | 0.35 mm |

![[raw/mcu/all_chip/hw_design/images/sf32lb52x-A-package-layout.png]]

## 3. 典型应用方案

典型运动手表框图：显示、存储、传感器、震动马达、音频输入输出。

![[raw/mcu/all_chip/hw_design/images/sf32lb52x-A-watch-app-diagram-52x.png]]

> 备注：大小核架构、片内充电 PMU；QSPI TFT/AMOLED 最高 512×512；PWM 背光；外挂 Flash；双模蓝牙 5.3；传感器接口；UART 调试；OTA。

## 4. 原理图设计指导

### 4.1 电源

**处理器供电要求（表 4-1 摘要）**

| 引脚 | 电压/说明 | 最大电流 |
|---|---|---|
| VBUS | 4.6~5.5V（USB 充电输入） | 500 mA |
| VBAT | 3.2~4.7V（锂电池） | 500 mA |
| VCC | 3.2~4.7V | — |
| VSYS | 3.3V（片内电源系统） | — |
| BUCK_LX / BUCK_FB | 1.25V | — |
| VDD_VOUT1 / VDD_VOUT2 | 内部 LDO 输出（默认无输出，需软件开启） | 150 mA |
| VDD_RET / VDD_RTC | retention / RTC 域 | — |
| VDD18_VOUT | 1.8V（依型号外供或内供） | — |
| VDD33_VOUT1 / VDD33_VOUT2 | 3.3V LDO（默认无输出，需软件开启） | — |
| AVDD33_AUD | 音频模拟（仅由 VDD33_VOUT1 供） | 50 mA |
| AVDD_BRF | 射频模拟 | 100 mA |
| MIC_BIAS | 麦克风偏置 | — |

> 备注：VCC 锂电池低压 3.48V，恒压推荐 3.8V；VDD18_VOUT 依型号外供或内供；VDD33_VOUT1/2 默认无输出，需软件配置。

**BUCK 电感选择要求**：L = 4.7µH ±20%，DCR ≤ 0.4Ω，Isat ≥ 450mA。

**电池及充电控制**

- 外部充电管理芯片方案（不带 / 带 PPM 两种）：

![[raw/mcu/all_chip/hw_design/images/sf32lb52x-CHG-NPPM.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52x-CHG-PPM.png]]

- VBAT 内部 GPADC 测压精度 ±30mV。
- 片内集成充电管理模块：

![[raw/mcu/all_chip/hw_design/images/sf32lb52x-CHG-INNER.png]]

  低电关机后须充至开机电压才启动。

- 片内充电时 OVP 芯片选型：VBUS 输入 4.5~5.5V，可选 **AW32905FCR**（OVLO 调 5.2~5.5V，R1/R2 ≤ 1% 误差）、**SGM4064YDE8G / LP5305AQVF**（Regulator 输出 4.5~5.4V）。

![[raw/mcu/all_chip/hw_design/images/sf32lb52x-OVP-SET.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52x-OVP-OVLO.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52x-OVP-REGU.png]]

**内部充电及 LDO 注意事项**
- VBUS 4.6~5.5V，VCC 3.2~4.7V；
- 涓流 56mA@3.0V 转恒流；恒流默认 65mA（可调 5~560mA）；满压 4.2V（最高 4.45V）；复充 -0.15V；VBUS 供 ≥ 350mA；路径阻抗勿过大；
- LDO 输出电容和 ≤ 9.6µF；AVDD33_AUD 只用 VDD33_VOUT1；LCD 不外供内 LDO。

**电源框图**：

![[raw/mcu/all_chip/hw_design/images/sf32lb52x-PWR-diagram.png]]

**如何降低待机功耗**：用负载开关动态管理模块；VDD33_VOUT2 → Motor，VDD33_VOUT1 → Flash/Sensor，LCD 外 LDO；GPIO 默认上下拉关闭；选用小 Iq / Istb 器件。

### 4.2 处理器工作模式及唤醒源

CPU Mode Table（表 4-4）：Active / Sleep / DeepSleep / Standby / Hibernate 五种模式。

Interrupt wake up source（表 4-5）：15 个唤醒中断源 —— LWKUP_PIN0~3 对应 PA24~27；PIN10~20 对应 PA34~44。

### 4.3 时钟

| 晶体 | 负载电容 CL | ESR | 推荐值 |
|---|---|---|---|
| 48MHz | 7~12pF（荐 8.8pF） | ≤30Ω | ±10ppm |
| 32.768KHz | ≤12.5pF（荐 7pF） | ≤80kΩ | ±20ppm |

晶体下挖二层 GND 减小寄生电容。推荐晶体：48MHz Hosonic E1SB48E001G00E / TKD SX20Y048000B31T-8.8；32.768KHz Hosonic ETST00327000LE / TKD SF32K32768D71T01。

详细的物料认证信息（含晶体、Buck 电感、Nor/SPI Nand/SD Nand Flash、LCD 驱动等全系列认证料号），请参考：
[[SIFLI_MCU_AVL_V0.4_20260812|SIFLI-MCU-AVL-认证表]]

### 4.4 射频

50Ω 阻抗，预留 π 型匹配网络。

![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-rf-diagram.png]]

### 4.5 显示 / 存储 / 按键 / 音频（与 3.3V 系列共用引脚定义）

> 显示、存储、按键、音频、UART/I2C/GPTIM、调试下载、产线烧录等章节的**引脚分配与本系列一致**（两系列共用 PA00–PA44 复用矩阵，仅 PA21 不同 —— 本系列无 PA21）。详细信号表（SPI/QSPI、JDI、触摸背光、SPI NOR/NAND、SD NAND/eMMC、Bootstrap、调试 UART PA18/PA19 等）见 [[SF32LB52X_Hardware_Design_Guide]] 第 4.5~4.13 节与 [[SF32LB52_Pinmux]]。

**⚠️ 与已确认事实不符之处（已修正）**：原电池指南"启动存储介质电源控制"写为"PA21 控电源开关（高开低关）"。但**电池系列无 PA21（共 44 GPIO，pin24=VCC）**，该描述沿用了 3.3V 指南文案。本系列合封存储电源控制**不可用 PA21**，须以其他可控 GPIO 或常开方式实现；hibernate 防漏电规则（[[CR_Hibernate_SiP_Supply]]、[[FC_Hibernate_SiP_Leakage]]）**不适用于电池系列**。

**开关机按键**：PA34 长按复位（默认硬件功能，长按 10s 强制复位，不受软件控制；软件可配长按时长）。

![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PWKEY.png]]

**机械旋钮按键**：

![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-XNKEY.png]]

**振动马达**（电池系列图）：

![[raw/mcu/all_chip/hw_design/images/sf32lb52x-A-VIB.png]]

**音频接口**：MIC_BIAS / ADCP（单端输入）/ DACP·DACN（差分输出）。MIC 隔直 ≥ 2.2µF，DAC 差分走线 < 10pF / < 2cm。

![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-MEMS-MIC.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-ECM-MIC.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-DAC-PA.png]]

**启动设置（表 4-14 Bootstrap）**：PA13 = BS1，PA17 = BS0（注意：电池系列图文件为 `SF32LB52x-A-Bootstrap.png`，与 3.3V 的 `sf32lb52X-B-Bootstrap.png` 不同）。

![[raw/mcu/all_chip/hw_design/images/SF32LB52x-A-Bootstrap.png]]

### 4.6 调试和下载接口

| 信号 | 引脚 |
|---|---|
| DBG_UART_RXD | PA18 |
| DBG_UART_TXD | PA19 |

> PA18/PA19 = USART1_RXD/TXD（Debug UART）由 ROM 软件在启动阶段设置，非硬件 default 复用（以 [[SF32LB52_Pinmux]] 表为准）。

## 5. PCB 设计指导

### 5.1 封装设计（与 3.3V 共用尺寸图）

![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-QFN68L-POD.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-QFN68L-SHAPE.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-QFN68L-REF.png]]

### 5.2 叠层 / 通用规则 / 扇出

![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-STACK.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-RULE.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-FANOUT.png]]

### 5.3 时钟 / 射频 / 音频 / USB / SDIO / DCDC 走线（与 3.3V 共用）

> 以下 PCB 走线章节两系列完全一致，图片共用（均以 `sf32lb52X-B-*` 命名）。完整图集见 [[SF32LB52X_Hardware_Design_Guide]] 第 5.4~5.10 节。

![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-CRYSTAL.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-SCH-RF.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-RF.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-AUDIO-PWR.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-SCH-USB.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-USB.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-SCH-SDIO.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-SDIO.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-SCH-DCDC.png]]
![[raw/mcu/all_chip/hw_design/images/sf32lb52X-B-PCB-DCDC.png]]

### 5.4 电源供电走线（VCC）

VCC 线宽 ≥ 0.4mm。

![[raw/mcu/all_chip/hw_design/images/sf32LB52x-A-SCH-VCC.png]]
![[raw/mcu/all_chip/hw_design/images/sf32LB52x-A-PCB-VCC.png]]

### 5.5 充电电路走线（电池专属）

VBUS / VBAT 线宽 ≥ 0.4mm，星型走线、不并行。

![[raw/mcu/all_chip/hw_design/images/sf32LB52x-A-SCH-CHG.png]]
![[raw/mcu/all_chip/hw_design/images/sf32LB52x-A-PCB-CHG.png]]

### 5.6 其它（TVS / EMI&ESD）

USB/电池座 TVS 前测试点，先过 TVS。

![[raw/mcu/all_chip/hw_design/images/sf32LB52x-A-SCH-PMU-TVS.png]]
![[raw/mcu/all_chip/hw_design/images/sf32LB52x-A-SCH-PMU-EOS.png]]

## 6. 相关文档

- 芯片技术规格书：[[SF32LB52x_Datasheet_V2.5.5]]
- 用户手册：[[SF32LB52X_UserManual_V0.8.8]]
- 引脚复用矩阵：[[SF32LB52_Pinmux]]
- 3.3V 系列硬件设计指南：[[SF32LB52X_Hardware_Design_Guide]]

## 7. 修订历史

| 版本 | 日期 | 说明 |
|---|---|---|
| v0.0.1 | 2024-10 | 初始版本 |
