---
title: CR-GPIO上电默认上下拉处理
type: mcu_check_rule
aliases: ["CR_GPIO_Default_PUPD","GPIO默认上下拉审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-一般"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_GPIO]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 一般
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
校验 SF32LB52X 各 GPIO 上电默认上下拉（PE 默认=1）在原理图/固件中被合理处理，避免默认态与外部电路冲突或低功耗漏电。

## 核心硬件内容（背景）
上电后 IO 默认存在上拉或下拉（PE=1），须软件配置为所需状态。部分引脚默认态：PA03/PA11/PA12=PU、PA18=PU(SWDIO)、PA19=No Pull(SWCLK)，其余多为 PD。详见 [[SF32LB52_Peripheral_GPIO]] §默认上下拉、[[DR_GPIO_DefaultPUPD_HighZ]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到某 GPIO 连接外部固定电平/外设使能/按键/总线时，核对上电默认 PU/PD 是否与外部电路期望一致。
2. **违规现象描述**：① 外部电路要求默认高却在内部默认下拉（或反之）导致上电瞬间误动作；② 关键使能脚因默认上下拉在启动前被错误激活；③ 低功耗下未处理默认态导致悬空漏电/功耗升高。
3. **风险影响说明**：默认态冲突 → 上电误触发/外设误使能/漏电流升高（一般）。
4. **标准化整改方案**：核对 Table 5-1 默认态；对敏感脚外部加确定电平或软件尽早配置；低功耗不用的输入脚配置确定电平或上下拉。
5. **知识库溯源依据**：[[SF32LB52X_UserManual_V0.8.8]] P66–P68（表 5-1 默认 PU/PD）；[[SF32LB52_Peripheral_GPIO]]。

## 关联页面
- GPIO：[[SF32LB52_Peripheral_GPIO]]｜设计规范：[[DR_GPIO_DefaultPUPD_HighZ]]、[[DR_LowPower_IO_Retention]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P66–P68（表 5-1）

## 待核实问题
- 完整 45 脚默认态以手册表 5-1 为准；本规则引用典型引脚，审图时须逐脚核对。
