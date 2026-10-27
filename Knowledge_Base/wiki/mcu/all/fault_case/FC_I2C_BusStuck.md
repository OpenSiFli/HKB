---
title: FC-I2C总线卡死
type: mcu_fault
aliases: ["FC_I2C_BusStuck","I2C总线卡死故障"]
tags: ["企业MCU","故障案例","根因分析","原理图审图/故障分析/报告输出"]
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
SF32LB52X I2C 总线因电气干扰或设备异常卡死（收发持续失败），本文给出根因、恢复流程与图纸审图拦截规则。

## 核心硬件内容（背景）
- 故障所属电路模块：串行通信（I2C，PA_I2C_UART 复用组 Sel#=4）。
- 相关芯片与硬件版本：SF32LB52X 全型号，用户手册 V0.8.8（§7.1.3.12）。

## 专项业务内容 —— 故障复盘（必填）
1. **失效现象、复现条件**：I2C 发送或接收持续失败，表现为总线卡死；多在电气干扰大、从设备异常或上拉失效时出现。
2. **涉及 MCU 型号、硬件版本**：SF32LB52X 家族（QFN68L），手册 V0.8.8。
3. **根因硬件分析**：开漏总线依赖外部上拉；若上拉电阻失效、从设备挂死拉低 SCL/SDA，或强干扰导致状态机异常，总线无法释放。
4. **短期整改方案、长期设计规避规则**：
   - 恢复：① 复位 I2C 模块（CR_UR 置1 等 100us 后置0）；② 若 BMR_SCL/BMR_SDA 均为1，置 CR_RSTREQ 由 I2C 发送 RCCR_RSTCYC 个时钟周期尝试恢复；③ 若 SCL/SDA 持续为0，检查硬件电路或复位从设备。
   - 规避：每条 I2C 总线 SCL/SDA 加可靠外部上拉至 VDDIOA；多电压域加电平转换；从设备电源稳定。
5. **同类图纸审图拦截规则**：对应 [[CR_I2C_BusStuck]]（I2C 外部上拉缺失）。

## 关联页面
- 串口外设：[[SF32LB52_Peripheral_Serial]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 校验规则：[[CR_I2C_BusStuck]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P138（§7.1.3.12 总线异常恢复）

## 待核实问题
- 推荐上拉阻值（按速率/总线电容）手册未给具体表，按通用 I2C 规范取值并据实测调整。
