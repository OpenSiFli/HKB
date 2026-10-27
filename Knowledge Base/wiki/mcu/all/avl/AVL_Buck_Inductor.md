---
title: Buck 电感（Buck Inductor） 认证物料（SIFLI MCU AVL V0.4）
type: mcu_avl
doc_type: avl
category: Buck 电感（Buck Inductor）
mcu_family: ["通用-所有SIFLI MCU"]
applicability: ["所有SIFLI MCU系列（含SF32LB52X/SF32LB52x及后续型号）"]
tags: ["AVL合格物料","BOM合规校验","物料选型标准","SIFLI-MCU-AVL-V0.4"]
source_version: "V0.4 (2026-08-12)"
created: 2026-08-12
updated: 2026-08-12
---

# Buck 电感（Buck Inductor） 认证物料（SIFLI MCU AVL V0.4）

> **适用范围**：本表为 SIFLI 全系列 MCU 合格物料（AVL），**不限于 SF32LB52 系列**，适用于所有 SIFLI MCU 型号。具体适配以对应芯片手册 / 硬件设计指南为准。
> **来源**：`raw/mcu/all_chip/avl/SIFLI-MCU-AVL-认证表-V0.4-20260812.xlsx` → Sheet「Buck inductor list」。版本 V0.4（2026-08-12）。
> **优先级**：AVL 企业标准 > 外围器件原厂规格书。

## 分类说明
片内 Buck 转换器功率电感，典型 4.7uH。选型须满足 L / DCR / Isat / Irms / SRF 要求。

## 物料清单（共 8 条）

| 序号 | 电感 | 关键参数要求 | 认证型号 | 厂家 | 类型 | 电感值<br>L | 误差<br>Tolerance | 最小谐振频率<br>SRF | 直流阻抗<br>DCR | 饱和电流<br>Isat | 额定电流<br>Irms | 封装 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 4.7uH | L(电感值) = 4.7uH ± 20%，<br>DCR(直流阻抗) ≦ 0.4 ohm，<br>Isat(饱和电流) ≧ 450mA | WPN201610U4R7MT | Sunlord | 绕线 | 4.7uH | ±20% | 21MHz | 288 mohm max | 1.3A | 1.45A | 0806（2016 公制） |
| 2 |  |  | WPN201610H4R7MT | Sunlord | 绕线 | 4.7uH | ±20% | 25MHz | 425 mohm max | 1.2A | 1.0A | 0806（2016 公制） |
| 3 |  |  | HTTX20161T-4R7MDR | CYNTEC | 绕线 | 4.7uH | ±20% |  | 250mohm max | 1.7A | 1.5A | 0806（2016 公制） |
| 4 |  |  | VLS201612CX-4R7M-1 | TDK | 绕线 | 4.7uH | ±20% | 51MHz | 252mohm max | 0.88A | 1.32A | 0806（2016 公制） |
| 5 |  |  | CIGW201610GL4R7MLE | Samsung | 绕线 | 4.7uH | ±20% |  | 240mohm max | 1.4A | 1.4A | 0806（2016 公制） |
| 6 |  |  | DFE201612E-4R7M=P2 | Murata | 绕线 | 4.7uH | ±20% |  | 252mohm max | 1.8A | 1.2A | 0806（2016 公制） |
| 7 |  |  | SWAI201610H4R7M | 三体微 | 绕线 | 4.7uH | ±20% |  | 390mohm max | 1.3A | 1.05A | 0806（2016 公制） |
| 8 |  |  | FSHJ201610-4R7M | 方磁 | 绕线 | 4.7uH | ±20% |  | 425 mohm max | 1.1A | 0.9A | 0806（2016 公制） |

## 备注
- 每行物料以 AVL 表格「认证型号 / 序号」为准；参数冲突以 AVL 企业标准优先。
- 本表为跨系列共享资源；新增 MCU 家族可直接引用并按功能筛选适配型号。
