---
title: DR-电源架构设计规范(SF32LB52X)
type: mcu_design_rule
aliases: ["DR_PowerArchitecture","SF32LB52X电源设计规范"]
tags: ["企业MCU","通用设计规范","电源","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_Power]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
SF32LB52X 多电源域（常规供电版 + 锂电供电版）的电源架构设计规范：明确各电源引脚取值、BUCK 不可旁路、输出 LDO 默认态、MIC_BIAS 与合封存储供电控制，支撑原理图取电设计与审图。

## 核心硬件内容
### 1. 规范主题与适用范围
- 主题：芯片供电架构、外部取电、内部电源树、电源域隔离。
- 适用：SF32LB52X 全部型号原理图电源设计。两大家族：常规供电版（52A/52B/52D/52E/52G/52J）、锂电供电版（523/525/527）。

### 2. 设计要求
- **常规版**：PVDD(19)=1.8/3.3V、VDDIOA(21)=1.8/3.3V、AVDD33(14)/AVDD33_AUD(38)/AVDD_BRF(52)=3.3V；VDD_SIP(23) 按 SiP 存储规格（PVDD=1.8V 时 VDD18_LDO 无法出 1.8V，须外供且关闭 VDD18_LDO）。
- **锂电版**：VBUS(5V)/VBAT(4V)/VCC(4V) 体系；VSYS(3.3V) 内部出给 AVDD_BRF；VDD33_VOUT1(3.3V, BOOT ROM 自动开启)；VDD33_VOUT2(3.3V, 默认关闭)；内置 560mA 充电，满电 4.2~4.45V。
- **BUCK（FB/LX）不可旁路、不可被外部 LDO 替代**；启动后自动开启、hibernate 后自动关闭。
- VDD33_VOUT2 默认关闭，需软件（PERI_LDO）开启；MIC_BIAS(40) 默认关闭，需 AUDCODEC 寄存器开启调压。
- 各电源域加去耦（具体容值待补参考设计）。

### 3. 约束禁忌
- 任一电源缺失/超绝对最大值（+3.63V / ‑0.3V）→ 功能异常或永久损伤（致命）。
- PVDD/VDDIOA 取值须核对订购型号（1.8 或 3.3V）。
- 合封存储外部供电须由 PA21 控制以防 hibernate 漏电（**仅适用于 3.3V 系列 SF32LB52X；电池系列 SF32LB52x 无 PA21**，须以其他可控方式关断外部 SiP 供电，见 [[DR_LowPower_IO_Retention]]、[[CR_Hibernate_SiP_Supply]]）。
- EPAD(69) 必须可靠接 GND。

### 4. 规范依据
- [[SF32LB52X_UserManual_V0.8.8]] §3（P39–P46，表 3-1/3-2、PMUC 寄存器）；原厂 Datasheet Table 4-1/4-2、Table 5-3、Table 5-7。

## 关联页面
- 电源外设：[[SF32LB52_Peripheral_Power]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 校验规则：[[CR_PowerDomains]]、[[CR_AbsMaxRatings]]、[[CR_EPAD_GND]]、[[CR_VBATS_Range]]、[[CR_Hibernate_SiP_Supply]]
- 低功耗：[[DR_LowPower_IO_Retention]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，§3（P39–P46）
2. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 4-1/4-2、5-3、5-7

## 待核实问题
- 各电源域推荐去耦电容容值、Buck 电感与反馈电阻具体值手册未列，待补 SiFli 参考原理图（raw/mcu/ref_design/）。
