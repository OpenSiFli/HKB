---
title: SF32LB52X 用户手册 V0.8.8（中文）
type: mcu_source
aliases: ["UM5201-SF32LB52x-CN","SF32LB52x用户手册"]
tags: ["企业MCU","芯片系列-SF32LB52","型号-SF32LB52家族","用户手册","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52x_batt|SF32LB52x]]
mcu_family: ["SF32LB52"]
mcu_model: ["SF32LB52BU36","SF32LB52BU56","SF32LB52DUB6","SF32LB52EUB6","SF32LB52GUC6","SF32LB52JUD6","SF32LB523","SF32LB525","SF32LB527"]
hardware_version: ["QFN68L","V0.8.8"]
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
SiFli（思澈科技）**UM5201-SF32LB52x-CN V0.8.8**（中文用户手册，371 页），覆盖 SF32LB52X 家族全硬件板块：电源架构（常规供电版 + 锂电供电版完整电源树）、时钟与复位源、低功耗模式、BOOT 模式、GPIO 默认上下拉与高阻处理、调试接口（SWD + UART 调试）、全外设（GPIO/UART/I2C/SPI/I2S/PDM/ADC/DAC/Audio/SDMMC/MPI/BLE/ATIM 等）寄存器级描述、典型连接（数字麦克风）、蓝牙共存接口。本手册是寄存器/编程型手册，**不含**独立的 PCB 布局/EMC/ESD 设计规范与 BOOT 外部 strapping 电路图（相关项见芯片实体页与 check_rules「待核实」）。服务于全量检索、原理图审图、PCB 校验、故障分析、评审报告。

## 核心硬件内容（手册提取要点）
1. **电源架构**：常规供电版（52B/52E/52G/52J）主电 PVDD=1.8/3.3V、IO 电 VDDIOA=1.8/3.3V、模拟 AVDD33/AVDD_BRF/AVDD33_AUD=3.3V、合封存储 VDD_SIP；锂电供电版（523/525/527）主电 VCC/VBAT/VBUS，内置 560mA 线性充电。片内 BUCK（FB/LX）不可旁路、不可被外部 LDO 替代；VDD33_VOUT1 由 BOOT ROM 自动开启，VDD33_VOUT2 默认关闭；MIC_BIAS 默认关闭需软件开启。详见 [[SF32LB52_Peripheral_Power]]、[[DR_PowerArchitecture]]。
2. **复位源**：板级（POR/BOR/PWRKEY 即 PA34 持续高 >10s/VBAT 欠压）、看门狗（IWDT/WDT1/WDT2）、软件（Reboot/HCPU·LCPU sysreset/模块 RCC）、唤醒（Hibernate/Standby 唤醒）。详见 [[DR_Reset_Design]]、[[CR_Reset_PWRKEY]]。
3. **BOOT 模式**：由 HPSYS_CFG **BMR 寄存器 Bit0** 决定（0=正常模式，1=下载模式），专用 boot mode 地址 0xFFA57200；并非纯引脚 strapping。详见 [[DR_BootMode]]、[[CR_BootMode_Register]]。
4. **低功耗**：active/sleep/deepsleep/standby/hibernate 五级；配套电源管脚电压表（Table 4-2）；deepsleep/standby 下 PA24~PA27 外输出 IO 不可翻转；hibernate 下 IO 高阻、仅 PMUC/RTC/IWDT 工作；合封存储外部供电须由 PA21 控制以防 hibernate 漏电。详见 [[DR_LowPower_IO_Retention]]、[[CR_Hibernate_SiP_Supply]]。
5. **GPIO 默认上下拉**：上电后 IO 默认存在上拉/下拉（PE 默认=1），须软件配置；默认态部分引脚 PU/PD 见 Table 5-1（如 PA18=PU、PA19=No Pull）。详见 [[SF32LB52_Peripheral_GPIO]]、[[CR_GPIO_Default_PUPD]]、[[DR_GPIO_DefaultPUPD_HighZ]]。
6. **调试接口**：SWD=PA18/PA19；UART 调试经 USART1（默认 PA18 RX / PA19 TX，1M 波特、8N1），上电默认开启并监听自定义调试帧。低功耗/IO 重映射/DMAC1 异常会导致调试失效。详见 [[SF32LB52_Peripheral_USB]]、[[DR_Debug_Interface]]、[[CR_DebugInterface_PA18_PA19]]、[[FC_DebugInterface_Failure]]。
7. **外设约束/故障**：I2C 总线电气干扰会卡死（恢复流程见 7.1.3.12）；ATIM 6 路互补 PWM 含 BKIN/BKIN2 紧急断路保护功率开关；SDMMC 与 MPI2 复用 PA12~PA17（互斥）；BLE 共存 4 线接口（BT_ACTIVE/BT_PRIORITY/BT_COLLISION/WLAN_ACTIVE）。详见 [[SF32LB52_Peripheral_Serial]]、[[SF32LB52_Peripheral_Timer_PWM]]、[[SF32LB52_Peripheral_Memory]]、[[SF32LB52_Peripheral_BLE_RF]]、[[FC_I2C_BusStuck]]、[[CR_ATIM_Break_BKIN]]、[[CR_SDMMC_MPI2_Exclusive]]。

## 章节页码索引（供溯源）
- 产品特性/封装：P5（QFN68L、44 GPIO、内置 Buck+LDO、两路 3.3V@150mA、休眠 2uA、560mA 锂电充电、VBAT 3.2~4.7V、VBUS 4.6~5.5V）
- 时钟与复位：P20–P22（复位源、表 2-1/2-2 复位域）、P54–P57（低功耗模式与电压表 4-2、调试器行为）
- 电源架构：P39–P46（锂电版表 3-1、常规版表 3-2、PMUC 寄存器、BUCK/ LDO）
- BOOT/系统配置：P91（HPSYS_CFG BMR/IDR/SYSCR）
- GPIO：P64–P68（IO 选择、高阻、输出/输入、表 5-1 默认 PU/PD、HPSYS_GPIO 寄存器）
- I2C 总线恢复：P138（7.1.3.12）
- ATIM 紧急断路/6 步 PWM：P192（9.1.3.14/15）
- 音频 PDM/Codec：P277–P278、P295、P307（数字麦克风典型连接、时钟、Audcodec 供电/时钟）
- 存储 SDMMC：P339–P342（与 MPI2 复用 IO、FIFO、开漏模式）
- 调试接口：P341（地址映射）、P362–P363（UART 调试、失效原因、数据共存）
- 蓝牙共存：P364–P368（BT_ACTIVE/PRIORITY/COLLISION/WLAN_ACTIVE、天线共用射频开关）

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 规格书来源：[[SF32LB52X_Datasheet_V0.2.6]]
- 外设/规则/案例：见 [[index_MCU_ALL]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，文档编号 UM5201‐SF32LB52x‐CN，V0.8.8，©2025 思澈科技（南京）有限公司；关键章节页码见上。

## 待核实问题
1. 手册为寄存器/编程型，**未提供**独立的 PCB 布局、EMC、ESD、浪涌、安规硬件设计规范，也无最小系统参考原理图与 BOOT 外部 strapping 电路图；此类内容需补 SiFli 参考设计（raw/mcu/ref_design/）后再入库，禁止编造。
2. 常规供电版型号补充：手册出现 SF32LB52A/52B/52D 与锂电版 SF32LB523/525/527，与 datasheet 订购表（BU36/BU56/DUB6/EUB6/GUC6/JUD6）命名体系不同，需核对内部型号映射关系（待核实）。
3. 外部复位（nRST）引脚与标准复位电路图手册未以原理图给出，仅描述复位源；待补参考设计。
