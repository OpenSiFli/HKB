---
title: SF32LB57 引脚复用矩阵（Pinmux）
type: mcu_pinmux
aliases: ["SF32LB57_Pinmux","SF32LB57 引脚复用","SF32LB57 pinmux"]
tags: ["企业MCU","引脚复用/Pinmux","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["pinmux_202600901","QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

# SF32LB57 家族 PINMUX（引脚复用矩阵）

> **权威来源**：`pinmux - 202600901.xlsx`（已归档 `raw/mcu/all_chip/pinmux/`）。
> **规则**：PINMUX 相关内容**以此表格为准**；规格书（DS5702 3.3V / DS5701 电池）Table 5-2/5-4 若与下表有差异，原则上以本表为准，差异在文末「与规格书差异」一节标注。
> **系列适用性**：本表覆盖 GPIO Group A（PA00–PA57），**电池供电系列（SF32LB57x）与 3.3V 供电系列（SF32LB57X）共用同一套大核 GPIO 复用矩阵**；两系列差异仅在于专用电源/模拟管脚（见 [[SF32LB57_Peripheral_Power]] §1），不涉及 GPIO Group A 的复用分配。

## 1. 工作表（Sheet）结构与含义

| 工作表 | 含义 | 是否入库 |
|---|---|---|
| **HPSYS** | 大核（HCPU / Big Core）GPIO 复用矩阵（GPIO Group A，PA00–PA57） | ✅ 入库（见第 3 节） |
| **matrix index** | 矩阵交叉开关信号总表（160 个可路由信号，idx 16–175） | ✅ 入库（见第 4 节） |
| **lcdc mux** | LCD 控制器接口复用（IF_SEL 0–3：SPI/JDI/EPD/DBI/DPI） | ✅ 入库（见第 5 节） |
| **lcdc dpi inner mux** | DPI 内部 RGB 位宽复用（mode 0–7） | ✅ 入库（见第 5 节） |
| **simplified** | 精简视图（PAD + PUPD + Func 0/1/2/3/4/5/6/15） | 仅对照，不另列表（内容与 HPSYS 一致） |

> ⚠️ **本文件 pinmux xlsx 仅含 HPSYS（大核 GPIO Group A）**，未含 LPSYS（小核 GPIO）/ PBR（电源 RF 控制）工作表（SF32LB52 家族 pinmux 含 LPSYS/PBR，57 家族本表未提供，见「与规格书差异」第 3 条）。

## 2. PINMUX 类型说明（命名规则）

- **所有 PAxx 默认功能 = `GPIO_Ax`（Func0）**：未做复用配置时即为通用 GPIO。
- **`MATRIX_DIOx`（Func16，每个 PA 均有）**：矩阵交叉开关输出。SF32LB57 采用**灵活矩阵（matrix）架构**——任一矩阵信号（见第 4 节：I2C/UART/TIM/PWM/… 共 160 个）均可经 `MATRIX_DIOx` 路由到**任意 PA 引脚**，替代 SF32LB52 家族「`PAxx_I2C_UART` / `PAxx_TIM` 固定通用分配组」的写法。本表不在每行重复列出 `MATRIX_DIOx`。
- **专用复用（Func1/2/3/…）**：该 IO 上固化的特定外设功能（如 SPI/I2S/MPI/SD/LCDC/USART/SWD/USB 等），见第 3 节「专用复用」列。
- **特殊标记前缀 `#`**：模拟 / 测试 / 唤醒 / 时钟类专用功能（`#GPADC_CHx` ADC 通道、`#WKUP_PINx` 唤醒、`#XTAL32K_XI/XO/EXT` 32K 晶振、`#USB11_DP/DM` USB、`#EFUSE_PWR` 熔丝电源、`#RTC_CLK`/`#LPTIM2_OUT`/`#LPTIM2_OUTB` 时钟/定时输出、`#ADC1N`/`#ADC2P`/`#ADC2N` 音频 ADC）。

## 3. 大核 GPIO（HPSYS / GPIO Group A）PINMUX 总表

> 列说明：**QFN68** = 7×7 封装是否引出（Y/—）；**QFN80/BGA112** = 8×8 / 5.4×4.4 封装是否引出；**PUPD** = 上下拉默认；**PadType** = 管脚电气类型（TYPE1/TYPE2）；**默认 Func0** = 上电默认 GPIO；**专用复用** = 固化外设功能（括号标 Func 选择器号）；**特殊标记** = `#` 类模拟/唤醒/时钟功能。
> **物理引脚号（Pin#）本表未列**，取自规格书 Table 5-2/5-3（见「与规格书差异」第 1 条）。所有 PA 均含 `MATRIX_DIOx`（Func16，矩阵交叉开关）未逐行列出。

| PA | QFN68 | QFN80/BGA112 | PUPD | PadType | 默认 Func0 | 专用复用 (FuncN) | 特殊标记 (#) |
|---|---|---|---|---|---|---|---|
| PA00 | Y | Y | PD | TYPE1 | GPIO_A0 | LCDC1_SPI_RSTB(F1) / SD2_DIO2(F3) | — |
| PA01 | Y | Y | PD | TYPE1 | GPIO_A1 | SD2_DIO3(F3) | — |
| PA02 | Y | Y | PD | TYPE1 | GPIO_A2 | LCDC1_SPI_TE(F1) / SD2_CLK(F3) | — |
| PA03 | Y | Y | PU | TYPE1 | GPIO_A3 | LCDC1_SPI_CS(F1) / SD2_CMD(F3) | — |
| PA04 | Y | Y | PD | TYPE1 | GPIO_A4 | LCDC1_SPI_CLK(F1) / SD2_DIO0(F3) | — |
| PA05 | Y | Y | PD | TYPE1 | GPIO_A5 | LCDC1_SPI_DIO0(F1) / SD2_DIO1(F3) | — |
| PA06 | Y | Y | PD | TYPE1 | GPIO_A6 | LCDC1_SPI_DIO1(F1) / SD1_DIO2(F2) | — |
| PA07 | Y | Y | PD | TYPE1 | GPIO_A7 | LCDC1_SPI_DIO2(F1) / SD1_DIO3(F2) | — |
| PA08 | Y | Y | PD | TYPE1 | GPIO_A8 | LCDC1_SPI_DIO3(F1) / SD1_CLK(F2) | — |
| PA09 | Y | Y | PD | TYPE1 | GPIO_A9 | SD1_CMD(F2) | #ADC1N(F15) |
| PA10 | Y | Y | PD | TYPE1 | GPIO_A10 | SD1_DIO0(F2) | #ADC2P(F15) |
| PA11 | Y | Y | PU | TYPE1 | GPIO_A11 | MPI3_CS2(F1) / SD1_DIO1(F2) | #ADC2N(F15) |
| PA12 | Y | Y | PU | TYPE1 | GPIO_A12 | MPI3_CS(F1) / SD1_DIO2(F2) | — |
| PA13 | Y | Y | PD | TYPE1 | GPIO_A13 | MPI3_DIO1(F1) / SD1_DIO3(F2) | — |
| PA14 | Y | Y | PD | TYPE1 | GPIO_A14 | MPI3_DIO2(F1) / SD1_CLK(F2) | — |
| PA15 | Y | Y | PD | TYPE1 | GPIO_A15 | MPI3_DIO0(F1) / SD1_CMD(F2) | — |
| PA16 | Y | Y | PD | TYPE1 | GPIO_A16 | MPI3_CLK(F1) / SD1_DIO0(F2) | — |
| PA17 | Y | Y | PD | TYPE1 | GPIO_A17 | MPI3_DIO3(F1) / SD1_DIO1(F2) | — |
| PA18 | Y | Y | PU | TYPE2 | GPIO_A18 | USART1_RXD(F1) / SWCLK(F2) | — |
| PA19 | Y | Y | PU | TYPE2 | GPIO_A19 | USART1_TXD(F1) / SWDIO(F2) | — |
| PA20 | Y | Y | PD | TYPE1 | GPIO_A20 | SWO(F1) | — |
| PA21 | — | Y | PD | TYPE1 | GPIO_A21 | — | — |
| PA22 | Y | Y | - | TYPE1 | GPIO_A22 | SD1_DIO2(F2) / SD2_DIO2(F3) | #XTAL32K_XI(F15) |
| PA23 | Y | Y | - | TYPE1 | GPIO_A23 | SD1_DIO3(F2) / SD2_DIO3(F3) | #XTAL32K_XO(F15) |
| PA24 | Y | Y | PD | TYPE1 | GPIO_A24 | SPI1_DIO(F1) / SD1_CLK(F2) / SD2_CLK(F3) | #RTC_CLK(F4) / #LPTIM2_OUT(F5) / #LPTIM2_OUTB(F6) |
| PA25 | Y | Y | PD | TYPE1 | GPIO_A25 | SPI1_DI(F1) / SD1_CMD(F2) / SD2_CMD(F3) | #RTC_CLK(F4) / #LPTIM2_OUT(F5) / #LPTIM2_OUTB(F6) / #XTAL32K_EXT(F15) |
| PA26 | Y | Y | PU | TYPE1 | GPIO_A26 | SD1_DIO0(F2) / SD2_DIO0(F3) | #RTC_CLK(F4) / #LPTIM2_OUT(F5) / #LPTIM2_OUTB(F6) |
| PA27 | Y | Y | PU | TYPE1 | GPIO_A27 | SD1_DIO1(F2) / SD2_DIO1(F3) | #RTC_CLK(F4) / #LPTIM2_OUT(F5) / #LPTIM2_OUTB(F6) |
| PA28 | Y | Y | PD | TYPE1 | GPIO_A28 | SPI1_CLK(F1) / SD2_DIO2(F3) | #GPADC_CH0(F15) |
| PA29 | Y | Y | PD | TYPE1 | GPIO_A29 | SPI1_CS(F1) / SD2_DIO3(F3) | #GPADC_CH1(F15) |
| PA30 | Y | Y | PD | TYPE1 | GPIO_A30 | SD2_CLK(F3) | #EFUSE_PWR(F4) / #GPADC_CH2(F15) |
| PA31 | Y | Y | PD | TYPE1 | GPIO_A31 | SD2_CMD(F3) | #GPADC_CH3(F15) |
| PA32 | Y | Y | PD | TYPE1 | GPIO_A32 | SD2_DIO0(F3) | #GPADC_CH4(F15) |
| PA33 | Y | Y | PD | TYPE1 | GPIO_A33 | SD2_DIO1(F3) | #WKUP_PIN(F5) / #GPADC_CH5(F15) |
| PA34 | Y | Y | PD | TYPE1 | GPIO_A34 | — | #WKUP_PIN(F5) / #GPADC_CH6(F15) |
| PA35 | Y | Y | PD | TYPE1 | GPIO_A35 | — | #USB11_DP(F4) / #WKUP_PIN(F5) / #GPADC_CH7(F15) |
| PA36 | Y | Y | PD | TYPE1 | GPIO_A36 | — | #USB11_DM(F4) / #WKUP_PIN(F5) / #GPADC_CH8(F15) |
| PA37 | Y | Y | PD | TYPE1 | GPIO_A37 | SPI2_DIO(F1) / SD1_DIO2(F2) | #WKUP_PIN(F5) / #GPADC_CH9(F15) |
| PA38 | Y | Y | PD | TYPE1 | GPIO_A38 | SPI2_DI(F1) / SD1_DIO3(F2) | #WKUP_PIN(F5) / #GPADC_CH10(F15) |
| PA39 | Y | Y | PU | TYPE1 | GPIO_A39 | SPI2_CLK(F1) / SD1_CLK(F2) | #WKUP_PIN(F5) |
| PA40 | Y | Y | PU | TYPE1 | GPIO_A40 | SPI2_CS(F1) / SD1_CMD(F2) | #WKUP_PIN(F5) |
| PA41 | Y | Y | PU | TYPE1 | GPIO_A41 | SD1_DIO0(F2) | #WKUP_PIN(F5) |
| PA42 | Y | Y | PU | TYPE1 | GPIO_A42 | SD1_DIO1(F2) | #WKUP_PIN(F5) |
| PA43 | Y | Y | PD | TYPE2 | GPIO_A43 | SWCLK(F1) | — |
| PA44 | Y | Y | PD | TYPE2 | GPIO_A44 | SWDIO(F1) | — |
| PA45 | — | Y | PD | TYPE1 | GPIO_A45 | SD2_DIO2(F3) | — |
| PA46 | — | Y | PD | TYPE1 | GPIO_A46 | SD2_DIO3(F3) | — |
| PA47 | — | Y | PD | TYPE1 | GPIO_A47 | SD2_CLK(F3) | — |
| PA48 | — | Y | PD | TYPE1 | GPIO_A48 | SD2_CMD(F3) | — |
| PA49 | — | Y | PD | TYPE1 | GPIO_A49 | SD2_DIO0(F3) | — |
| PA50 | — | Y | PD | TYPE1 | GPIO_A50 | SD2_DIO1(F3) | — |
| PA51 | — | Y | PD | TYPE1 | GPIO_A51 | — | — |
| PA52 | — | Y | PD | TYPE1 | GPIO_A52 | — | — |
| PA53 | — | Y | PD | TYPE1 | GPIO_A53 | — | — |
| PA54 | — | Y | PD | TYPE1 | GPIO_A54 | — | — |
| PA55 | Y | Y | PD | TYPE1 | GPIO_A55 | — | #ADC1P(F15) |
| PA56 | Y | Y | PD | TYPE1 | GPIO_A56 | — | #MICBIAS(F15) |
| PA57 | — | Y | PD | TYPE1 | GPIO_A57 | — | — |

> 注：QFN68 封装未引出的 PA = **PA21、PA45、PA46、PA47、PA48、PA49、PA50、PA51、PA52、PA53、PA54、PA57**（共 12 个 PA 仅存在于 QFN80/BGA112）；故 QFN68 = 46 GPIO，QFN80/BGA112 = 58 GPIO。

## 4. Matrix Index（矩阵交叉开关信号表，160 个）

> 下表为 `matrix index` 工作表，列出矩阵可路由的 160 个信号（idx 16–175）。任意信号可经 `MATRIX_DIOx`（Func16）路由到任意 PA 引脚（见第 2 节）。按模块分组：

### I2C（8 个信号）

| idx | func |
|---|---|
| 16 | I2C1_SCL |
| 17 | I2C1_SDA |
| 18 | I2C2_SCL |
| 19 | I2C2_SDA |
| 20 | I2C3_SCL |
| 21 | I2C3_SDA |
| 22 | I2C4_SCL |
| 23 | I2C4_SDA |
### SPI（8 个信号）

| idx | func |
|---|---|
| 24 | SPI1_CLK |
| 25 | SPI1_CS |
| 26 | SPI1_DI |
| 27 | SPI1_DIO |
| 28 | SPI2_CLK |
| 29 | SPI2_CS |
| 30 | SPI2_DI |
| 31 | SPI2_DIO |
### UART（12 个信号）

| idx | func |
|---|---|
| 32 | UART1_TXD |
| 33 | UART1_RXD |
| 34 | UART1_RTS |
| 35 | UART1_CTS |
| 36 | UART2_TXD |
| 37 | UART2_RXD |
| 38 | UART2_RTS |
| 39 | UART2_CTS |
| 40 | UART3_TXD |
| 41 | UART3_RXD |
| 42 | UART3_RTS |
| 43 | UART3_CTS |
### CAN（4 个信号）

| idx | func |
|---|---|
| 44 | CAN1_TXD |
| 45 | CAN1_RXD |
| 46 | CAN2_TXD |
| 47 | CAN2_RXD |
### PTA/BT（6 个信号）

| idx | func |
|---|---|
| 48 | BT_ACTIVE |
| 49 | BT_PRIORITY |
| 50 | BT_COLLISION |
| 51 | WLAN_ACTIVE |
| 52 | BT_TX |
| 53 | BT_RX |
### GPTIM（10 个信号）

| idx | func |
|---|---|
| 54 | GPTIM1_CH1 |
| 55 | GPTIM1_CH2 |
| 56 | GPTIM1_CH3 |
| 57 | GPTIM1_CH4 |
| 58 | GPTIM1_ETR |
| 59 | GPTIM2_CH1 |
| 60 | GPTIM2_CH2 |
| 61 | GPTIM2_CH3 |
| 62 | GPTIM2_CH4 |
| 63 | GPTIM2_ETR |
### LPTIM（6 个信号）

| idx | func |
|---|---|
| 64 | LPTIM1_IN |
| 65 | LPTIM1_OUT |
| 66 | LPTIM1_ETR |
| 67 | LPTIM2_IN |
| 68 | LPTIM2_OUT |
| 69 | LPTIM2_ETR |
### ATIM（20 个信号）

| idx | func |
|---|---|
| 70 | ATIM1_CH1 |
| 71 | ATIM1_CH2 |
| 72 | ATIM1_CH3 |
| 73 | ATIM1_CH4 |
| 74 | ATIM1_ETR |
| 75 | ATIM1_CH1N |
| 76 | ATIM1_CH2N |
| 77 | ATIM1_CH3N |
| 78 | ATIM1_BK |
| 79 | ATIM1_BK2 |
| 80 | ATIM2_CH1 |
| 81 | ATIM2_CH2 |
| 82 | ATIM2_CH3 |
| 83 | ATIM2_CH4 |
| 84 | ATIM2_ETR |
| 85 | ATIM2_CH1N |
| 86 | ATIM2_CH2N |
| 87 | ATIM2_CH3N |
| 88 | ATIM2_BK |
| 89 | ATIM2_BK2 |
### PWM（5 个信号）

| idx | func |
|---|---|
| 90 | PWM1_CH1 |
| 91 | PWM1_CH2 |
| 92 | PWM1_CH3 |
| 93 | PWM1_CH4 |
| 94 | PWM1_CH5 |
### I2S（10 个信号）

| idx | func |
|---|---|
| 95 | I2S1_MCLK |
| 96 | I2S1_SDO |
| 97 | I2S1_SDI |
| 98 | I2S1_BCK |
| 99 | I2S1_LRCK |
| 100 | I2S2_MCLK |
| 101 | I2S2_SDO |
| 102 | I2S2_SDI |
| 103 | I2S2_BCK |
| 104 | I2S2_LRCK |
### PTM（16 个信号）

| idx | func |
|---|---|
| 105 | PTM1_CH0 |
| 106 | PTM1_CH1 |
| 107 | PTM1_CH2 |
| 108 | PTM1_CH3 |
| 109 | PTM1_CH4 |
| 110 | PTM1_CH5 |
| 111 | PTM1_CH6 |
| 112 | PTM1_CH7 |
| 113 | PTM1_CH8 |
| 114 | PTM1_CH9 |
| 115 | PTM1_CH10 |
| 116 | PTM1_CH11 |
| 117 | PTM1_CH12 |
| 118 | PTM1_CH13 |
| 119 | PTM1_CH14 |
| 120 | PTM1_CH15 |
### LDCD（30 个信号）

| idx | func |
|---|---|
| 121 | LCDC_IF0 |
| 122 | LCDC_IF1 |
| 123 | LCDC_IF2 |
| 124 | LCDC_IF3 |
| 125 | LCDC_IF4 |
| 126 | LCDC_IF5 |
| 127 | LCDC_IF6 |
| 128 | LCDC_IF7 |
| 129 | LCDC_IF8 |
| 130 | LCDC_IF9 |
| 131 | LCDC_IF10 |
| 132 | LCDC_IF11 |
| 133 | LCDC_IF12 |
| 134 | LCDC_IF13 |
| 135 | LCDC_IF14 |
| 136 | LCDC_IF15 |
| 137 | LCDC_IF16 |
| 138 | LCDC_IF17 |
| 139 | LCDC_IF18 |
| 140 | LCDC_IF19 |
| 141 | LCDC_IF20 |
| 142 | LCDC_IF21 |
| 143 | LCDC_IF22 |
| 144 | LCDC_IF23 |
| 145 | LCDC_IF24 |
| 146 | LCDC_IF25 |
| 147 | LCDC_IF26 |
| 148 | LCDC_IF27 |
| 149 | LCDC_IF28 |
| 150 | LCDC_IF29 |
### PDM（6 个信号）

| idx | func |
|---|---|
| 151 | PDM1_CLK |
| 152 | PDM2_CLK |
| 153 | PDM1_DATA |
| 154 | PDM1_DATA2 |
| 155 | PDM2_DATA |
| 156 | PDM2_DATA2 |
### DCMI（19 个信号）

| idx | func |
|---|---|
| 157 | DCMI_CLK |
| 158 | DCMI_HSYNC |
| 159 | DCMI_VSYNC |
| 160 | DCMI_DI0 |
| 161 | DCMI_DI1 |
| 162 | DCMI_DI2 |
| 163 | DCMI_DI3 |
| 164 | DCMI_DI4 |
| 165 | DCMI_DI5 |
| 166 | DCMI_DI6 |
| 167 | DCMI_DI7 |
| 168 | DCMI_DI8 |
| 169 | DCMI_DI9 |
| 170 | DCMI_DI10 |
| 171 | DCMI_DI11 |
| 172 | DCMI_DI12 |
| 173 | DCMI_DI13 |
| 174 | DCMI_DI14 |
| 175 | DCMI_DI15 |

## 5. LCD 接口复用（LCDC）

### 5.1 lcdc mux（IF_SEL 选择接口类型）

> 括号数字（8 / 17 / 22 / 24 / 30）为各接口的 IF_SEL 子接口选择器索引；末列数字为该 lcdc_if 信号所占 PAD 数（4/3/2）。`lcdc_if[0..29]` 共 30 个 LCD 接口信号。

| lcdc_if | IF_SEL=0 SPI | IF_SEL=1 JDI | IF_SEL=2 EPD | IF_SEL=3 DBI | DPI | PAD数 |
|---|---|---|---|---|---|---|
| lcdc_if[0] | LCDC_SPI_TE |  | LCDC_TCON_GDSP | LCDC_8080_TE | LCDC_DPI_CLK | 4 |
| lcdc_if[1] | LCDC_SPI_RSTB |  | LCDC_TCON_GDCLK | LCDC_8080_RSTB | LCDC_DPI_HSYNC | 4 |
| lcdc_if[2] | LCDC_SPI_CS |  | LCDC_TCON_SDCLK | LCDC_8080_CS | LCDC_DPI_VSYNC | 4 |
| lcdc_if[3] | LCDC_SPI_CLK |  | LCDC_TCON_SDSTL | LCDC_8080_WR | LCDC_DPI_DE | 4 |
| lcdc_if[4] |  |  | LCDC_TCON_SDLE | LCDC_8080_RD | LCDC_DPI_SD | 3 |
| lcdc_if[5] |  |  | LCDC_TCON_SDOE | LCDC_8080_DC | LCDC_DPI_CM | 3 |
| lcdc_if[6] | LCDC_SPI_DIO0 |  | LCDC_TCON_SDAT0 | LCDC_8080_DIO0 | LCDC_DPI_R0 | 4 |
| lcdc_if[7] | LCDC_SPI_DIO1 |  | LCDC_TCON_SDAT1 | LCDC_8080_DIO1 | LCDC_DPI_R1 | 4 |
| lcdc_if[8] | LCDC_SPI_DIO2 |  | LCDC_TCON_SDAT2 | LCDC_8080_DIO2 | LCDC_DPI_R2 | 4 |
| lcdc_if[9] | LCDC_SPI_DIO3 |  | LCDC_TCON_SDAT3 | LCDC_8080_DIO3 | LCDC_DPI_R3 | 4 |
| lcdc_if[10] |  | LCDC_JDI_SCS | LCDC_TCON_SDAT4 | LCDC_8080_DIO4 | LCDC_DPI_R4 | 4 |
| lcdc_if[11] |  | LCDC_JDI_SCLK | LCDC_TCON_SDAT5 | LCDC_8080_DIO5 | LCDC_DPI_R5 | 4 |
| lcdc_if[12] |  | LCDC_JDI_SO | LCDC_TCON_SDAT6 | LCDC_8080_DIO6 | LCDC_DPI_R6 | 4 |
| lcdc_if[13] |  | LCDC_JDI_DISP | LCDC_TCON_SDAT7 | LCDC_8080_DIO7 | LCDC_DPI_R7 | 4 |
| lcdc_if[14] |  | LCDC_JDI_EXTCOMIN | LCDC_TCON_SDAT8 | LCDC_8080_DIO8 | LCDC_DPI_G0 | 4 |
| lcdc_if[15] |  |  | LCDC_TCON_SDAT9 | LCDC_8080_DIO9 | LCDC_DPI_G1 | 3 |
| lcdc_if[16] |  |  | LCDC_TCON_SDAT10 | LCDC_8080_DIO10 | LCDC_DPI_G2 | 3 |
| lcdc_if[17] |  |  | LCDC_TCON_SDAT11 | LCDC_8080_DIO11 | LCDC_DPI_G3 | 3 |
| lcdc_if[18] |  | LCDC_JDI_VCK | LCDC_TCON_SDAT12 | LCDC_8080_DIO12 | LCDC_DPI_G4 | 4 |
| lcdc_if[19] |  | LCDC_JDI_XRST | LCDC_TCON_SDAT13 | LCDC_8080_DIO13 | LCDC_DPI_G5 | 4 |
| lcdc_if[20] |  | LCDC_JDI_HCK | LCDC_TCON_SDAT14 | LCDC_8080_DIO14 | LCDC_DPI_G6 | 4 |
| lcdc_if[21] |  | LCDC_JDI_HST | LCDC_TCON_SDAT15 | LCDC_8080_DIO15 | LCDC_DPI_G7 | 4 |
| lcdc_if[22] |  | LCDC_JDI_ENB |  | LCDC_8080_RWN | LCDC_DPI_B0 | 3 |
| lcdc_if[23] |  | LCDC_JDI_VST |  | LCDC_8080_CS2 | LCDC_DPI_B1 | 3 |
| lcdc_if[24] |  | LCDC_JDI_R1 |  |  | LCDC_DPI_B2 | 2 |
| lcdc_if[25] |  | LCDC_JDI_G1 |  |  | LCDC_DPI_B3 | 2 |
| lcdc_if[26] |  | LCDC_JDI_B1 |  |  | LCDC_DPI_B4 | 2 |
| lcdc_if[27] |  | LCDC_JDI_R2 |  |  | LCDC_DPI_B5 | 2 |
| lcdc_if[28] |  | LCDC_JDI_G2 |  |  | LCDC_DPI_B6 | 2 |
| lcdc_if[29] |  | LCDC_JDI_B2 |  |  | LCDC_DPI_B7 | 2 |

### 5.2 lcdc dpi inner mux（DPI RGB 位宽复用）

> mode 0–7 选择 RGB 数据位宽与映射（rgb565/rgb666/rgb888 及其 over-8bit 变体）；software default = mode 1。

| matrix net | dpi_d | 0(rgb565 conf1) | 1(rgb565 conf2) 默认 | 2(rgb565 conf3) | 3(rgb666 conf1) | 4(rgb666 conf2) | 5(rgb888) | 6(rgb666 over8) | 7(rgb888 over8) |
|---|---|---|---|---|---|---|---|---|---|
| lcdc_if[22] | dpi_d[0] | b0 | b0 |  | b0 | b0 | b0 | r0/g0/b0 | r0/g0/b0 |
| lcdc_if[23] | dpi_d[1] | b1 | b1 | b0 | b1 | b1 | b1 | r1/g1/b1 | r1/g1/b1 |
| lcdc_if[24] | dpi_d[2] | b2 | b2 | b1 | b2 | b2 | b2 | r2/g2/b2 | r2/g2/b2 |
| lcdc_if[25] | dpi_d[3] | b3 | b3 | b2 | b3 | b3 | b3 | r3/g3/b3 | r3/g3/b3 |
| lcdc_if[26] | dpi_d[4] | b4 | b4 | b3 | b4 | b4 | b4 | r4/g4/b4 | r4/g4/b4 |
| lcdc_if[27] | dpi_d[5] | g0 |  | b4 | b5 | b5 | b5 | r5/g5/b5 | r5/g5/b5 |
| lcdc_if[28] | dpi_d[6] | g1 |  |  | g0 |  | b6 |  | r6/g6/b6 |
| lcdc_if[29] | dpi_d[7] | g2 |  |  | g1 |  | b7 |  | r7/g7/b7 |
| lcdc_if[14] | dpi_d[8] | g3 | g0 | g0 | g2 | g0 | g0 |  |  |
| lcdc_if[15] | dpi_d[9] | g4 | g1 | g1 | g3 | g1 | g1 |  |  |
| lcdc_if[16] | dpi_d[10] | g5 | g2 | g2 | g4 | g2 | g2 |  |  |
| lcdc_if[17] | dpi_d[11] | r0 | g3 | g3 | g5 | g3 | g3 |  |  |
| lcdc_if[18] | dpi_d[12] | r1 | g4 | g4 | r0 | g4 | g4 |  |  |
| lcdc_if[19] | dpi_d[13] | r2 | g5 | g5 | r1 | g5 | g5 |  |  |
| lcdc_if[20] | dpi_d[14] | r3 |  |  | r2 |  | g6 |  |  |
| lcdc_if[21] | dpi_d[15] | r4 |  |  | r3 |  | g7 |  |  |
| lcdc_if[6] | dpi_d[16] |  | r0 |  | r4 | r0 | r0 |  |  |
| lcdc_if[7] | dpi_d[17] |  | r1 | r0 | r5 | r1 | r1 |  |  |
| lcdc_if[8] | dpi_d[18] |  | r2 | r1 |  | r2 | r2 |  |  |
| lcdc_if[9] | dpi_d[19] |  | r3 | r2 |  | r3 | r3 |  |  |
| lcdc_if[10] | dpi_d[20] |  | r4 | r3 |  | r4 | r4 |  |  |
| lcdc_if[11] | dpi_d[21] |  |  | r4 |  | r5 | r5 |  |  |
| lcdc_if[12] | dpi_d[22] |  |  |  |  |  | r6 |  |  |
| lcdc_if[13] | dpi_d[23] |  |  |  |  |  | r7 |  |  |

## 6. 与规格书（DS5702 3.3V / DS5701 电池）差异 / 待核实

1. **物理引脚号（Pin#）本表缺失**：pinmux xlsx 仅给 QFN68 / QFN80-BGA112 的 Y/N 引出标记，未列具体封装引脚号；物理 Pin# 须查规格书 Table 5-2（大核 GPIO）/ Table 5-3（专用管脚）。待补。
2. **GPIO 数量**：本表 QFN68 = 46 GPIO（PA21、PA45–PA54、PA57 未引出）；规格书页 [[SF32LB57]] 标注 QFN68 = 47 GPIO，二者存在偏差，**以本 pinmux 表为准**，规格书 GPIO 计数待原厂复核（草稿 V0.2）。
3. **LPSYS / 小核 GPIO 缺失**：本 pinmux xlsx 仅含 HPSYS（大核 GPIO Group A），无 LPSYS/PBR 工作表；SF32LB57 为双大核架构，小核 GPIO 复用是否另行提供待用户手册确认。
4. **MATRIX_DIOx 矩阵路由**：57 家族以矩阵交叉开关实现 I2C/UART/TIM/PWM 等通用分配（替代 52 家族固定 `PAxx_I2C_UART`/`PAxx_TIM` 列），具体矩阵信号见第 4 节。
5. **专用复用外设命名差异（相对 52 家族）**：57 为 **MPI3**（非 MPI2）、**SD1/SD2**（双 SD 控制器）、**USART1**（单 Debug UART，PA18/PA19）、**无独立 PA_I2C_UART/PA_TIM 列**；禁止跨家族套用 52 家族引脚分配。
6. **PA34 电源键（PWRKEY）**：PA34 在 57 家族同样带 PWRKEY（开关机）硬件功能，本表 PA34 行未列 PWRKEY 复用名（属纯硬件功能）。与 52 不同，**57 可将 PA34 的 PWRKEY 功能经 PMUC WER.PWRKEY = 0 关闭**，关闭后即可完全当作普通 GPIO、无高电平保持时长限制；关闭前长按高电平仍触发复位。详见 [[DR_PA34_PowerKey_GPIO]]。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- GPIO：[[SF32LB57_Peripheral_GPIO]]｜电源：[[SF32LB57_Peripheral_Power]]｜存储：[[SF32LB57_Peripheral_Memory]]｜串口：[[SF32LB57_Peripheral_Serial]]
- 52 家族对照：[[SF32LB52_Pinmux]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [pinmux - 202600901.xlsx]，Raw：`raw/mcu/all_chip/pinmux/pinmux - 202600901.xlsx`（原件 `E:/Work/Package/ButterFli-Micro-S/pinmux/pinmux - 202600901.xlsx` 仅复制未移动）。
2. [DS5702-SF32LB57X V0.2]，Raw：`raw/mcu/all_chip/datasheets/DS5702-SF32LB57X-芯片技术规格书-V0p2-20260909.pdf`，Table 5-2（GPIO 复用）、Table 5-4（Matrix Index）。
3. [DS5701-SF32LB57x V0.2]，Raw：`raw/mcu/all_chip/datasheets/DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf`。
