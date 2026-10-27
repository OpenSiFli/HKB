---
title: SF32LB52 外设-GPIO
type: mcu_periph
aliases: ["SF32LB52 GPIO","SF32LB52 通用输入输出"]
tags: ["企业MCU","外设模块-GPIO","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_Datasheet_V2.5.5],[SF32LB52x_Datasheet_V0.2.6],[SF32LB52X_UserManual_V0.8.8]]
mcu_family: ["SF32LB52"]
mcu_model: ["SF32LB52x(电池)","SF32LB52X(3.3V)"]
series_applicability: ["通用-两系列共用"]
hardware_version: ["QFN68L"]
created: 2026-08-10
updated: 2026-08-12
---

## 摘要
SF32LB52 家族（3.3V 系列 SF32LB52X 与电池系列 SF32LB52x）GPIO：3.3V 系列 SF32LB52X 最多 45 个 GPIO（Big Core 域 PA00–PA44，含 PA21），电池系列 SF32LB52x **无 PA21、共 44 个 GPIO**（pin24 在本系列为电源引脚 VCC，不作 PA21）。PA 信号引脚与复用矩阵两系列**基本一致，唯一差异即 PA21（仅 3.3V 系列有）**；两系列**其余差异在电源专用引脚（含 GPIO 供电域）**，见下方「系列电源引脚差异」与 [[SF32LB52_Peripheral_Power]]。

> **适用系列**：本外设为 SF32LB52X（3.3V 供电）与 SF32LB52x（电池供电）两系列共用；外设逻辑一致，差异仅在电源架构与电源专用引脚（见 [[SF32LB52_Peripheral_Power]]、本页「系列电源引脚差异」）。

## 核心硬件内容
### 1. 工作机制
- 共 45 GPIO（PA00–PA44，含 PA21），均为 I/O 可复用；复用选择器 Sel#：0=GPIO，1~8 为各外设复用组。（注：电池系列 SF32LB52x 无 PA21，共 44 GPIO，见「PA00–PA44 引脚复用矩阵」说明）
- 输入支持电平/边沿（上/下/双沿）中断触发；输出值经寄存器配置。
- 部分引脚兼作唤醒源（WKUP_PIN0~20，见 PA24~PA44 部分引脚）。

### 2. 系列电源引脚差异（重要）
两系列 PA 信号引脚基本相同（**唯一差异为 PA21：仅 3.3V 系列 SF32LB52X 有 PA21（pin24）；电池系列 SF32LB52x pin24 为电源引脚 VCC，无 PA21**），且 **GPIO 供电域引脚不同**：
- **3.3V 系列 SF32LB52X**：GPIO 由外部 **VDDIOA（引脚 21）** 供电，范围 1.8/3.3V，IO 电平跟随 VDDIOA。
- **电池系列 SF32LB52x**：引脚 21 为 **VBUS（充电输入）**，**外部无独立 VDDIOA 引脚**；片内 VDDIOA 在芯片内部直接连到 **VSYS** 引脚，GPIO IO 域由 VSYS 经内部 VDDIOA 供电（IO 电平跟随 VSYS≈3.3V）。已确认，无需再核对 UM5201。

### 3. 标准电路要求
- **内部上/下拉**：7~20kΩ（@3.3V）/ 10~30kΩ（@1.8V），可由寄存器使能；外部上下拉电阻选型须与之协调。
- **驱动能力（DS5202 V0.2.6 文本，测试条件 VOH=0.8×VDDIO）**：@3.3V 最大 38mA（min 12 / typ 30）；@1.8V 最大 13mA（6/10/13）。
- **驱动能力（DS5201 V2.5.5 Table 4-19 四档，测试条件 VOH=0.9×VDDIO）**：由 DS1/DS0 选择 **2 / 4 / 8 / 12 mA**（覆盖全部 GPIO）。
- **两系列 IO 驱动能力完全相同**：上述两组数值是**同一驱动电路**在两种不同输出高电平测试条件（VOH=0.8×VDDIO 与 VOH=0.9×VDDIO）下测得的结果，并非两种不同能力。设计取电与 DS1/DS0 配置按目标 VOH 要求选择即可。

### 4. 约束禁忌
- **低功耗浮空禁忌（重要）**：使能输入功能的数字 IO 若悬空，低功耗场景下漏电流/功耗会升高 → 必须配置确定电平（接他芯确定输出或外部上/下拉电阻）。【依据 Table 5-1 注释，P39】
- 复用功能切换须通过 PINMUX 配置，避免与其他外设引脚冲突。
- 用作 GPADC 输入的引脚（PA28~PA34 = CH0~CH6）禁止施加超过模拟输入范围的电压。

### 5. 规范依据
- Datasheet §3.5.1 GPIO（P15）、Table 5-1 Pin Types（P39）、Table 5-2 GPIO(PA) Pin List（P40–P46 / 电池版 P41–P47）、Table 4-3/4-4 I/O 特性（P29–P30）

## PA00–PA44 引脚复用矩阵（3.3V 系列 SF32LB52X；电池系列 SF32LB52x 无 PA21、共 44 GPIO）

> 📌 **完整 PINMUX 复用矩阵**（含 LPSYS 小核 PB00–PB03、SIP Group A 内部 PAD 说明、通用分配组 I2C_UART/TIM 类型、以及**与规格书 Table 5-2 的差异清单**）见 [[SF32LB52_Pinmux]]。PINMUX 表为本家族引脚复用的**权威依据**。
| 引脚号 | 名称 | 关键复用 |
|------|------|----------|
| 51 | PA00 | GPIO_A0 / LCDC1_SPI_RSTB / PA_I2C_UART / PA_TIM / LCDC1_8080_RSTB |
| 50 | PA01 | GPIO_A1 / PA_I2C_UART / PA_TIM |
| 49 | PA02 | GPIO_A2 / LCDC1_SPI_TE / I2S1_MCLK / LCDC1_JDI_B2 / 8080_TE |
| 48 | PA03 | GPIO_A3 / LCDC1_SPI_CS / I2S1_SDO / LCDC1_JDI_B1 / 8080_CS |
| 47 | PA04 | GPIO_A4 / LCDC1_SPI_CLK / I2S1_SDI / LCDC1_JDI_G1 / 8080_WR |
| 46 | PA05 | GPIO_A5 / LCDC1_SPI_DIO0 / I2S1_BCK / LCDC1_JDI_R1 / 8080_RD |
| 45 | PA06 | GPIO_A6 / LCDC1_SPI_DIO1 / I2S1_LRCK / LCDC1_JDI_HST / 8080_DC |
| 44 | PA07 | GPIO_A7 / LCDC1_SPI_DIO2 / PDM1_CLK / LCDC1_JDI_ENB / 8080_DIO0 |
| 43 | PA08 | GPIO_A8 / LCDC1_SPI_DIO3 / PDM1_DATA / LCDC1_JDI_VST / 8080_DIO1 |
| 42 | PA09 | GPIO_A9 / PA_I2C_UART / PA_TIM |
| 35 | PA10 | GPIO_A10 / PA_I2C_UART / PA_TIM |
| 34 | PA11 | GPIO_A11 / PA_I2C_UART / PA_TIM |
| 33 | PA12 | GPIO_A12 / MPI2_CS / SD1_DIO2 / PA_I2C_UART / PA_TIM |
| 32 | PA13 | GPIO_A13 / MPI2_DIO1 / SD1_DIO3 |
| 31 | PA14 | GPIO_A14 / MPI2_DIO2 / SD1_CLK |
| 30 | PA15 | GPIO_A15 / MPI2_DIO0 / SD1_CMD |
| 29 | PA16 | GPIO_A16 / MPI2_CLK / SD1_DIO0 |
| 28 | PA17 | GPIO_A17 / MPI2_DIO3 / SD1_DIO1 |
| 27 | PA18 | GPIO_A18 / **SWDIO** |
| 26 | PA19 | GPIO_A19 / **SWCLK** |
| 25 | PA20 | GPIO_A20 |
| 24 | PA21 | GPIO_A21（**外挂 Flash 存储电源控制**，主要用途：驱动外部电源开关使能；Nor Flash 可常供电不必断电，SPI Nand/SD Nand 须控供电）｜**仅 3.3V 系列 SF32LB52X**；电池系列 pin24 为电源引脚 VCC，无 PA21，外挂存储供电改用默认 PU 的 GPIO |
| 11 | PA22 | GPIO_A22 / PDM1_CLK / **XTAL32K_XI** |
| 10 | PA23 | GPIO_A23 / PDM1_DATA / **XTAL32K_XO** |
| 9  | PA24 | GPIO_A24 / SPI1_DIO / I2S1_MCLK / WKUP_PIN0（deepsleep 可翻转保留组） |
| 8  | PA25 | GPIO_A25 / SPI1_DI / I2S1_SDO / XTAL32K_EXT / WKUP_PIN1 |
| 7  | PA26 | GPIO_A26 / WKUP_PIN2 |
| 6  | PA27 | GPIO_A27 / WKUP_PIN3 |
| 5  | PA28 | GPIO_A28 / SPI1_CLK / I2S1_SDI / **GPADC_CH0** |
| 4  | PA29 | GPIO_A29 / SPI1_CS / I2S1_BCK / **GPADC_CH1** |
| 3  | PA30 | GPIO_A30 / EFUSE_PWR / I2S1_LRCK / **GPADC_CH2** |
| 2  | PA31 | GPIO_A31 / **GPADC_CH3** |
| 1  | PA32 | GPIO_A32 / **GPADC_CH4** |
| 67 | PA33 | GPIO_A33 / **GPADC_CH5** / WKUP_PIN10 |
| 66 | PA34 | GPIO_A34 / **GPADC_CH6** / WKUP_PIN11 / **PWRKEY 复位（默认持续高>10s；PWRKEY_CNT 可配至 ~100+s，作 GPIO 见 [[DR_PA34_PowerKey_GPIO]]）** |
| 65 | PA35 | GPIO_A35 / **USB11_DP** / WKUP_PIN12 |
| 64 | PA36 | GPIO_A36 / **USB11_DM** / WKUP_PIN13 |
| 63 | PA37 | GPIO_A37 / SPI2_DIO / LCDC1_8080_DIO2 / WKUP_PIN13 |
| 62 | PA38 | GPIO_A38 / SPI2_DI / WKUP_PIN14 |
| 61 | PA39 | GPIO_A39 / SPI2_CLK / LCDC1_JDI_VCK / 8080_DIO3 / WKUP_PIN15 |
| 60 | PA40 | GPIO_A40 / SPI2_CS / LCDC1_JDI_XRST / 8080_DIO4 / WKUP_PIN16 |
| 59 | PA41 | GPIO_A41 / LCDC1_JDI_HCK / 8080_DIO5 / WKUP_PIN17 |
| 58 | PA42 | GPIO_A42 / LCDC1_JDI_R2 / 8080_DIO6 / WKUP_PIN18 |
| 57 | PA43 | GPIO_A43 / LCDC1_JDI_G2 / 8080_DIO7 / WKUP_PIN19 |
| 56 | PA44 | GPIO_A44 / WKUP_PIN20 |

> 复用选择器 Sel#：0=GPIO；1~8 为 LCDC1/I2S/PDM/SPI/PA_I2C_UART/PA_TIM/USB/ADC/WKUP 等复用组。当某 PA 映射为 PA_I2C_UART 时，具体作为哪个 I2C/USART 还需在 HPSYS_CFG 指定（如 PA07 作 USART2_TXD：PAD_PA07_FSEL=4 + USART2_PINR_TXD_PIN=7）；多个接口信号指定到同一 IO 会引起功能错误。完整复用矩阵（含小核 LPSYS、SIP Group A、与规格书差异）以 [[SF32LB52_Pinmux]] 为准（PINMUX 表权威，优于 datasheet Table 5-2）。

## 用户手册 V0.8.8 补充（默认上下拉 / 高阻 / 中断）
来源：[[SF32LB52X_UserManual_V0.8.8]] §5（P64–P68）。

### 默认上下拉（表 5-1，上电 PE 默认=1）
- 上电后 IO 默认存在上拉或下拉（PE=1），需软件配置为所需状态。
- 部分引脚默认态：PA03=PU、PA11=PU、PA12=PU、PA18=**PU（SWDIO）**、PA19=**No Pull（SWCLK）**；其余多为 PD（PA00/01/02/04/05/06/07/08/09/10/13/14/15/16/17 等）。
- PA 映射为 PA_I2C_UART 时，具体作为哪个 I2C/USART 还需在 HPSYS_CFG 指定；多个接口信号指定到同一 IO 会引起功能错误。

### 高阻与开漏
- 配置高阻：PE=0 + IO 设为 GPIO 功能 + GPIO 输出使能关闭。
- 开漏输出：使能内部上拉(PE=1,PS=1) 或外部上拉；开漏 0=OE=1,O=0；开漏 1=OE=0。

### 中断
- 无论 IO 映射何种功能均可产生 GPIO 中断；中断使能应仅在需要时开启，不用时须关闭以免误触发。
- 中断条件由 IPH/IPL/ITR 配置（高/低电平、上升/下降/双沿）；GPIO 中断可唤醒低功耗。

### 低功耗 IO
- deepsleep/standby 下除 **PA24~PA27** 外的输出 IO 不可翻转（保持进入前电平）；hibernate 下 IO 高阻（唤醒 PIN 可保持上下拉，配置在 RTC 寄存器）。

> 详见 [[DR_GPIO_DefaultPUPD_HighZ]]、[[CR_GPIO_Default_PUPD]]、[[DR_LowPower_IO_Retention]]。

## 关联页面
- 电池系列实体：[[SF32LB52x_batt|SF32LB52x]]｜3.3V 系列实体：[[SF32LB52X]]｜家族总览：[[SF32LB52]]
- 电源：[[SF32LB52_Peripheral_Power]]｜时钟：[[SF32LB52_Peripheral_Clock]]｜GPADC：[[SF32LB52_Peripheral_GPADC]]
- 校验规则：[[CR_FloatingIO_LowPower]]、[[CR_AbsMaxRatings]]、[[CR_Reset_Levels]]

## 原始来源完整引用
1. [DS5201-SF32LB52x-Datasheet V2p5p5.pdf]，Raw：raw/mcu/all_chip/datasheets/DS5201-SF32LB52x-Datasheet V2p5p5.pdf，Table 5-2 GPIO(PA) Pin List（P41–P47）、Table 4-19 IO Drive Strength（P38）
2. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/DS5202-SF32LB52X-Datasheet V0p2p6.pdf，Table 5-2（P40–P46）、Table 4-3/4-4（P29–P30）
3. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，§5 GPIO（P64–P68）

## 待核实问题
- 电池系列 GPIO IO 域由内部 VDDIOA→VSYS 供电、外部无 VDDIOA 引脚（已确认，见上方「系列电源引脚差异」）。
- 各 GPIO 在复位后的默认状态（上电默认输入/输出/高阻）datasheet 文本未逐引脚列出，待核实或参考参考设计。
- PA 复用矩阵两系列差异已确认：**仅 PA21 不同**——PA21 仅存在于 3.3V 系列 SF32LB52X（pin24），电池系列 SF32LB52x pin24 为电源引脚 VCC、无 PA21；故 3.3V 系列共 45 GPIO、电池系列共 44 GPIO。其余 PA00–PA44（除 PA21 外）两系列完全一致。
