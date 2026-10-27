---
mcu_family: SF32LB52
mcu_series: ["3.3V供电系列", "电池供电系列"]
mcu_model: ["SF32LB52X", "SF32LB52x"]
series_applicability: ["通用-两系列共用"]
hardware_version: "SF32LB52_pinmux_20230707"
sources:
  - "[[SF32LB52X_Datasheet_V0.2.6]]"
  - "[[SF32LB52x_Datasheet_V2.5.5]]"
type: pinmux
---

# SF32LB52 家族 PINMUX（引脚复用矩阵）

> **权威来源**：`SF32LB52_pinmux_20230707.xlsx`（已导入 `raw/mcu/all_chip/pinmux/`）。
> **规则**：PINMUX 相关内容**以此表格为准**；规格书（DS5201 电池 / DS5202 3.3V）上若与下表有差异，原则上以本表为准，并在文末「与规格书差异」一节逐条标注。**例外：GPADC 通道编号以规格书为准（见差异 1）。**
> 物理引脚号（Pin#）取自规格书 Table 5-2，仅供对照；规格书本身未列出 USART1 等的引脚分配（见差异第 2 条）。

## 1. 工作表（Sheet）结构与含义

| 工作表 | 对应域 | 含义 | 是否入库 |
|---|---|---|---|
| **HPSYS** | 大核（HCPU / Big Core） | 大核 GPIO 复用矩阵 | ✅ 入库（见第 3、4 节） |
| └ SIP Group A | 内部合封存储 | 合封 SiP 存储器的内部 PAD（PAD_SA00–SA12），**芯片内部连接，不涉及片外硬件知识** | ⛔ 仅列名，不展开（见第 5 节） |
| └ GPIO Group A | 大核 GPIO | **PA00–PA44**（共 45 个 PA 信号） | ✅ 入库（见第 3 节） |
| **LPSYS** | 小核（LCPU / Little Core） | 小核 GPIO 复用矩阵 | ✅ 入库（见第 4 节） |
| └ GPIO Group B | 小核 GPIO | **PB00–PB03**，芯片内部映射到 PA00–PA03 | ✅ 入库 |
| └ PBR Group | 电源/RF 控制 | PBR0–PBR3（非 GPIO，电源/RF 控制） | ⛔ 仅说明（见第 4 节） |

> ⚠️ **PA21 仅存在于 3.3V 系列（SF32LB52X）**：PA21 对应 pin24；电池系列（SF32LB52x）的 pin24 为电源引脚 **VCC**，无 PA21（故电池系列共 44 GPIO）。本表的 45 个 PA 为 3.3V 系列完整集合；电池系列请忽略 PA21 行。PA21 **主要用途是给外挂 Flash 存储做电源控制**（Nor Flash 可常供电不必断电，SPI Nand / SD Nand 必须控制供电；电池系列无 PA21 时改用默认 PU 的 GPIO），详见 [[SF32LB52_Peripheral_Memory]] §4.1。

## 2. PINMUX 类型说明（命名规则）

- **所有 PAxx 默认功能 = `GPIO_Ax`（Func0）**：未做复用配置时即为通用 GPIO。
- **`PAxx_I2C_UART`（通用分配组，所有 PA 均有）**：该 IO 上可**任意分配 I2C 和 UART 的信号**（SiFli 灵活复用，不固定到某一 I2C/UART 外设）。
- **`PAxx_TIM`（通用分配组，所有 PA 均有）**：该 IO 上可**任意分配与定时器（TIM/PWM）相关的信号**。
- **专用复用（Func1/2/7/8）**：该 IO 上固化的特定外设功能（如 SPI/I2S/MPI/SD/LCDC/JDI/PDM/USB 等），见下表「专用复用」列。
- **特殊标记前缀**：
  - `#` 开头 = 模拟/测试/唤醒类专用功能（如 `#GPADC_CHx` ADC 通道、`#WKUP_PINx` 唤醒、`#XTAL32K_XI/XO` 32K 晶振、`#USB11_DP/DM` USB、`#EFUSE_PWR`、`#ACTESTx`/`#DCTESTx` 测试、`#AUD_CLK_EXT` 外部音频时钟）。
  - `!` 开头 = 芯片内部**调试观测（debug-trace）信号**（如 `!DBG_DO0…15`、`!DBG_CLK`），属片上调试可见性，非普通外设复用。
  - 括号 `( )` 包裹 = 备选/次要功能：
    - `(JDI_*)` = **串行 JDI 屏接口信号**（属于 LCD 类别的串行 JDI 显示接口，如 JDI_EXTCOMIN / JDI_SO / JDI_SCLK / JDI_SCS / JDI_DISP）。
    - `(PWR_KEY)` = **PA34 上带的默认硬件功能**：长按 10s 强制复位芯片（纯硬件行为，不受软件控制）；软件可通过寄存器**设置长按的时长**（其余时间该引脚仍可作普通 GPIO / ADC）。

## 3. 大核 GPIO（HPSYS / GPIO Group A）PINMUX 总表

> 列说明：**Pin#(3.3V·DS5202)** = 3.3V 系列物理引脚号；**Pin#(电池·DS5201)** = 电池系列物理引脚号（PA21 显示「无(未引出)」）。PUPD = 上下拉默认。
> **GPADC 通道号已按规格书更正为 CH0–CH6**（PINMUX 原表为 CH1–CH7 的 +1 偏移，已弃用，见差异 1）。

| PA | Pin#(3.3V·DS5202) | Pin#(电池·DS5201) | PUPD | 默认 Func0 | 专用复用 (Func1/2/7/8) | 通用分配组 | 特殊标记 |
|---|---|---|---|---|---|---|---|
| PA00 | 51 | 51 | PD | GPIO_A0 | LCDC1_SPI_RSTB / LCDC1_8080_RSTB | I2C_UART / TIM | — |
| PA01 | 50 | 50 | PD | GPIO_A1 | — | I2C_UART / TIM | — |
| PA02 | 49 | 49 | PD | GPIO_A2 | LCDC1_SPI_TE / I2S1_MCLK / LCDC1_JDI_B2 / LCDC1_8080_TE | I2C_UART / TIM | #ACTEST0 / !DBG_DO0 |
| PA03 | 48 | 48 | PU | GPIO_A3 | LCDC1_SPI_CS / I2S1_SDO / LCDC1_JDI_B1 / LCDC1_8080_CS | I2C_UART / TIM | #ACTEST1 / !DBG_DO1 |
| PA04 | 47 | 47 | PD | GPIO_A4 | LCDC1_SPI_CLK / I2S1_SDI / LCDC1_JDI_G1 / LCDC1_8080_WR | I2C_UART / TIM | !DBG_DO2 |
| PA05 | 46 | 46 | PD | GPIO_A5 | LCDC1_SPI_DIO0 / I2S1_BCK / LCDC1_JDI_R1 / LCDC1_8080_RD | I2C_UART / TIM | !DBG_DO3 |
| PA06 | 45 | 45 | PD | GPIO_A6 | LCDC1_SPI_DIO1 / (JDI_EXTCOMIN) / I2S1_LRCK / LCDC1_JDI_HST / LCDC1_8080_DC | I2C_UART / TIM | !DBG_DO4 |
| PA07 | 44 | 44 | PD | GPIO_A7 | LCDC1_SPI_DIO2 / PDM1_CLK / LCDC1_JDI_ENB / LCDC1_8080_DIO0 | I2C_UART / TIM | !DBG_DO5 |
| PA08 | 43 | 43 | PD | GPIO_A8 | LCDC1_SPI_DIO3 / (JDI_SO) / PDM1_DATA / LCDC1_JDI_VST / LCDC1_8080_DIO1 | I2C_UART / TIM | !DBG_DO6 |
| PA09 | 42 | 42 | PD | GPIO_A9 | — | I2C_UART / TIM | !DBG_DO7 |
| PA10 | 35 | 35 | PD | GPIO_A10 | — | I2C_UART / TIM | — |
| PA11 | 34 | 34 | PU | GPIO_A11 | — | I2C_UART / TIM | !AUD_CLK_EXT |
| PA12 | 33 | 33 | PU | GPIO_A12 | MPI2_CS / SD1_DIO2 | I2C_UART / TIM | — |
| PA13 | 32 | 32 | PD | GPIO_A13 | MPI2_DIO1 / SD1_DIO3 | I2C_UART / TIM | — |
| PA14 | 31 | 31 | PD | GPIO_A14 | MPI2_DIO2 / SD1_CLK | I2C_UART / TIM | — |
| PA15 | 30 | 30 | PD | GPIO_A15 | MPI2_DIO0 / SD1_CMD | I2C_UART / TIM | — |
| PA16 | 29 | 29 | PD | GPIO_A16 | MPI2_CLK / SD1_DIO0 | I2C_UART / TIM | — |
| PA17 | 28 | 28 | PD | GPIO_A17 | MPI2_DIO3 / SD1_DIO1 | I2C_UART / TIM | — |
| PA18 | 27 | 27 | PU | GPIO_A18 | USART1_RXD / SWDIO | I2C_UART / TIM | — |
| PA19 | 26 | 26 | - | GPIO_A19 | USART1_TXD / SWCLK | I2C_UART / TIM | — |
| PA20 | 25 | 25 | PD | GPIO_A20 | — | I2C_UART / TIM | !DBG_CLK |
| PA21 | 24 | 无(未引出) | PD | GPIO_A21 | — | I2C_UART / TIM | — |
| PA22 | 11 | 11 | - | GPIO_A22 | PDM1_CLK | I2C_UART / TIM | #XTAL32K_XI |
| PA23 | 10 | 10 | - | GPIO_A23 | PDM1_DATA | I2C_UART / TIM | #XTAL32K_XO |
| PA24 | 9 | 9 | PD | GPIO_A24 | SPI1_DIO / I2S1_MCLK | I2C_UART / TIM | #WKUP_PIN0 |
| PA25 | 8 | 8 | PD | GPIO_A25 | SPI1_DI / I2S1_SDO | I2C_UART / TIM | #XTAL32K_EXT / #WKUP_PIN1 |
| PA26 | 7 | 7 | PU | GPIO_A26 | — | I2C_UART / TIM | #WKUP_PIN2 |
| PA27 | 6 | 6 | PU | GPIO_A27 | — | I2C_UART / TIM | #WKUP_PIN3 |
| PA28 | 5 | 5 | PD | GPIO_A28 | SPI1_CLK / I2S1_SDI | I2C_UART / TIM | #GPADC_CH0 |
| PA29 | 4 | 4 | PD | GPIO_A29 | SPI1_CS / I2S1_BCK | I2C_UART / TIM | #GPADC_CH1 |
| PA30 | 3 | 3 | PD | GPIO_A30 | I2S1_LRCK | I2C_UART / TIM | #EFUSE_PWR / #DCTEST0 / #GPADC_CH2 |
| PA31 | 2 | 2 | PD | GPIO_A31 | — | I2C_UART / TIM | #DCTEST1 / #GPADC_CH3 / !DBG_DO8 |
| PA32 | 1 | 1 | PD | GPIO_A32 | — | I2C_UART / TIM | #GPADC_CH4 |
| PA33 | 67 | 67 | PD | GPIO_A33 | — | I2C_UART / TIM | #GPADC_CH5 |
| PA34 | 66 | 66 | PD | GPIO_A34 | (PWR_KEY) | I2C_UART / TIM | #GPADC_CH6 / #WKUP_PIN10 |
| PA35 | 65 | 65 | PD | GPIO_A35 | — | I2C_UART / TIM | #USB11_DP / #WKUP_PIN11 |
| PA36 | 64 | 64 | PD | GPIO_A36 | — | I2C_UART / TIM | #USB11_DM / #WKUP_PIN12 |
| PA37 | 63 | 63 | PD | GPIO_A37 | SPI2_DIO / LCDC1_8080_DIO2 | I2C_UART / TIM | #WKUP_PIN13 / !DBG_DO9 |
| PA38 | 62 | 62 | PD | GPIO_A38 | SPI2_DI | I2C_UART / TIM | #WKUP_PIN14 |
| PA39 | 61 | 61 | PU | GPIO_A39 | SPI2_CLK / (JDI_SCLK) / LCDC1_JDI_VCK / LCDC1_8080_DIO3 | I2C_UART / TIM | #WKUP_PIN15 / !DBG_DO10 |
| PA40 | 60 | 60 | PU | GPIO_A40 | SPI2_CS / (JDI_SCS) / LCDC1_JDI_XRST / LCDC1_8080_DIO4 | I2C_UART / TIM | #WKUP_PIN16 / !DBG_DO11 |
| PA41 | 59 | 59 | PU | GPIO_A41 | (JDI_DISP) / LCDC1_JDI_HCK / LCDC1_8080_DIO5 | I2C_UART / TIM | #WKUP_PIN17 / !DBG_DO12 |
| PA42 | 58 | 58 | PU | GPIO_A42 | LCDC1_JDI_R2 / LCDC1_8080_DIO6 | I2C_UART / TIM | #WKUP_PIN18 / !DBG_DO13 |
| PA43 | 57 | 57 | PD | GPIO_A43 | LCDC1_JDI_G2 / LCDC1_8080_DIO7 | I2C_UART / TIM | #WKUP_PIN19 / !DBG_DO14 |
| PA44 | 56 | 56 | PD | GPIO_A44 | — | I2C_UART / TIM | #WKUP_PIN20 / !DBG_DO15 |

## 4. 小核 GPIO（LPSYS）PINMUX

小核（LCPU）仅有 **PB00–PB03** 共 4 个 GPIO，在芯片内部**分别映射到 PA00–PA03**（与大核共用同一组物理引脚，由 LPSYS 域驱动）。

| 小核引脚 | 映射到(大核) | PUPD | 功能 (Func) |
|---|---|---|---|
| PB00 | PA00 | - | GPIO_B0 / PB00_UART / PB00_TIM / !DBG_DO0 / !DBG_CLK |
| PB01 | PA01 | - | GPIO_B1 / PB01_UART / PB01_TIM / !DBG_DO1 / !DBG_CLK |
| PB02 | PA02 | - | GPIO_B2 / PB02_UART / PB02_TIM / !DBG_DO2 / !DBG_CLK |
| PB03 | PA03 | - | GPIO_B3 / PB03_UART / PB03_TIM / !DBG_DO3 / !DBG_CLK |

> PB00_UART / PB00_TIM 含义同大核：该小核 IO 上可任意分配 UART / TIM 信号。`!DBG_CLK` 为小核调试时钟观测。

**PBR Group（非 GPIO，电源/RF 控制，仅说明不展开）**：

| PBR 引脚 | PUPD | 功能 |
|---|---|---|
| PBR0 | PD | (PSW_CTRL) / (Wireless CHG_INT) |
| PBR1 | PD | (LPTIM_OUT) |
| PBR2 | PD | (LPTIM_OUT) |
| PBR3 | PD | (32K_OUT) |

## 5. SIP Group A（内部合封存储 PAD，不涉及片外硬件知识）

HPSYS 工作表中的 **SIP Group A** 为合封（SiP）存储器与主控之间的**内部 PAD**，芯片对外无对应封装引脚，布局/驱动由 SiP 内部决定，**不纳入片外硬件知识库**。仅列 PAD 名备查：

`PAD_SA00, PAD_SA01, PAD_SA02, PAD_SA03, PAD_SA04, PAD_SA05, PAD_SA06, PAD_SA07, PAD_SA08, PAD_SA09, PAD_SA10, PAD_SA11, PAD_SA12`

## 6. 默认功能与 Debug UART 说明

- **所有 PAxx 默认 = GPIO**（Func0 = `GPIO_Ax`），其余 PAxx 未单独列出专用复用的，默认即 GPIO。
- **PA18 / PA19 = Debug UART（调试串口）**：PA18 默认 `USART1_RXD`，PA19 默认 `USART1_TXD`（PINMUX 表 Func1）。**以本表为准**（规格书 Table 5-2 未列出 USART1 引脚分配，见差异第 2 条）。⚠️ 该 UART 引脚分配由 **ROM 软件在启动阶段设置**，并非 GPIO 硬件 default 复用（故不出现在规格书硬件 default 表中）；运行时软件可重映射，但 Debug UART 固定走 PA18/PA19。
- **SWD 调试接口**：PA18/PA19 的 Func2 同时提供 `SWDIO` / `SWCLK`，可与 Debug UART 复用同一组引脚（调试阶段用 SWD，运行时用 USART1 作日志口）。

## 7. 与规格书（DS5201 电池 / DS5202 3.3V）Table 5-2 的差异

> 下表中「规格书」指 DS5201-SF32LB52x V2.5.5 与 DS5202-SF32LB52X V0.2.6 的 Table 5-2（GPIO (PA) Pin List）。两者 Table 5-2 内容一致（仅引脚引出对 PA21 不同）。

### 差异 1：GPADC 通道编号（PA28–PA34）—— 已裁定：以规格书为准

PINMUX 原表的 `#GPADC_CHx` 通道号比规格书大 1（整体 +1 偏移）：

| PA | PINMUX 原表 `#GPADC` | 规格书 `#GPADC` | 差异 |
|---|---|---|---|
| PA28 | CH1 | CH0 | +1 |
| PA29 | CH2 | CH1 | +1 |
| PA30 | CH3 | CH2 | +1 |
| PA31 | CH4 | CH3 | +1 |
| PA32 | CH5 | CH4 | +1 |
| PA33 | CH6 | CH5 | +1 |
| PA34 | CH7 | CH6 | +1 |

✅ **裁定（用户确认）**：**以规格书 CH0–CH6 为准**。第 3 节「大核 GPIO PINMUX 总表」中的 `#GPADC_CHx` 已按规格书更正为 CH0–CH6；PINMUX 原表的 CH1–CH7 视为 +1 偏移，已弃用。固件访问 PA28–PA34 的 ADC 应使用规格书通道号 CH0–CH6，原理图/PCB 标注亦以规格书为准。

### 差异 2：USART1（Debug UART）引脚分配规格书缺失 —— 已裁定：以 PINMUX 表为准

- PINMUX 表：PA18 = `USART1_RXD`、PA19 = `USART1_TXD`（Func1，Debug UART）。
- 规格书 Table 5-2：PA18/PA19 仅列 `Func2=SWDIO/SWCLK`、`Func4=PA_I2C_UART`、`Func5=PA_TIM`，**未列出任何 USART1 分配**；全文中 USART1 仅出现在存储器映射（0x5008_4000）与 IRQ[59]，**未绑定到任何 GPIO 引脚**。
- **原因**：该 UART 引脚分配由 **ROM 软件在启动阶段设置**，**并非 GPIO 硬件 default 复用**，因此不会出现在规格书的硬件 default（Table 5-2）中。
- ✅ **裁定（用户确认）**：**以 PINMUX 表为准**（PA18/PA19 = USART1 RXD/TXD，作 Debug UART）。

### 差异 3：调试观测 / 测试 / 模拟专用标记（`!DBG_*`、`#ACTEST*`、`#DCTEST*`、`#AUD_CLK_EXT`）规格书未列

- PINMUX 表在 PA02–PA04、PA06–PA09、PA11、PA20、PA31、PA37、PA39–PA44 等标注了 `!DBG_DO0…15`、`!DBG_CLK`（片上调试追踪观测）以及 `#ACTEST0/1`、`#DCTEST0/1`（ATE/工厂测试）、`#AUD_CLK_EXT`（外部音频时钟）。
- 规格书 Table 5-2 的「Function」列仅列外设复用，**不含上述调试/测试观测信号**。
- **结论**：属不同类别（片上可观测性/测试），非外设复用冲突；PINMUX 表补充了这些标记，规格书未枚举，二者不矛盾。
- 📝 **裁定（用户确认）**：此类标记**仅作记录备查，原理图评审不涉及**（不影响硬件原理图检查）。

### 差异 4：括号备选功能 `(JDI_*)`、`(PWR_KEY)` 规格书未列或命名不同

- PINMUX 表在 PA06/08/39/40/41 列 `(JDI_EXTCOMIN)`、`(JDI_SO)`、`(JDI_SCLK)`、`(JDI_SCS)`、`(JDI_DISP)`，PA34 列 `(PWR_KEY)`。
- 规格书 Table 5-2 对 PA39–PA41 列的是 `LCDC1_JDI_VCK/XRST/HCK` 等（Sel#6/7），**未列上述括号 JDI 备选名**；PA34 未列 `PWR_KEY`。
- ✅ **裁定（用户确认）含义**：
  - **`(JDI_*)` = 串行 JDI 屏接口信号**，属于 **LCD 类别**的串行 JDI 显示接口（JDI_EXTCOMIN / JDI_SO / JDI_SCLK / JDI_SCS / JDI_DISP），与规格书 `LCDC1_JDI_*` 为同一 LCD 接口的别名/备选命名。
  - **`(PWR_KEY)` = PA34 上带的默认硬件功能**：长按强制复位芯片（**默认阈值约 10s**，可由 **PWRKEY_CNT** 配置至最大值约 100+s），属纯硬件行为、**无禁用位**；其余时间该引脚仍可作普通 GPIO / ADC。52 系列要把 PA34 当 GPIO 使用须配 PWRKEY_CNT 最大值并约束高电平保持 < 50s，详见 [[DR_PA34_PowerKey_GPIO]]。
- 结论：PINMUX 表补充了 JDI 接口的备选命名与电源键功能，规格书表项较简，二者不矛盾，建议以 PINMUX 表为准并在原理图中核对 JDI 引脚用途。

### 差异 5：PA21 引出差异（系列相关，非功能冲突）

- PINMUX 表含 PA21（Func0=`GPIO_A21`，通用分配组 I2C_UART/TIM），QFN68 列标记为 `*`。
- 规格书：DS5202（3.3V）PA21 = pin24（正常引出）；DS5201（电池）PA21 行引脚号标记为 `‐`（**无封装引脚**，电池系列 pin24 = VCC）。
- **结论**：PINMUX 表覆盖 3.3V 系列完整 45 GPIO；电池系列无 PA21，设计电池系列板时 PA21 行不可用。

### 规格书与 PINMUX 表一致的部分（已核对）

- 所有 PA 的 **Func0 默认 = GPIO_Ax**、**Func4 = PA_I2C_UART（通用 I2C/UART）**、**Func5 = PA_TIM（通用 TIM）** 两组通用分配在规格书与 PINMUX 表完全一致。
- SPI1/SPI2、I2S1、MPI2/SD1、PDM1、LCDC1_8080、USB11、XTAL32K、WKUP、EFUSE 等专用复用的引脚归属在两者间一致（除差异 4 的 JDI 备选名外）。

## 8. 裁定结论备查（原「待核实」已按用户确认全部裁定）

- 差异 1 GPADC 通道号：**以规格书 CH0–CH6 为准**，第 3 节总表已更正（PINMUX 原表 CH1–CH7 为 +1 偏移，弃用）。
- 差异 2 USART1 Debug UART：**以 PINMUX 表为准**（PA18/PA19）；缺失原因 = ROM 软件设置 UART，不在硬件 default 中。
- 差异 3 调试/测试标记（`!DBG_*` / `#ACTEST*` / `#DCTEST*` / `#AUD_CLK_EXT`）：**仅记录，原理图评审不涉及**。
- 差异 4 JDI/PWR_KEY：`(JDI_*)` = 串行 LCD 接口信号（与规格书 `LCDC1_JDI_*` 同一接口别名）；`(PWR_KEY)` = PA34 默认硬件 10s 长按复位（软件可配时长），含义已澄清，与规格书不矛盾。
