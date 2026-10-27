---
title: SPI Nand Flash 认证物料（SIFLI MCU AVL V0.4）
type: mcu_avl
doc_type: avl
category: SPI Nand Flash
mcu_family: ["通用-所有SIFLI MCU"]
applicability: ["所有SIFLI MCU系列（含SF32LB52X/SF32LB52x及后续型号）"]
tags: ["AVL合格物料","BOM合规校验","物料选型标准","SIFLI-MCU-AVL-V0.4"]
source_version: "V0.4 (2026-08-12)"
created: 2026-08-12
updated: 2026-08-12
---

# SPI Nand Flash 认证物料（SIFLI MCU AVL V0.4）

> **适用范围**：本表为 SIFLI 全系列 MCU 合格物料（AVL），**不限于 SF32LB52 系列**，适用于所有 SIFLI MCU 型号。具体适配以对应芯片手册 / 硬件设计指南为准。
> **来源**：`raw/mcu/all_chip/avl/SIFLI-MCU-AVL-认证表-V0.4-20260812.xlsx` → Sheet「SPI Nand Flash list」。版本 V0.4（2026-08-12）。
> **优先级**：AVL 企业标准 > 外围器件原厂规格书。

## 分类说明
大容量 SPI Nand Flash，须外部控制供电（无 Deep Power Down）。选型须关注 ECC / Page·Block 大小 / 速率。

## 物料清单（共 18 条）

| 序号 | 型号 | 厂家 | 容量 | 工作电压 | 温度范围 | Manufacture ID | Read JEDEC ID | Page size(Byte) | Block size(Byte) | 最大速率 | ECC | Golden Block | Standby电流 | Page Read电流 | Program/Erase电流 | 下载工具支持 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | F35SQA512M | FORESEE | 512Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0XCD7070 | 9F+dummy(8bit)+MID+DID1+DID2 | 2048+64 | 128K+4K | 133MHz | HW 1-Bit | block0 | 10uA | 10mA | 15mA |  |
| 2 | F35UQA512M | FORESEE | 512Mb | 1.7 ~ 1.95V | -40 ~ 85℃ | 0XCD6060 | 9F+dummy(8bit)+MID+DID1+DID2 | 2048+64 | 128K+4K | 104MHz | HW 1-Bit | block0 | 10uA | 10mA | 15mA |  |
| 3 | DS35M12B | Dosilicon | 512Mb | 1.7 ~ 1.95V | -40 ~ 85℃ | 0XE5A5E5 | 9F+dummy(8bit)+MID+DID | 2048+128 | 128K+8K | 83MHz | HW 8-Bit | block0 | 10uA | 10mA | 15mA |  |
| 4 | DS35Q12B | Dosilicon | 512Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0XE5F5E5 | 9F+dummy(8bit)+MID+DID | 2048+128 | 128K+8K | 104MHz | HW 8-Bit | block0 | 10uA | 10mA | 15mA |  |
| 5 | W25N01GW | WINBOND | 1Gb | 1.7 ~ 1.95V | -40 ~ 85℃ | 0XEFBA21 | 9F+dummy(8bit)+MID+DID1+DID2 | 2048+64 | 128K+4K | 104MHz | HW 1-Bit | block0 | 10uA | 25mA | 25mA |  |
| 6 | W25N01GV | WINBOND | 1Gb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0XEFAA21 | 9F+dummy(8bit)+MID+DID1+DID2 | 2048+64 | 128K+4K | 104MHz | HW 1-Bit | block0 | 10uA | 25mA | 25mA |  |
| 7 | GD5F1GM7RE | GD | 1Gb | 1.7 ~ 2.0V | -40 ~ 85℃ | 0XC881C8 | 9F+dummy(8bit)+MID+DID | 2048+64 | 128K+8K | 104MHz /SDR<br>80MHz /DTR | HW 8-Bit | block0 | 10uA | 10mA | 10mA |  |
| 8 | GD5F1GM7UE | GD | 1Gb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0XC891C8 | 9F+dummy(8bit)+MID+DID | 2048+64 | 128K+8K | 133MHz /SDR<br>104MHz /DTR | HW 8-Bit | block0 | 10uA | 15mA | 15mA |  |
| 9 | F35SQA001G | FORESEE | 1Gb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0XCD7171 | 9F+dummy(8bit)+MID+DID1+DID2 | 2048+64 | 128K+4K | 104MHz | HW 1-Bit | block0 | 10uA | 10mA | 15mA |  |
| 10 | HYF1GQ4IDACAE | HeYangTek | 1Gb | 1.7 ~ 1.98V | -40 ~ 85℃ | 0XC981C9 | 9F+00+MID+DID | 2048+64 | 128K+4K | 80MHz | HW 4-Bit | block0 | 10uA | 5mA |  |  |
| 11 | HYF1GQ4UDACAE | HeYangTek | 1Gb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0XC921C9 | 9F+00+MID+DID | 2048+64 | 128K+4K | 108MHz | HW 4-Bit | block0 | 10uA | 15mA |  |  |
| 12 | XT26Q01D | XTX | 1Gb | 1.7 ~ 1.95V | -40 ~ 85℃ | 0X0B5100 | 9F+00+MID+DID | 2048+128 | 128K+8K | 108MHz | HW 8-Bit | block0 | 15uA | 26mA | 28mA/18mA |  |
| 13 | XT26G01C | XTX | 1Gb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0X0B3100 | 9F+00+MID+DID | 2048+128 | 128K+8K | 104MHz | HW 8-Bit | block0 | 180uA | 25mA | 30mA/25mA |  |
| 14 | DS35M1GB | Dosilicon | 1Gb | 1.7 ~ 1.95V | -40 ~ 85℃ | 0XE5A1E5 | 9F+dummy(8bit)+MID+DID | 2048+128 | 128K+8K | 83MHz | HW 8-Bit | block0 | 10uA | 10mA | 15mA |  |
| 15 | DS35Q1GB | Dosilicon | 1Gb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0XE5F1E5 | 9F+dummy(8bit)+MID+DID | 2048+128 | 128K+8K | 104MHz | HW 8-Bit | block0 | 10uA | 10mA | 15mA |  |
| 16 | ZB35Q01A | ZBIT | 1Gb | 2.7 ~ 3.6V | -40 ~ 85℃ | 0X5E415E | 9F+00+MID+DID | 2048+64 | 128K+4K | 80MHz | HW 8-Bit | block0 | 10uA | 10mA | 10mA |  |
| 17 | FM25SL01 | FM | 1Gb | 1.75 ~ 1.95V | -40 ~ 85℃ | 0XA1A5A1 | 9F+dummy(8bit)+MID+DID | 2048+128 | 128K+8K | 80MHz | HW 1-Bit | block0 | 10uA | 16mA | 16mA |  |
| 18 | TC58CYG0S3HRAIJ | KIOXIA | 1Gb | 1.7 ~ 1.95V | -40 ~ 85℃ | 0X98D240 | 9F+dummy(8bit)+MID+DID1+DID2 | 2048+64 | 128K+4K | 133MHz | HW 8-Bit | block0 | 30uA | 17mA | 26mA |  |

## 备注
- 每行物料以 AVL 表格「认证型号 / 序号」为准；参数冲突以 AVL 企业标准优先。
- 本表为跨系列共享资源；新增 MCU 家族可直接引用并按功能筛选适配型号。
