---
title: CR-ATIM刹车输入(BKIN)可靠性
type: mcu_check_rule
aliases: ["CR_ATIM_Break_BKIN","ATIM刹车审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-致命"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_Timer_PWM]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 致命
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
校验 SF32LB52X ATIM 高级定时器驱动的功率电路，其刹车输入 BKIN/BKIN2 连接可靠，确保故障快速关断到安全态。

## 核心硬件内容（背景）
ATIM 含 6 路互补 PWM + 死区，适用于电机/半桥驱动。两路断路输入 **BKIN/BKIN2** 通常接功率级/三相逆变器故障输出；激活时关闭 PWM 输出并强制预定义安全态。BDTR_BKE/BKE2 使能、BDTR_BKP/BKP2 选极性；ATIM 复位后断路默认禁止、BDTR_MOE 低。详见 [[SF32LB52_Peripheral_Timer_PWM]] §9.1.3.14。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到 ATIM PWM 输出驱动功率桥/电机（含栅极驱动、半桥、三相逆变）时，核对 BKIN/BKIN2 是否连接功率级故障信号并有可靠拉电平。
2. **违规现象描述**：① BKIN/BKIN2 悬空或未连接故障检测；② 故障信号无滤波/无确定电平导致误触发或失效；③ 功率级故障输出与 BKIN 极性（BDTR_BKP）未匹配；④ 未使能断路（BDTR_BKE=0）即投入功率运行。
3. **风险影响说明**：刹车不可靠 → 桥臂直通/过流烧毁功率器件甚至起火（致命）。
4. **标准化整改方案**：BKIN/BKIN2 接功率级故障输出并加 RC 滤波与确定上下拉；软件使能断路并正确配置极性；建议启用 AF1_LOCK 写保护冻结安全参数。
5. **知识库溯源依据**：[[SF32LB52X_UserManual_V0.8.8]] P192（9.1.3.14 紧急断路）；[[SF32LB52_Peripheral_Timer_PWM]]。

## 关联页面
- 定时器/PWM：[[SF32LB52_Peripheral_Timer_PWM]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜设计规范：[[index_MCU_ALL]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P192（§9.1.3.14）

## 待核实问题
- ATIM 各 PWM/BKIN 通道与具体 GPIO 引脚映射（Sel#=5）待补 PINMUX 表。
