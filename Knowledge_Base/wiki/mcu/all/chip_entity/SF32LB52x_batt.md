---
title: SF32LB52x
type: mcu_chip
aliases: ["SF32LB52x 电池系列","SF32LB52x(电池供电)","SiFli SF32LB52x"]
tags: ["企业MCU","芯片系列-SF32LB52","型号-SF32LB52x 电池系列","芯片实体","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52x_Datasheet_V2.5.5],[SF32LB52X_UserManual_V0.8.8]]
mcu_family: ["SF32LB52"]
mcu_series: ["电池供电系列"]
mcu_model: ["SF32LB520U36","SF32LB523UB6","SF32LB525UC6","SF32LB527UD6","SF32LB523LUB6"]
hardware_version: ["QFN68L","Datasheet V2.5.5","UserManual V0.8.8"]
created: 2026-08-12
updated: 2026-08-12
---

## 摘要
SiFli **SF32LB52x（小写 x）= 电池供电系列**，一颗面向 AIoT 的超低功耗双核 MCU（big.LITTLE Arm Cortex-M33 STAR-MC1，HCPU@240MHz / LCPU@24MHz），集成双模 BT5.3、2D/2.5D GPU、576KB SRAM，QFN68L 封装、**共 44 GPIO（无 PA21）**。**内置 560mA 锂电线性充电器**，电源专用引脚为 **VBUS / VBAT / VSYS / VCC**，主电 VBAT 3.2~4.7V（单节锂电）。适用于由单节锂电供电的可穿戴、便携 AIoT、智能传感等场景。

> 本页为 **SF32LB52x 电池供电系列** 实体总页。同家族另有 **SF32LB52X（大写 X）3.3V 供电系列**（无充电电路、主电 PVDD、GPIO 由 VDDIOA 供电），见 [[SF32LB52X]]；两系列共用用户手册，家族总览见 [[SF32LB52]]。
>
> 📌 **文档来源**：本电池系列由 **DS5201-SF32LB52x**（标题小写 x）描述，与芯片命名（小写 x=电池）一致；3.3V 系列由 **DS5202-SF32LB52X**（标题大写 X）描述，与芯片命名（大写 X=3.3V）一致。文档标题大小写与芯片系列**一致**，不存在反转。

## 核心硬件内容

### 1. 芯片基础
- 厂商 / 系列：SiFli（思澈科技）/ SF32LB52x 电池供电系列（52 家族）
- 内核：Arm Cortex-M33 STAR-MC1 ×2（big.LITTLE）
  - HCPU：最高 240MHz，32KB I-Cache + 16KB D-Cache，512KB SRAM（全保持）
  - LCPU：最高 24MHz，64KB SRAM（全保持）
- 存储资源：片上 SRAM 共 576KB（HPSYS 512KB + LPSYS 64KB）；SiP 存储随型号（8/32Mb NOR-Flash 或 32/64Mb pSRAM）
- 订购型号（DS5201 V2.5.5 订购表）：SF32LB520U36 / SF32LB523UB6 / SF32LB525UC6 / SF32LB527UD6 / SF32LB523LUB6
- 封装：QFN68L，7×7×0.85mm，0.35mm pitch，含散热裸焊盘 EPAD（引脚 69）
- 工作温度：‑40 ~ +85 °C
- 无线：双模 BT5.3（BLE/BR/EDR），BLE 灵敏度 ‑100dBm(1Mbps)，最大 Tx 19dBm(BR/BLE)/13dBm(EDR)
- 内置电源：高效率 Buck + 多路 LDO + **560mA 锂电线性充电电路（VBUS → VBAT）**

### 2. 引脚分配
**GPIO（Big Core 域 PA00–PA44 中**无 PA21**，共 44 个，I/O 可复用）** — 完整引脚号与复用见 [[SF32LB52_Peripheral_GPIO]]（PA 复用矩阵与 3.3V 系列仅 PA21 不同：本系列 pin24 为电源引脚 VCC、无 PA21；差异仅在电源专用引脚与 PA21 是否存在）。

**专用引脚 —— 电池系列电源 / RF / 模拟 / IO（DS5201 Table 5-3）**
| 引脚号 | 名称 | 类型 | 说明 |
|------|------|------|------|
| 21 | VBUS | PWR | 充电 / 系统输入（USB 5V），4.6~5.5V |
| 20 | VBAT | PWR | 锂电电源输出（给系统供电），3.2~4.7V |
| 19 | VSYS | PWR | 系统电源输出（PMU 后） |
| 24 | VCC | PWR | 系统电源输入（3.2~4.7V） |
| 18 | BUCK_LX | A,I/O | Buck 电感开关节点 |
| 17 | BUCK_FB | PWR | Buck 输出反馈（内部 1.25V） |
| 16 | VDD_VOUT1 | PWR | 内部 LDO1 输出（HPSYS，1.1V） |
| 15 | VDD_VOUT2 | PWR | 内部 LDO2 输出（LPSYS，0.9V） |
| 22 | VDD33_VOUT1 | PWR | 3.3V LDO 输出 1 |
| 14 | VDD33_VOUT2 | PWR | 3.3V LDO 输出 2 |
| 23 | VDD18_VOUT | PWR | SiP 存储电源（1.8V） |
| 13 | VDD_RET | PWR | RET LDO 输出（内部 0.7V） |
| 12 | VDD_RTC | PWR | RTC LDO 输出（内部 1.1V，hibernate 保持） |
| 68 | GPADC_VREF | A,I | GPADC 参考电压输入 |
| 55/54 | XTAL48M_XI/XO | A,I / A,O | 48MHz 晶振端口 |
| 53 | BRF_ANT | A,I/O | 天线接口（片上集成 Balun） |
| 52 | AVDD_BRF | PWR | RF 电源输入 2.97~3.63V |
| 41 | ADCP | A,I | 音频 ADC 输入 |
| 40 | MIC_BIAS | PWR | 麦克风偏置输出（1.4~2.8V, 0~2mA，默认关闭需软件开启） |
| 39 | AUD_VREF | A,I | 音频参考电压输入 |
| 38 | AVDD33_AUD | PWR | 音频电源输入 2.97~3.63V |
| 37/36 | DACP / DACN | A,O | 音频 DAC 差分输出 |
| 69 | EPAD | GND | 散热裸焊盘，须接 GND |

> 本系列**外部无独立 VDDIOA 引脚**（3.3V 系列的 pin21=VDDIOA 在本系列为 VBUS）；片内 VDDIOA 在芯片内部直接连到 **VSYS** 引脚，GPIO IO 域由 VSYS 经内部 VDDIOA 供电（IO 电平跟随 VSYS≈3.3V）。已确认，无需核对 UM5201。如系统需外部 3.3V 独立 IO 供电，应选同家族 3.3V 系列 [[SF32LB52X]]。

### 3. 极限电气参数（Absolute Maximum Ratings，DS5201 Table 4-2）
- VBUS：0 ~ +5.5V
- VBAT / VCC：0 ~ +4.7V
- VIN（I/O 输入）：0 ~ VIO+0.3V
- 存储温度：‑40 ~ +125 °C
- RF 输入（VLNA）：0 dBm（max）
- 输入电流 IIN：20 mA
- ESD：HBM ±4000V（JS-001）、CDM ±1000V（JS-002）；Latch-up：I-Test ±200mA、OVT +1.5×VddMAX

### 4. 推荐工作条件（DS5201 Table 4-1）
- VBUS：4.6（Min）~ 5（Typ）~ 5.5V（Max）
- VBAT / VCC：3.2 ~ 4.7V
- 工作温度：‑40 ~ +25 ~ +85 °C

### 5. I/O 特性（Table 4-3 @3.3V；电池系列另 Table 4-19 四档驱动 DS1/DS0）
- 输入高 / 低：VIH≥0.7×VDDIOA，VIL≤0.3×VDDIOA
- **输出驱动（两系列相同）**：3.3V 系列 DS5202 V0.2.6 文本为 @3.3V 最大 12/30/38mA（min/typ/max），测试条件 **VOH=0.8×VDDIO**；电池系列 DS5201 V2.5.5 Table 4-19 可配置四档 2/4/8/12mA（DS1/DS0），测试条件 **VOH=0.9×VDDIO**。**两系列驱动能力完全相同**，为同一驱动电路在两种 VOH 测试条件下的结果，并非不同能力。
- 内部上 / 下拉电阻：@3.3V 7/10/20 kΩ
- 输入电容 CIN：2.5~3.5 pF
- nRST 释放 / 复位电压：VIH_nRST≥0.7×VDD，VIL_nRST≤0.3×VDD

### 6. 电源架构与充电（电池系列，DS5201 + 用户手册 V0.8.8 表 3-2）
**电池供电版（SF32LB52x）**：外部 **VBUS**(21, 4.6~5.5V) → 内置 **560mA 线性充电器** → **VBAT**(20, 3.2~4.7V) 给单节锂电；VBAT 经 PMU 出 **VSYS**(19)、**VCC**(24) 给系统；Buck（BUCK_LX 18 / BUCK_FB 17，1.25V）下游 LDO 出 VDD_VOUT1(16, HPSYS 1.1V) / VDD_VOUT2(15, LPSYS 0.9V) / VDD_RET(13, 0.7V)；VDD33_VOUT1(22) / VDD33_VOUT2(14) 出 3.3V 给 AVDD_BRF(52) / AVDD33_AUD(38)；VDD18_VOUT(23) 给合封 Flash/PSRAM；VDD_RTC(12, 1.1V) hibernate 保持。

**充电器全参数（DS5201 Table 4-18）**
| 参数 | 符号 | 最小值 | 典型值 | 最大值 | 单位 |
|------|------|------|------|------|------|
| 充电输入电压 | Vbus | 4.6 | 5 | 5.5 | V |
| 恒流充电电流 | Icc | 5 | — | 560 | mA |
| 充满终止电压 | Vcv | 4.2 | — | 4.45 | V |
| 充满电压精度 | — | ±1.5% of Vcv | | | |
| 再充电阈值 | Vrechg | Vcv−0.15 | | | V |

> 充满后充电回路自动断开进入 Charger Full 模式；电池电压跌至 Vcv−0.15V 自动再充电。VBUS 须满足 4.6~5.5V（典型 USB 5V），超 5.5V 触发 AbsMax 风险。详见 [[SF32LB52_Peripheral_Power]]、[[DR_PowerArchitecture]]。

### 7. 复位系统（用户手册 V0.8.8，表 2-1/2-2）
四类复位源（与 3.3V 系列一致，因共用用户手册）：
- **板级复位**：POR（上电）、BOR（欠压，BOR_EN 可关）、PWRKEY（**PA34；默认持续高 >10s** 复位除 RTC/IWDT 外模块，长按阈值可由 PWRKEY_CNT 配置至最大值约 100+s，见 [[DR_PA34_PowerKey_GPIO]]）。
- **看门狗**：IWDT（全局）、WDT1（HPSYS）、WDT2（LPSYS）。
- **软件**：Reboot、HCPU/LCPU SYSRESETREQ、模块 RCC RSTRx。
- **唤醒复位**：Hibernate 唤醒 / HPSYS·LPSYS Standby 唤醒。
> nRST 外部复位标准电路图手册未以原理图给出（仅描述源），待补 SiFli 参考设计。详见 [[DR_Reset_Design]]、[[CR_Reset_PWRKEY]]。

### 8. BOOT 启动配置（用户手册 V0.8.8，P91）
BOOT 模式由 **HPSYS_CFG BMR 寄存器 Bit0** 决定：**0=正常模式，1=下载模式**。本系列 BOOT 主要为**寄存器配置**，非纯外部引脚 strapping。详见 [[DR_BootMode]]、[[CR_BootMode_Register]]。

### 9. 低功耗模式与电压（用户手册 V0.8.8，表 4-2）
active/sleep → deepsleep → standby → hibernate 五级（与 3.3V 系列一致，VDD_VOUT1/VDD_RET/VDD_RTC 电压相同）：
| 模式 | VDD_VOUT1 | VDD_RET | VDD_RTC |
|------|------|------|------|
| active/sleep | 1.0/1.2V | 0.7V | 1.1V |
| deepsleep | 0.7V | 0.7V | 1.1V |
| standby | 0V | 0.7V | 1.1V |
| hibernate | 0V | 0V | 1.1V（仅 PMUC/RTC/IWDT 工作） |
> deepsleep/standby 下除 PA24~PA27 外的输出 IO 不可翻转；hibernate 下 IO 高阻、唤醒 PIN 可保持上下拉（配置在 RTC 寄存器）。详见 [[DR_LowPower_IO_Retention]]。

### 10. 最小系统硬件规范（要点）
- **电源（电池版）**：VBUS(21) 接 USB/适配器 5V，经充电器给 VBAT 锂电；VBAT/VCC 取电满足 3.2~4.7V；Buck 不可旁路；EPAD 接 GND。详见 [[SF32LB52_Peripheral_Power]]。
- **时钟**：主时钟片内 48MHz 晶振（XTAL48M_XI/XO，引脚 55/54）；可选 32.768kHz 低速晶振（PA22/PA23 或 XTAL32K_EXT）。详见 [[SF32LB52_Peripheral_Clock]]。
- **复位**：复位源见 §7；nRST 外部电路图待补参考设计。
- **BOOT**：寄存器 BMR 配置（§8），下载模式经调试接口。
- **下载/调试**：SWD = PA18(SWDIO, 默认 PU) + PA19(SWCLK, 默认 No Pull)；UART 调试经 USART1（PA18 RX / PA19 TX，默认 1M/8N1）。详见 [[SF32LB52_Peripheral_USB]]、[[DR_Debug_Interface]]、[[CR_DebugInterface_PA18_PA19]]。

### 11. 全外设硬件要求（摘要，详细见各外设页）
- GPIO：[[SF32LB52_Peripheral_GPIO]]（44 GPIO、无 PA21、默认 PU/PD、高阻处理、开漏、中断配置）
- GPADC：[[SF32LB52_Peripheral_GPADC]]（12-bit/4Msps）
- 串口：[[SF32LB52_Peripheral_Serial]]（**UART×3**（UART1/2/3，HPSYS，应用可用）/ I2C×4 / SPI×2；⚠️ 规格书所列 UART4/5 位于 LPSYS，仅为蓝牙 HCI 调试接口，正常开发不可用）
- 音频接口：[[SF32LB52_Peripheral_I2S_PDM]]（I2S×1 / PDM×1）
- 音频模拟：[[SF32LB52_Peripheral_Audio]]（24-bit DAC/ADC、MIC_BIAS、AUD_VREF）
- 无线：[[SF32LB52_Peripheral_BLE_RF]]（片上 Balun）
- 存储接口：[[SF32LB52_Peripheral_Memory]]（MPI QSPI/OPI、SDMMC 与 MPI2 复用 PA12~PA17）
- 定时器/PWM：[[SF32LB52_Peripheral_Timer_PWM]]（GPTIM/ATIM/BTIM/LPTIM）
- 显示/GPU：ePicasso 2.5D GPU、LCD 控制器（DBI 8080/SPI、JDI）—— 详见 datasheet §2 / §3.5

### 12. 约束禁忌（使用限制与量产风险）
- **VBUS 输入范围**：必须 4.6~5.5V（典型 USB 5V）；严禁超过 AbsMax 5.5V。
- **VBAT 锂电范围**：3.2~4.7V；单节锂电直接接 VBAT，禁止并联多芯或超压。
- **充电电流 / 散热**：560mA 恒流为上限，须按电池容量与 PCB 散热留余量；充满自动截止。
- **低功耗浮空输入**：使能输入的数字 IO 若悬空，低功耗电流升高 → 必须配置确定电平。
- **GPADC 源电阻**：外部信号源电阻须满足采样时间上限（12-bit 时 RAIN 最大 5000kΩ@慢采样，最快 1kΩ@4 TPCLK）。
- **多电源域**：任一处电源缺失 / 超范围导致功能异常或永久损伤。
- **BRF_ANT（53）**：片上集成 Balun 与天线匹配，通常无需片外匹配网络。
- **EPAD（69）**：散热裸焊盘必须可靠接 GND。
- **USB DP/DM（PA35/PA36）**：差分对，片内 PHY，禁止外接独立收发器；需做阻抗 / 等长。
- **外挂存储供电控制（无 PA21）**：本电池系列**无 PA21**，不适用「PA21 控制存储供电」规则（该规则仅适用于 3.3V 系列 SF32LB52X，见 [[CR_Hibernate_SiP_Supply]]）。若使用外挂存储需控制供电，**选用 PA11（MPI2_VDD_EN/SD_VDD_EN，默认 PU）** 驱动电源开关使能即可（参考设计黄金样板，见 [[SF32LB52x_batt_Reference_Schematic]]、[[CR_RefDesign_ExternalFlash_Power]]）；另注意 **Nor Flash 自身可进 Deep Power Down（≈1µA），可常供电、无需断电**，仅 **SPI Nand / SD Nand Flash 才必须控制供电电源**。
- **SDMMC 与 MPI2 互斥**：共用 PA12~PA17，启用 SDMMC 时不能通过 MPI2 访问外部 Flash。
- **BOOT 模式**：误置 BMR[0]=1 会进入下载模式，量产固件须确保正常模式。

## 关联页面
- 家族总览：[[SF32LB52]]｜3.3V 系列实体：[[SF32LB52X]]
- 来源摘要：[[SF32LB52x_Datasheet_V2.5.5]]、[[SF32LB52X_UserManual_V0.8.8]]
- 硬件设计指南（电池系列）：[[SF32LB52x_batt_Hardware_Design_Guide]]（1:1 PDF：[[raw/mcu/all_chip/hw_design/SF32LB52x_batt_HW_Application.pdf]]）
- 外设：[[SF32LB52_Peripheral_GPIO]]、[[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_Clock]]、[[SF32LB52_Peripheral_GPADC]]、[[SF32LB52_Peripheral_BLE_RF]]、[[SF32LB52_Peripheral_USB]]、[[SF32LB52_Peripheral_Serial]]、[[SF32LB52_Peripheral_Audio]]、[[SF32LB52_Peripheral_Memory]]、[[SF32LB52_Peripheral_Timer_PWM]]、[[SF32LB52_Peripheral_I2S_PDM]]
- 设计规范：[[DR_PowerArchitecture]]、[[DR_GPIO_DefaultPUPD_HighZ]]、[[DR_LowPower_IO_Retention]]、[[DR_Reset_Design]]、[[DR_Debug_Interface]]、[[DR_BootMode]]
- 故障案例：[[FC_I2C_BusStuck]]、[[FC_DebugInterface_Failure]]、[[FC_Hibernate_SiP_Leakage]]、[[FC_SDMMC_FIFO_Overflow]]
- 校验规则：`wiki/mcu/all/check_rules/` 下 CR_* 系列（见 [[index_MCU_ALL]]）

## 原始来源完整引用
1. [DS5201-SF32LB52x-Datasheet V2p5p5.pdf]，Raw：raw/mcu/all_chip/datasheets/DS5201-SF32LB52x-Datasheet V2p5p5.pdf，Table 4-1~4-19（P29 起）、Table 5-2（GPIO）、Table 5-3（P47 专用引脚）、订购表（P50）、Table 4-18 充电特性（P38）
2. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，V0.8.8：电源架构 P39–P46、复位 P20–P22、低功耗 P54–P57、BOOT P91、GPIO P64–P68、I2C P138、ATIM P192、音频 P277–P307、SDMMC P339–P342、调试 P341/P362–P363

## 待核实问题
1. 用户手册为寄存器 / 编程型，**未提供** PCB 布局、EMC、ESD、浪涌、安规等独立硬件设计规范，也无最小系统参考原理图、BOOT 外部 strapping 电路图、nRST 外部复位电路图；此类内容需补 SiFli 参考设计（raw/mcu/ref_design/），禁止编造。
2. 电池系列 GPIO IO 域由内部 VDDIOA→VSYS 供电、外部无 VDDIOA 引脚（已确认，无需核对 UM5201）。
3. 是否已存在独立 errata 勘误手册，建议放入 raw/mcu/all_chip/errata/ 后补充勘误页。
4. 订购型号 520/523/525/527（+LUB6）与 3.3V 系列 52B/D/E/G/J 及用户手册 52A/B/D 命名体系映射待核对。
5. 大量电气 / 引脚表为位图，pypdf 无法提取数值，需 OCR / 人工核对，禁止编造。
