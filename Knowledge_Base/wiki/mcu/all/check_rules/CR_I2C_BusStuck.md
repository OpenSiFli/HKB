---
title: CR-I2C总线外部上拉缺失
type: mcu_check_rule
aliases: ["CR_I2C_BusStuck","I2C上拉审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_Serial]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 严重
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
校验 SF32LB52X 各 I2C 总线（SCL/SDA，PA_I2C_UART 复用组 Sel#=4）在原理图中配置外部上拉电阻，避免总线卡死。

## 核心硬件内容（背景）
I2C 为开漏总线，须外部上拉。用户手册 7.1.3.12 指出：电气干扰/设备异常会导致 I2C 卡死（收发持续失败）；若 SCL/SDA 持续为 0，多为上拉失效或从设备挂死。详见 [[FC_I2C_BusStuck]]、[[SF32LB52_Peripheral_Serial]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到芯片 I2C 功能引脚（SCL/SDA）时，核对每个 I2C 总线是否均有上拉电阻至 IO 电源域（VDDIOA）。
2. **违规现象描述**：① SCL 或 SDA 无外部上拉（仅靠内部可选上拉或悬空）；② 上拉电阻接错电源域（非 VDDIOA）导致电平不匹配；③ 多设备总线无合理上拉/无电平转换导致卡死。
3. **风险影响说明**：无/弱上拉 → 总线无法释放、通信失败、系统卡死（严重）。
4. **标准化整改方案**：每条 I2C 总线 SCL/SDA 各加外部上拉（阻值按总线电容与速率，典型 1k~10kΩ 至 VDDIOA）；多电压域加电平转换；保留恢复手段（见 [[FC_I2C_BusStuck]]）。
5. **知识库溯源依据**：[[SF32LB52X_UserManual_V0.8.8]] P138（7.1.3.12 总线异常恢复）；[[SF32LB52_Peripheral_Serial]]。

## 关联页面
- 串口：[[SF32LB52_Peripheral_Serial]]｜故障案例：[[FC_I2C_BusStuck]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P138（§7.1.3.12）

## 待核实问题
- 推荐上拉阻值（按各速率/电容）手册未给具体表，按通用 I2C 规范取值并据实测调整。
