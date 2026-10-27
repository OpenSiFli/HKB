---
title: CR-参考设计-外挂存储供电控制(PA21/PA11)
type: mcu_check_rule
aliases: ["CR_RefDesign_ExternalFlash_Power","外挂存储供电控制审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_3V3_Reference_Schematic],[SF32LB52x_batt_Reference_Schematic],[SF32LB52_Peripheral_Memory]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族","SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SF32LB52 官方参考设计，校验**外挂存储（Nor / SPI Nand / SD Nand Flash、合封 SiP）的供电控制 GPIO 选择与常供电判定**是否符合黄金样板：3.3V 系列 SiP(VDD_SIP) 由 **PA21** 控制、外挂 Nand(VDD_MEM) 由 **PA11** 控制；电池系列无 PA21，Nand/外部 Flash 统一由 **PA11**（默认 PU）控制。

## 核心硬件内容（背景）
- **3.3V 系列（SF32LB52X，有 PA21）**：
  - 合封/SiP Flash 的 VDD_SIP（pin23）外部供电使能 → **PA21**。
  - 外挂 SPI Nand / SD Nand 的 VDD_MEM → **PA11**（MPI2_VDD_EN/SD_VDD_EN，默认 PU）。
- **电池系列（SF32LB52x，无 PA21）**：无外部 VDD_SIP 引脚，外挂 Nand/SD Nand 的 VDD_MEM → **PA11**（默认 PU）。
- **常供电判定（按存储介质）**：
  - **Nor Flash**：自身可进 Deep Power Down（≈1µA）。MPI 外接 **≤16MB** Nor 可常供电；**≥32MB** Nor 须由 PA21 可控断电。
  - **SPI Nand / SD Nand Flash**：自身无深度掉电机制，待机功耗高，**必须由 GPIO 控制供电**（3.3V 系列 VDD_MEM→PA11；电池系列→PA11）。
- **Hibernate 关机**：必须能关断存储供电（3.3V 系列 VDD_SIP→PA21；外挂 Nand→PA11），否则不可进入 Hibernate 或会持续漏电。
- 外部 Flash 与 eMMC **二选一**；双 Nor 方案 Flash1 CS=PA12、Flash2 CS=PA26。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 解析到 VDD_SIP / VDD_MEM / 外部 Flash 供电网络由 GPIO 控制或常开时触发。
   - 触发对象：网络 `VDD_SIP`、`VDD_MEM`、`VDD_3V3`(Flash 支线)；GPIO `PA21`、`PA11`、`PA12`、`PA26`。
2. **违规现象描述**：
   - 电池系列原理图出现 **PA21** 控制存储供电（该系列无 PA21，规则无效）；
   - 外挂 **SPI Nand / SD Nand** 常供电未受 GPIO 控制 → 待机漏电/失效；
   - **≥32MB Nor** 未受 PA21 控制且设计用 Hibernate → 漏电；
   - 控制 GPIO 非 PA21/PA11（如误用其他非默认 PU 脚，启动早期电平不确定）。
3. **风险影响说明**：存储供电失控 → Hibernate/待机漏电、电池快速耗尽、存储数据丢失或无法启动（严重）。
4. **标准化整改方案**：
   - 3.3V 系列：SiP VDD_SIP 使能接 **PA21**；外挂 Nand VDD_MEM 使能接 **PA11**。
   - 电池系列：外挂 Nand/Flash VDD_MEM 使能接 **PA11**（默认 PU，复位早期维持确定电平）。
   - Nor ≤16MB 可常供电；Nand/SD Nand 必须受控；需 Hibernate 时必须受控断电。
5. **知识库溯源依据**：[[SF32LB52X_3V3_Reference_Schematic]]、[[SF32LB52x_batt_Reference_Schematic]]；[[SF32LB52_Peripheral_Memory]] §4.1；[[CR_Hibernate_SiP_Supply]]。

## 关联页面
- 存储外设：[[SF32LB52_Peripheral_Memory]]｜Hibernate 规则：[[CR_Hibernate_SiP_Supply]]｜GPIO 默认态：[[CR_GPIO_Default_PUPD]]
- 电源：[[SF32LB52_Peripheral_Power]]｜芯片实体：[[SF32LB52X]]、[[SF32LB52x_batt]]

## 原始来源完整引用
1. [SF32LB52X_3V3-Reference-SCH-V1.0.0_20251015.pdf]，Raw：raw/mcu/ref_design/SF32LB52X_3V3/，设计注释（Nor≥32MB 用 PA21、Nand 用 PA11、Hibernate 必须控）
2. [SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]，Raw：raw/mcu/ref_design/SF32LB52x_batt/，设计注释（电池系列 PA11 控 VDD_MEM、Nor 可常供、Nand 必须控）

## 待核实问题
- 无（参数来自参考设计黄金样板）。
