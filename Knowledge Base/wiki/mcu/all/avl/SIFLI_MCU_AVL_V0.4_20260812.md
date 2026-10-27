---
title: SIFLI MCU AVL 认证物料总表（V0.4，全系列）
type: mcu_avl
doc_type: avl
mcu_family: ["通用-所有SIFLI MCU"]
applicability: ["所有SIFLI MCU系列（含SF32LB52X/SF32LB52x及后续型号）"]
tags: ["AVL合格物料","BOM合规校验","物料选型标准","SIFLI-MCU-AVL-V0.4"]
source_version: "V0.4 (2026-08-12)"
created: 2026-08-12
updated: 2026-08-12
---

# SIFLI MCU AVL 认证物料总表（V0.4，全系列）

> **适用范围**：本 AVL 为 **SIFLI 全系列 MCU 的合格物料清单**，**不限于 SF32LB52 系列**，适用于所有 SIFLI MCU 型号（含 SF32LB52X / SF32LB52x 及后续推出的型号）。物料按功能分类，具体适配以对应芯片手册 / 硬件设计指南为准。
> **来源文件**：`raw/mcu/all_chip/avl/SIFLI-MCU-AVL-认证表-V0.4-20260812.xlsx`（原始 Excel，仅读取不修改）。
> **版本**：V0.4，生效日期 2026-08-12，作者 yzli。
> **优先级**：AVL 企业标准 > 外围器件原厂规格书。BOM 选型须从本表选取；非 AVL 物料、禁用物料须经特殊审批方可使用。

## 版本与变更历史

| 日期 | 作者 | 版本 | 修改历史 | 备注 |
|---|---|---|---|---|
| 2023-12-29 | yzli | V0.1 | 初始版本 |  |
| 2025-07-16 | yzli | V0.2 | 增加惠伦和晶威特48M晶体 |  |
| 2026-01-21 | yzli | V0.3 | 增加UCUN Nor Flash:UC25WQ80IB,UC25IQ32A,UC25IQ64A,UC25IQ128A |  |
| 2026-08-12 | yzli | V0.4 | 增加惠伦3SQ3270024 |  |

## 物料分类导航

| 分类 | 物料数 | 说明 | 页面 |
|---|---|---|---|
| 晶体（Crystal） | 18 | 主时钟晶体（以 48MHz 为主） | [[AVL_Crystal]] |
| Buck 电感（Buck Inductor） | 8 | 片内 Buck 转换器功率电感 | [[AVL_Buck_Inductor]] |
| Nor Flash | 44 | 外挂代码/数据存储 Nor Flash（QSPI） | [[AVL_Nor_Flash]] |
| SPI Nand Flash | 18 | 大容量 SPI Nand Flash | [[AVL_SPI_Nand_Flash]] |
| SD Nand Flash | 5 | SD2.0 接口 Nand（嵌入式 SDIO） | [[AVL_SD_Nand_Flash]] |
| LCD 驱动（LCD Driver） | 1 | 显示驱动 IC（含 AMOLED / LCD） | [[AVL_LCD_Driver]] |

> 说明：TP driver list（触摸屏驱动）在当前 V0.4 为空，暂无认证型号，后续版本补充后单独建页。

## 使用约定
- 各分类物料清单见上方「页面」链接；每页均标注来源 Sheet 与行号，便于溯源。
- 物料参数、适配范围以 AVL 表格为准；与器件原厂手册冲突时，以 AVL 企业标准优先，同时保留原厂参数并标注差异。
- 本总表为跨系列共享资源，新增 MCU 家族时无需复制，直接引用本表并按功能筛选适配型号即可。
