---
title: CR-参考设计-外设接口电平匹配VDDIOA
type: mcu_check_rule
aliases: ["CR_RefDesign_Interface_VoltageMatch","接口电平匹配审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_3V3_Reference_Schematic],[SF32LB52x_batt_Reference_Schematic],[SF32LB52_Peripheral_GPIO]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族","SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SF32LB52 官方参考设计，校验 **所有外设接口信号电平是否与 VDDIOA 一致**：LCD / I2C / SPI / UART / GPS / 4G / HR / MIC 等接口电压必须等于 VDDIOA（1.8V 或 3.3V）；eMMC 接口电压须匹配 VDDIOA；4G/GPS 模块电平=3.3V 时 PA_26_LS_EN 不需要。高于 VDDIOA 直连会损伤 IO（升级为致命）。

## 核心硬件内容（背景）
- VDDIOA 支持 1.8V 与 3.3V；参考设计反复标注「接口电压必须和 VDDIOA 保持一致」「GPIO 接口电平是 3.3V，所有外设的电平必须匹配」「外部 Flash 接口电压必须是 3.3V」。
- 模块电平转换 IC 使能由 **PA_09_LH_EN** 控制；4G/GPS 模块接口电平为 3.3V 时，其电平转换使能 **PA_26_LS_EN 不需要**。
- 越级电压（如 5V 信号直连 3.3V IO）属 [[CR_AbsMaxRatings]] 范畴，可致 IO 永久损伤。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 解析到外设接口（LCD/I2C/SPI/UART/GPS/4G/HR/MIC/eMMC）连接 MCU GPIO 时，核对器件供电域与 VDDIOA 是否一致。
2. **违规现象描述**：
   - 外设 VCC 与 VDDIOA 不一致（如 VDDIOA=1.8V 但外设为 3.3V，或反之）且无电平转换；
   - 5V 信号直连 MCU GPIO（超 ABS MAX，致命）；
   - eMMC 接口电压与 VDDIOA 不匹配；
   - 4G/GPS 模块=3.3V 时仍保留 PA_26_LS_EN 电平转换电路（多余/可省）。
3. **风险影响说明**：电平不匹配 → 通信失败/IO 闩锁或永久损伤（严重；超压为致命）。
4. **标准化整改方案**：外设与 MCU 选同压域，或用电平转换 IC（PA_09_LH_EN 控）；核对 VDDIOA 取值（1.8/3.3V）；模块=3.3V 时去掉 PA_26_LS_EN。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_GPIO]]；参考设计两页（接口电压匹配注释）。

## 关联页面
- GPIO：[[SF32LB52_Peripheral_GPIO]]｜绝对最大额定值：[[CR_AbsMaxRatings]]｜GPIO 默认态：[[CR_GPIO_Default_PUPD]]

## 原始来源完整引用
1. [SF32LB52X_3V3-Reference-SCH-V1.0.0_20251015.pdf] / [SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]，Raw：raw/mcu/ref_design/，设计注释（接口电压必须和 VDDIOA 一致、外部 Flash 接口电压必须 3.3V、4G/GPS 3.3V 时 PA_26_LS_EN 不需要）

## 待核实问题
- 无（参数来自参考设计黄金样板）。
