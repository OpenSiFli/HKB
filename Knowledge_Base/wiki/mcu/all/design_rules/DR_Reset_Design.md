---
title: DR-复位源设计规范(SF32LB52X)
type: mcu_design_rule
aliases: ["DR_Reset_Design","SF32LB52X复位设计规范"]
tags: ["企业MCU","通用设计规范","复位/电源","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
SF32LB52X 复位源（POR/BOR/PWRKEY/VBAT 欠压/IWDT/WDT1/WDT2/软件/唤醒）的设计规范，指导外部复位电路与看门狗配置。

## 核心硬件内容
### 1. 规范主题与适用范围
- 主题：复位源分类与作用域、外部复位/电源按键电路、看门狗。
- 适用：最小系统复位设计与可靠性。

### 2. 设计要求
- **板级复位**：POR（上电）、BOR（欠压，BOR_EN 可关）、**PWRKEY（PA34；默认持续高 >10s 复位除 RTC/IWDT 外，长按阈值可由 PWRKEY_CNT 配置至最大值约 100+s；57 系列可经 PMUC WER.PWRKEY=0 关闭，见 [[DR_PA34_PowerKey_GPIO]]）**、VBAT 欠压。
- **看门狗**：IWDT（全局）、WDT1（HPSYS，WER_WDT1=1 可扩大至全局）、WDT2（LPSYS）。
- **软件**：Reboot（PMUC CR_REBOOT 写1）、HCPU/LCPU SYSRESETREQ、模块 RCC RSTRx。
- 复位标志查询/清除：WSR_*/WCR_*（PWRKEY/IWDT/WDT1/WDT2/LOWBAT 等）。

### 3. 约束禁忌
- PWRKEY 引脚（PA34）须可靠下拉，避免常态高导致意外复位；52 系列长按阈值默认约 10s、最大可配至 ~100+s（见 [[DR_PA34_PowerKey_GPIO]]），57 系列可关闭 PWRKEY 功能。
- 外部复位标准电路图手册未给出，设计需待补参考设计核实（待核实）。
- 多看门狗作用域不同，关键系统建议启用 IWDT 全局保护。

### 4. 规范依据
- [[SF32LB52X_UserManual_V0.8.8]] §2.2（P20–P22，表 2-1/2-2）；[[SF32LB52x_batt|SF32LB52x]] §7。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜电源：[[SF32LB52_Peripheral_Power]]
- 校验规则：[[CR_Reset_PWRKEY]]、[[CR_Reset_Levels]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，§2.2（P20–P22）

## 待核实问题
- nRST 外部复位标准电路图手册未给出，待补 SiFli 参考设计。
