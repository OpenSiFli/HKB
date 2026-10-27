---
title: SF32LB52 外设-存储接口(MPI/SDMMC)
type: mcu_periph
aliases: ["SF32LB52X MPI","SF32LB52X SDMMC","SF32LB52X 存储接口"]
tags: ["企业MCU","外设模块-存储接口","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52x_Datasheet_V0.2.6],[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Datasheet_V2.5.5]]
mcu_family: ["SF32LB52"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
series_applicability: ["通用-两系列共用"]
created: 2026-08-10
updated: 2026-08-11
---

## 摘要

> **适用系列**：本外设为 SF32LB52X（电池供电）与 SF32LB52x（3.3V 供电）两系列**共用**；两系列外设逻辑一致，差异仅在电源架构与电源专用引脚（见 [[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_GPIO]]）。
SF32LB52X 存储接口：MPI（Memory Peripheral Interface，支持 SiP QSPI-NOR/NAND、OPI-PSRAM、HyperRAM 等，最高 144MHz）与 SDMMC（SD3.0/SDIO3.0/eMMC4.51，最高 48MHz）。本页整理外部存储电路约束与引脚映射。

## 核心硬件内容
### 1. MPI（§3.8.1，P26–P27）
- 支持 SPI NOR/NAND Flash（1/2/4 线，DTR）、pSRAM（x8/x16，Xccela/Legacy）、HyperRAM（x8/x16，HyperBus）。
- 两种模式：寄存器模式 / 地址映射模式（XIP，支持 On-The-Fly AES128/256-CTR 解密）。
- SiP 存储随型号：8/32Mb NOR-Flash 或 32/64/128Mb pSRAM（Table 5-7）。
- 外部扩展引脚（复用组 MPI2 / SD1）：PA12~PA17（MPI2_CS/DIOx/CLK、SD1_DIOx/CLK/CMD，Sel#=1/2）。

### V2.5.5 订购型号与 SiP 存储（Table 5-7，P51）
- V2.5.5 官方订购码及内置存储：
  - `SF32LB520U36`：8Mb NOR Flash
  - `SF32LB523UB6` / `SF32LB523LUB6`：32Mb OPI-pSRAM
  - `SF32LB525UC6`：64Mb OPI-pSRAM
  - `SF32LB527UD6`：128Mb OPI-pSRAM
- 命名体系变更：V2.5.5（520/523/525/527）与 V0.2.6（52BU36 等 6 款）不同，跨版本映射待核实（见芯片实体待核实 #2）。
- SiP 接口频率（V2.5.5 确认）：NOR-Flash 最高 96MHz（DTR）；OPI-PSRAM 最高 144MHz（Table 3-1 / Features）。

### 2. SDMMC（§3.8.2，P27）
- 兼容 SD Host 3.0 / SDIO 3.0 / eMMC 4.51；SDR12/25/50；SDR 1/4 线；不支持 DDR；内置 21K 字节 FIFO。
- 复用组 SD1（PA12~PA17）。

### 3. 接口速率（Table 3-1，P28）
- MPI1：SiP OPI-PSRAM 144MHz / SiP QSPI-NOR 96MHz(DTR)
- MPI2：外部 QSPI-NOR/NAND 96MHz
- SDMMC：外部 eMMC 48MHz

### 4. 约束禁忌
- 外部 QSPI/SD 走线需控制阻抗与等长（尤其 DQS/时钟），并注意电源完整性。
- SiP 型号已内置存储，外部 MPI2/SDMMC 仅用于扩展；不可与 SiP 地址冲突。
- VDD_SIP（引脚23）须按 SiP 存储规格供电。

### 4.1 外挂存储供电控制（PA21 / 默认 PU GPIO）
- **PA21（仅 3.3V 系列 SF32LB52X，pin24）主要用途**：给**外挂 Flash 存储做电源控制**（驱动外部电源开关/LDO 使能，不用时断电或 hibernate 下关断防漏电）。
- **存储介质类型决定是否需要 GPIO 控制供电**：
  - **Nor Flash**：待机/关机时可自身进入 **Deep Power Down（DPD）模式**，电流约 **1µA** → Nor Flash **可常供电**，不必用 GPIO 切其供电电源（无需断电即可低功耗）。
  - **SPI Nand Flash / SD Nand Flash**：自身无深度掉电省电机制 → **必须控制其供电电源**（通过 PA21 或等效 GPIO 在不用时断电）才能降到低功耗。
- **电池系列（SF32LB52x）无 PA21**：外挂存储供电控制可选用**默认是 PU（上拉）的 GPIO** 驱动电源开关使能；选默认 PU 的 GPIO 可在 MCU 复位/启动早期（固件接管前）维持确定电平、避免误上电或漏电。
- **认证料号选型（全系列通用 AVL）**：Nor Flash 见 [[AVL_Nor_Flash]]；SPI Nand Flash 见 [[AVL_SPI_Nand_Flash]]；SD Nand Flash 见 [[AVL_SD_Nand_Flash]]（均汇总于 [[SIFLI_MCU_AVL_V0.4_20260812|SIFLI MCU AVL V0.4]]，适用于所有 SIFLI MCU 型号）。
- 关联：SiP 合封存储 VDD_SIP 的 hibernate 防漏电规则（3.3V 系列）见 [[CR_Hibernate_SiP_Supply]]、[[FC_Hibernate_SiP_Leakage]]、[[DR_LowPower_IO_Retention]]。

### 5. 规范依据
- Datasheet §3.8 Memory Interfaces（P26–P27）、Table 3-1（P28）、Table 5-2（PA12~PA17，P51–P52）、Table 5-3（VDD_SIP 23，P47）、Table 5-7（P50）

## 用户手册 V0.8.8 补充（SDMMC 与 MPI2 互斥 / FIFO）
来源：[[SF32LB52X_UserManual_V0.8.8]] §14（P339–P342）。

- **SDMMC 与 MPI2 复用 PA12~PA17**：二者共用 IO，使用 SDMMC 功能时**不能**通过 MPI2 访问外部 Flash（互斥）。原理图/固件须避免同时启用。详见 [[CR_SDMMC_MPI2_Exclusive]]。
- SDMMC 内置 **2KB FIFO**；支持 SD3.0/SDIO3.0/eMMC4.51，SDR 单线/4 线（不支持 DDR、不支持 SPI）；CLK 由 HCLK 分频（CLKCR_DIV，最小分频比 2）。
- eMMC 某些状态 CMD 线需开漏模式（CDR_CMD_OD=1），访问 SD/SDIO 或 eMMC 其它状态须改回推挽。
- FIFO 上/下溢会产生 SR_FIFO_OVERRUN/UNDERRUN；可设 CLKCR_VOID_FIFO_ERROR 在 FIFO 不足时自动停 CLK。详见 [[FC_SDMMC_FIFO_Overflow]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 电源：[[SF32LB52_Peripheral_Power]]｜GPIO：[[SF32LB52_Peripheral_GPIO]]
- 校验规则：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.8（P26–P27）、Table 3-1（P28）、Table 5-2（P51–P52）
2. [DS5201-SF32LB52x-Datasheet V2p5p5.pdf]，Raw：raw/mcu/all_chip/datasheets/DS5201-SF32LB52x-Datasheet V2p5p5.pdf，Table 3-1（P29）、Table 5-7 订购信息（P51）

## 待核实问题
- 外部 QSPI/SD 具体端接电阻、等长与时序约束待补参考设计/Layout 指南。
