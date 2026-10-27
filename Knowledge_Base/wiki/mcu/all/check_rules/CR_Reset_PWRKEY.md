---
title: CR-PWRKEY复位引脚(PA34)处理
type: mcu_check_rule
aliases: ["CR_Reset_PWRKEY","PWRKEY复位审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-一般"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 一般
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
校验 SF32LB52X 电源按键（PWRKEY，对应引脚 PA34）电路，避免误触发 PWRKEY 复位。默认持续高 >10s 复位，长按阈值可由 **PWRKEY_CNT** 配置至最大值约 100+s；57 系列 PA34 的 PWRKEY 可由 **PMUC WER.PWRKEY=0** 关闭（见 [[DR_PA34_PowerKey_GPIO]]）。

## 核心硬件内容（背景）
芯片复位源含板级 **PWRKEY 复位**：若电源按键 PA34 持续高电平超过 10 秒，发生 PWRKEY 复位（除 RTC 与 IWDT 外所有模块复位）。标志可通过 PMUC WSR_PWRKEY 查询、WCR_PWRKEY 清除。详见 [[DR_Reset_Design]]、[[SF32LB52x_batt|SF32LB52x]] §7。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到 PA34 用作电源按键或连接外部上拉/控制逻辑时，核对高电平持续时长风险与按键去抖/释放设计。
2. **违规现象描述**：① PA34 被错误永久上拉至高（无按键即持续高）且 >10s 触发意外复位；② 按键电路无释放/滤波，长按误触发复位；③ 将 PA34 复用为 GPIO 却未考虑 PWRKEY 复位功能冲突。
3. **风险影响说明**：意外 PWRKEY 复位 → 设备频繁重启/无法稳定运行（一般）。
4. **标准化整改方案**：电源按键须经可靠下拉与按键闭合上拉，确保常态为低、仅在按压时高；软件侧合理处理或屏蔽；复用 PA34 时评估 PWRKEY 复位影响。
5. **知识库溯源依据**：[[SF32LB52X_UserManual_V0.8.8]] P20（2.2.1 板级复位源）；[[SF32LB52x_batt|SF32LB52x]] §7 复位系统。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜设计规范：[[DR_Reset_Design]]｜PA34 作 GPIO 规范：[[DR_PA34_PowerKey_GPIO]]｜报告模板：[[index_MCU_ALL]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P20（复位源，PWRKEY 持续高>10s）

## 待核实问题
- nRST 外部复位标准电路图手册未给出，待补参考设计。
