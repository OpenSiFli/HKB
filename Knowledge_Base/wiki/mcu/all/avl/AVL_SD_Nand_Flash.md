---
title: SD Nand Flash 认证物料（SIFLI MCU AVL V0.4）
type: mcu_avl
doc_type: avl
category: SD Nand Flash
mcu_family: ["通用-所有SIFLI MCU"]
applicability: ["所有SIFLI MCU系列（含SF32LB52X/SF32LB52x及后续型号）"]
tags: ["AVL合格物料","BOM合规校验","物料选型标准","SIFLI-MCU-AVL-V0.4"]
source_version: "V0.4 (2026-08-12)"
created: 2026-08-12
updated: 2026-08-12
---

# SD Nand Flash 认证物料（SIFLI MCU AVL V0.4）

> **适用范围**：本表为 SIFLI 全系列 MCU 合格物料（AVL），**不限于 SF32LB52 系列**，适用于所有 SIFLI MCU 型号。具体适配以对应芯片手册 / 硬件设计指南为准。
> **来源**：`raw/mcu/all_chip/avl/SIFLI-MCU-AVL-认证表-V0.4-20260812.xlsx` → Sheet「SD Nand Flash list」。版本 V0.4（2026-08-12）。
> **优先级**：AVL 企业标准 > 外围器件原厂规格书。

## 分类说明
SD2.0 接口 Nand（嵌入式 SDIO），须外部控制供电。

## 物料清单（共 5 条）

| 序号 | 型号 | 厂家 | 容量 | 温度范围 | 工作电压 | 接口协议 | 最快时钟 | Standby电流 | Operation电流 | 下载工具支持 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CSNP1GCR01-BOW | CS | 1Gb | -30 ~ 85℃ | 2.7 ~ 3.6V | SD2.0 | 50MHz | 150uA TYP | 15mA/50MHz TYP |  |
| 2 | XTSD01GLGEAG | XTX | 1Gb | -30 ~ 85℃ | 2.7 ~ 3.6V | SD2.0 | 50MHz | 200uA MAX | 30mA/50MHz MAX |  |
| 3 | XSSD01GGAI | XSS | 1Gb | 0 ~ 70℃ | 2.7 ~ 3.6V | SD2.0 | 50MHz | 300uA MAX | 45mA/50MHz MAX |  |
| 4 | MKDV1GCL-AB | MK | 1Gb | -25~ 85℃ | 2.7 ~ 3.6V | SD2.0 | 50MHz | 50uA MAX | 28mA/50MHz MAX |  |
| 5 | XS26D01GACW | Icthink | 1Gb | -25~ 85℃ | 2.7 ~ 3.6V | SD2.0 | 50MHz | 250uA MAX | 100mA/50MHz MAX |  |

## 备注
- 每行物料以 AVL 表格「认证型号 / 序号」为准；参数冲突以 AVL 企业标准优先。
- 本表为跨系列共享资源；新增 MCU 家族可直接引用并按功能筛选适配型号。
