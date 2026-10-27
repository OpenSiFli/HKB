---
title: LCD 驱动（LCD Driver） 认证物料（SIFLI MCU AVL V0.4）
type: mcu_avl
doc_type: avl
category: LCD 驱动（LCD Driver）
mcu_family: ["通用-所有SIFLI MCU"]
applicability: ["所有SIFLI MCU系列（含SF32LB52X/SF32LB52x及后续型号）"]
tags: ["AVL合格物料","BOM合规校验","物料选型标准","SIFLI-MCU-AVL-V0.4"]
source_version: "V0.4 (2026-08-12)"
created: 2026-08-12
updated: 2026-08-12
---

# LCD 驱动（LCD Driver） 认证物料（SIFLI MCU AVL V0.4）

> **适用范围**：本表为 SIFLI 全系列 MCU 合格物料（AVL），**不限于 SF32LB52 系列**，适用于所有 SIFLI MCU 型号。具体适配以对应芯片手册 / 硬件设计指南为准。
> **来源**：`raw/mcu/all_chip/avl/SIFLI-MCU-AVL-认证表-V0.4-20260812.xlsx` → Sheet「LCD driver list」。版本 V0.4（2026-08-12）。
> **优先级**：AVL 企业标准 > 外围器件原厂规格书。

## 分类说明
显示驱动 IC（含 AMOLED / LCD），接口含 MIPI / QSPI / DBI 等。

## 物料清单（共 1 条）

| 序号 | 型号 | 厂家 | 分辨率 | 类型 | IO电压 | 接口 | GRAM | Color | 最快速率SDR | 最快速率DDR |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RM69090 | Raydium | 368*448 | AMOLED | 1.65 ~ 3.3V | MIPI,QSPI | Y | 16.7M | ?MHz | 不支持 |

## 备注
- 每行物料以 AVL 表格「认证型号 / 序号」为准；参数冲突以 AVL 企业标准优先。
- 本表为跨系列共享资源；新增 MCU 家族可直接引用并按功能筛选适配型号。
