---
title: SF32LB57 USB 2.0 Full-Speed
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_USB","SF32LB57 USB","SF32LB57 USB2.0"]
tags: ["企业MCU","外设-USB","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 集成 **1× USB 2.0 Full-Speed**（§3.5.8），片内 PHY。**两系列一致**。

## 1. 主要特性
- **1× USB2.0 FS**（Full-Speed，12Mbps）
- 片内集成 PHY
- ⚠️ 本册（V0.2）**未说明是否支持 Host/Device/OTG** 及是否为 USB-C 相关特性，待补用户手册。

## 2. 引脚
⚠️ **USB DP/DM 的具体引脚号本册 Table 5-3 未单列**（在 GPIO PA 复用表中）。SF32LB52 家族为 PA35/PA36，**禁止直接套用到 57 家族**，须以 [[SF32LB57_Pinmux]] / 用户手册为准。

## 3. 硬件设计约束
- **DP/DM 为差分对**，须做 **90Ω 差分阻抗控制**、**等长走线**，并远离射频（BRF_ANT）、Buck 开关节点与晶体。
- **禁止外接独立 USB 收发器**（片内已集成 PHY）。
- USB 走线下方保持完整参考地平面，避免跨分割。
- 若用作 Device，VBUS 检测与 CC/ID（若 USB-C）按方案需求设计；ESD 保护器件须靠近 USB 座放置且结电容满足 FS 信号完整性要求。
- 电池系列若由 VBUS(21) 同时承担充电输入，须注意 USB VBUS 与充电输入的共用与保护设计。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- GPIO/复用：[[SF32LB57_Peripheral_GPIO]]、[[SF32LB57_Pinmux]]
- 电源：[[SF32LB57_Peripheral_Power]]｜串口：[[SF32LB57_Peripheral_Serial]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，§3.5.8 USB2.0 FS（P21）；产品特性「1×USB2.0FS」（P5）。
2. [DS5701-SF32LB57x V0.2]，同上（P21 / P5）。

## 待核实问题
1. **USB DP/DM 引脚号**未在本册专用引脚表中列出，待补 Pinmux / 用户手册；**禁止套用 SF32LB52 的 PA35/PA36**。
2. Host / Device / OTG 角色支持情况未说明。
3. 是否需外接 VBUS 检测分压、USB-C CC 逻辑，待补参考设计。
