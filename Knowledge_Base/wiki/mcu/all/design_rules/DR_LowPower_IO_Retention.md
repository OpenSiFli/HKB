---
title: DR-低功耗IO保持与合封供电控制规范
type: mcu_design_rule
aliases: ["DR_LowPower_IO_Retention","低功耗IO保持设计规范"]
tags: ["企业MCU","通用设计规范","低功耗/电源","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_Power]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
SF32LB52X（**3.3V 系列**，有 PA21）低功耗模式（deepsleep/standby/hibernate）下 IO 保持、唤醒 PIN 上下拉、合封存储外部供电（PA21）控制的设计规范，防止漏电与唤醒失效。**注意：电池系列 SF32LB52x 无 PA21，PA21 控制 SiP 供电一段仅适用于 3.3V 系列；电池系列须以其他可控方式关断外部 SiP 供电。**

## 核心硬件内容
### 1. 规范主题与适用范围
- 主题：低功耗模式 IO 状态、唤醒源、hibernate 漏电防护。
- 适用：低功耗/电池供电产品设计。

### 2. 设计要求
- 低功耗模式电源管脚电压（HPSYS，表 4-2）：active/sleep VDD_VOUT1=1.0/1.2V；deepsleep=0.7V；standby=0V；hibernate 全 0V（仅 VDD_RTC=1.1V 保持）。
- deepsleep/standby 下除 **PA24~PA27** 外的输出 IO 不可翻转（保持进入前电平）；hibernate 下 IO 高阻，唤醒 PIN 可保持上下拉（配置在 RTC 寄存器，不丢失）。
- **合封存储外部供电须由 PA21 控制**：hibernate 下 PA21 高阻，外部下拉关断电源开关；退出后 PA21 输出高开启供电。若外部供电不可关断，应避免 hibernate。
- 低功耗不用的输入脚配置确定电平或上下拉，避免悬空漏电。

### 3. 约束禁忌
- 误用 hibernate 且合封存储外部供电不可关断 → 持续漏电、电池耗尽（严重）。
- 唤醒 PIN 若依赖 GPIO 上下拉但配置在错误寄存器，hibernate 下会丢失 → 无法唤醒。

### 4. 规范依据
- [[SF32LB52X_UserManual_V0.8.8]] §4.2（P54–P57，表 4-2）、§3.2（P42，合封 IO 漏电）；[[SF32LB52x_batt|SF32LB52x]] §9。

## 关联页面
- 电源：[[SF32LB52_Peripheral_Power]]｜GPIO：[[SF32LB52_Peripheral_GPIO]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 校验规则：[[CR_Hibernate_SiP_Supply]]、[[CR_FloatingIO_LowPower]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，§4.2（P54–P57）、§3.2（P42）

## 待核实问题
- 无。
