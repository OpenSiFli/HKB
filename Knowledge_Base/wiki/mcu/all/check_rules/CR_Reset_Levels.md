---
title: CR-复位引脚电平阈值
type: mcu_check_rule
aliases: ["CR_Reset_Levels","复位电平审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_Datasheet_V0.2.6]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-10
updated: 2026-08-10
---

## 摘要
校验 SF32LB52X 复位电路输出的释放/复位电平是否满足 IO 特性阈值（释放 ≥0.7×VDD、复位 ≤0.3×VDD），确保可靠上电复位与手动复位。

## 核心硬件内容（背景）
I/O 特性（Table 4-3/4-4）：nRST 释放电压 VIH_nRST≥0.7×VDD，复位电压 VIL_nRST≤0.3×VDD。复位电路设计须保证上电与手动复位时电平跨越阈值干净、无毛刺。详见 [[SF32LB52x_batt|SF32LB52x]] 最小系统章节（复位细节 datasheet 未给图，待核实）。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 SF32LB52X 复位网络（nRST，复用/专用复位引脚）时，检查复位源（上电复位电路、手动复位按键、看门狗）输出电压是否满足阈值，是否有上拉/滤波。
2. **违规现象描述**：复位释放电平 <0.7×VDD（如弱上拉不足导致高电平不够）；复位有效电平 >0.3×VDD；复位线无滤波/无上拉导致毛刺误复位。
3. **风险影响说明**：阈值不满足 → 上电不启动或随机复位（严重）。
4. **标准化整改方案**：复位线加合适上拉（参考内部 PU/PD 7~20kΩ@3.3V）与去抖 RC；手动复位按键正确接地；确认 VDD 域与复位电平参考一致。
5. **知识库溯源依据**：[[SF32LB52x_batt|SF32LB52x]] 最小系统；Datasheet Table 4-3/4-4（P29–P30）。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜GPIO：[[SF32LB52_Peripheral_GPIO]]｜电源：[[SF32LB52_Peripheral_Power]]
- 同类规则：[[CR_AbsMaxRatings]]、[[CR_FloatingIO_LowPower]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 4-3/4-4（P29–P30）

## 待核实问题
- 复位引脚具体编号与标准复位电路图 datasheet 文本未给出，待补 SiFli 参考设计（raw/mcu/ref_design/）。
