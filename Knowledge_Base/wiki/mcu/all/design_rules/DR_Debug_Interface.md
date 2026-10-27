---
title: DR-调试接口设计规范(SF32LB52X)
type: mcu_design_rule
aliases: ["DR_Debug_Interface","SF32LB52X调试接口设计规范"]
tags: ["企业MCU","通用设计规范","调试/下载","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_USB]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
SF32LB52X 调试接口（SWD=PA18/PA19；UART 调试=USART1，PA18 RX/PA19 TX，默认 1M/8N1）的设计规范，保障产测/返修可调试且不损伤 IO。

## 核心硬件内容
### 1. 规范主题与适用范围
- 主题：调试接口引脚保留、电平兼容、ESD 防护、低功耗可重连。
- 适用：原理图调试接口、测试点、产线工装设计。

### 2. 设计要求
- 保留 PA18(SWDIO, 默认 PU)/PA19(SWCLK, 默认 No Pull) 测试点或串阻，避免外部固定电平冲突默认态。
- UART 调试经 USART1，上电默认开启，默认 1M 波特/8 数据/1 停止/无校验，监听自定义调试帧并自动经 DMAC1 专用通道读写总线。
- 调试走线加 ESD/TVS 防护（产线插拔）。
- 低功耗设计须保证唤醒后可重连调试（HPSYS 从 deepsleep/standby 唤醒且 ISSR_HP_ACTIVE=1 后调试器可重连）。

### 3. 约束禁忌
- 不可将 PA18/PA19 强上拉/强下拉或接固定电平导致 SWD/UART 调试失效。
- 进入 deepsleep/standby/hibernate 或重映射 PA18/PA19、复位 DMAC1 会导致调试断开（见 [[FC_DebugInterface_Failure]]）。

### 4. 规范依据
- [[SF32LB52X_UserManual_V0.8.8]] §4.2.6（P57）、§15.7–15.10（P341–P363）；[[SF32LB52x_batt|SF32LB52x]] §10。

## 关联页面
- USB/调试外设：[[SF32LB52_Peripheral_USB]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 校验规则：[[CR_DebugInterface_PA18_PA19]]
- 故障案例：[[FC_DebugInterface_Failure]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，§4.2.6（P57）、§15.7–15.10（P341–P363）

## 待核实问题
- 外部调试连接器（如 4-pin SWD、测试点间距）企业规范若未定义，建议补充。
