---
title: Nor Flash 认证物料（SIFLI MCU AVL V0.4）
type: mcu_avl
doc_type: avl
category: Nor Flash
mcu_family: ["通用-所有SIFLI MCU"]
applicability: ["所有SIFLI MCU系列（含SF32LB52X/SF32LB52x及后续型号）"]
tags: ["AVL合格物料","BOM合规校验","物料选型标准","SIFLI-MCU-AVL-V0.4"]
source_version: "V0.4 (2026-08-12)"
created: 2026-08-12
updated: 2026-08-12
---

# Nor Flash 认证物料（SIFLI MCU AVL V0.4）

> **适用范围**：本表为 SIFLI 全系列 MCU 合格物料（AVL），**不限于 SF32LB52 系列**，适用于所有 SIFLI MCU 型号。具体适配以对应芯片手册 / 硬件设计指南为准。
> **来源**：`raw/mcu/all_chip/avl/SIFLI-MCU-AVL-认证表-V0.4-20260812.xlsx` → Sheet「Nor Flash list」。版本 V0.4（2026-08-12）。
> **优先级**：AVL 企业标准 > 外围器件原厂规格书。

## 分类说明
外挂代码/数据存储 Nor Flash（QSPI），支持 Deep Power Down 低功耗。详见各 MCU 存储接口外设页。

## 物料清单（共 44 条）

| 序号 | 型号 | 厂家 | 容量 | 工作电压 | 温度范围 | 最快时钟<br>SDR | 最快时钟<br>TDR | Manufacture ID | Standby电流 | Deep Power Down电流 | EBH电流 | EDH电流 | 下载工具支持 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P25Q40SU | PUYA | 4Mb | 1.65 ~ 3.6V | -40 ~ 85℃ | 85MHz Fast Read @1.8V<br>104MHz Fast Read @3.3V | 不支持 | 0X856013 | 10uA | 0.1uA @1.8V<br>0.6uA @3.3V | 3.5mA @85MHz 1.8V<br>5mA @85MHz 3.3V | 不支持 |  |
| 2 | P25Q80LE | PUYA | 8Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 104MHz Fast Read | 不支持 | 0X856014 | 9uA | 0.1uA | 1.5mA @85MHz | 不支持 |  |
| 3 | GD25LE80E | GD | 8Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XC86014 | 10uA | 0.2uA | 3mA @80MHz | 不支持 |  |
| 4 | UC25WQ80IB | UCUN | 8Mb | 1.65 ~ 3.6V | -40 ~ 85℃ | 104MHz Fast Read | 不支持 | 0XB36014 | 1.5uA | 0.5uA | 6mA @85MHz | 缺 |  |
| 5 | P25Q16LE | PUYA | 16Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 104MHz Fast Read | 不支持 | 0X856015 | 18uA | 0.1uA | 3mA @85MHz | 不支持 |  |
| 6 | GD25LE16E | GD | 16Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XC86015 | 10uA | 0.2uA | 3mA @80MHz | 不支持 |  |
| 7 | P25Q32L | PUYA | 32Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 120MHz Fast Read | 不支持 | 0X856016 | 9uA | 0.2uA | 2mA @85MHz | 不支持 |  |
| 8 | SK25LE032 | SK | 32Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 133MHz Fast Read | 80MHz | 0X257016 | 10uA | 0.1uA | 2mA @80MHz | 2.6mA @80MHz |  |
| 9 | GD25LE32E | GD | 32Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XC86016 | 10uA | 0.2uA | 3mA @80MHz | 不支持 |  |
| 10 | UC25IQ32A | UCUN | 32Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 66MHz | 0XB34014 | 15uA | 1uA | 8mA @80MHz | 缺 |  |
| 11 | P25Q64LE | PUYA | 64Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 104MHz Fast Read | 不支持 | 0X856017 | 18uA | 0.3uA | 2mA @85MHz | 不支持 |  |
| 12 | P25Q64H | PUYA | 64Mb | 2.3 ~ 3.6V | -40 ~ 85℃ | 120MHz Fast Read | 不支持 | 0X856017 | 18uA | 0.6uA | 4mA @85MHz | 不支持 |  |
| 13 | P25Q64SH | PUYA | 64Mb | 2.3 ~ 3.6V | -40 ~ 85℃ | 120MHz Fast Read | 70MHz | 0X856017 | 10uA | 0.3uA | 6.8mA @85MHz | 9.45mA @70MHz |  |
| 14 | GD25LE64E | GD | 64Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XC86017 | 10uA | 0.2uA | 3mA @80MHz | 不支持 |  |
| 15 | ZB25LQ64A | ZBIT | 64Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 133MHz Fast Read | 66MHz | 0X5E7017 | 10uA | 1uA | 4mA @104MHz | 缺 |  |
| 16 | BY25Q64ES | BOYA | 64Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 120MHz Fast Read | 不支持 | 0X684017 | 9uA | 0.4uA | 6mA @80MHz | 不支持 |  |
| 17 | UC25IQ64A | UCUN | 64Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 66MHz | 0XB34017 | 10uA | 1uA | 15mA @80MHz | 缺 |  |
| 18 | P25Q128L | PUYA | 128Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 70MHz Fast Read | 43MHz | 0X856018 | 15uA | 0.5uA | 4.5mA @85MHz | 缺 |  |
| 19 | PY25Q128HA | PUYA | 128Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 104MHz Fast Read | 66MHz | 0X852018 | 15uA | 1uA | 7mA @85MHz | 9mA @66MHz |  |
| 20 | SK25LP128 | SK | 128Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 166MHz Fast Read | 104MHz | 0X257018 | 8uA | 0.1uA | 2mA @80MHz | 2.6mA @80MHz |  |
| 21 | GD25LQ128E | GD | 128Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 120MHz Fast Read | 不支持 | 0XC86018 | 35uA | 1uA | 13mA @80MHz | 不支持 |  |
| 22 | GD25Q128E | GD | 128Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XC84018 | 14uA | 1uA | 8mA @80MHz | 不支持 |  |
| 23 | GD25F128F | GD | 128Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 166MHz Fast Read | 104MHz | 0XC84318 | 16uA | 1uA | 12mA @80MHz | 缺 |  |
| 24 | W25Q128JW | Winbond | 128Mb | 1.7 ~ 1.95V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XEF6018 | 10uA | 1uA | 缺 | 不支持 |  |
| 25 | W25Q128JV | Winbond | 128Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XEF4018 | 10uA | 1uA | 12mA @104MHz | 不支持 |  |
| 26 | XT25F128F | XTX | 128Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 104MHz | 0X0B4018 | 15uA | 1uA | 8mA @80MHz | 缺 |  |
| 27 | XT25Q128DW | XTX | 128Mb | 1.7 ~ 2.0V | -40 ~ 85℃ | 108MHz Fast Read | 76MHz | 0X0B6018 | 12uA | 0.4uA | 9mA @80MHz | 缺 |  |
| 28 | FM25W128 | FM | 128Mb | 1.65 ~ 3.6V | -40 ~ 85℃ | 50MHz Fast Read @1.8V<br>100MHz Fast Read @3.3V | 不支持 | 0XA12818 | 5uA | 1uA@3.3V | 缺 | 不支持 |  |
| 29 | XM25QU128C | XMC | 128Mb | 1.65 ~ 1.95V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0X204118 | 18uA | 6uA | 6mA @66MHz | 不支持 |  |
| 30 | ZB25VQ128D | ZBIT | 128Mb | 2.3 ~ 3.6V | -40 ~ 85℃ | 104MHz Fast Read | 不支持 | 0X5E4018 | 10uA | 1uA | 4mA @104MHz | 不支持 |  |
| 31 | ZB25LQ128B | ZBIT | 128Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 104MHz Fast Read | 不支持 | 0X5E5018 | 9uA | 3uA | 9mA @104MHz | 不支持 |  |
| 32 | BY25Q128ES | BOYA | 128Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 108MHz Fast Read | 不支持 | 0X684018 | 14uA | 0.2uA | 6mA @80MHz | 不支持 |  |
| 33 | UC25IQ128A | UCUN | 128Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 66MHz | 0XB34018 | 15uA | 1uA | 12mA @80MHz | 缺 |  |
| 34 | W25Q256JW | Winbond | 256Mb | 1.7 ~ 1.95V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XEF6019 | 10uA | 1uA | 8mA @80MHz | 不支持 |  |
| 35 | W25Q256JV | Winbond | 256Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XEF7019 | 10uA | 1uA | 12mA @104MHz | 不支持 |  |
| 36 | PY25Q256HB | PUYA | 256Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 100MHz | 0X852019 | 20uA | 1uA | 7mA @80MHz | 11.5mA @80MHz |  |
| 37 | GD25LQ256D | GD | 256Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 120MHz Fast Read | 不支持 | 0XC86019 | 70uA | 2uA | 10mA @80MHz | 不支持 |  |
| 38 | GD25Q256E | GD | 256Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0XC84019 | 16uA | 1uA | 12mA @80MHz | 不支持 |  |
| 39 | XM25QU256C | XMC | 256Mb | 1.65 ~ 1.95V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0X204119 | 15uA | 7uA | 11mA @66MHz | 不支持 |  |
| 40 | XM25QH256C | XMC | 256Mb | 2.3 ~ 3.6V | -40 ~ 85℃ | 133MHz Fast Read | 不支持 | 0X204019 | 15uA | 7uA | 7mA @66MHz | 不支持 |  |
| 41 | XT25F256BW | XTX | 256Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 104MHz Fast Read | 50MHz | 0X0B4019 | 15uA | 0.5uA | 8mA @80MHz | 缺 |  |
| 42 | DS25M4BA | Dosilicon | 256Mb | 1.65 ~ 1.95V | -40 ~ 85℃ | 108MHz Fast Read | 80MHz | 0XE54219 | 15uA | 5uA | 13mA @108MHz | 缺 |  |
| 43 | BY25Q256FS | BOYA | 256Mb | 2.7 ~ 3.6V | -40 ~ 85℃ | 100MHz Fast Read | 54MHz | 0X684919 | 28uA | 2uA | 13mA @80MHz | 缺 |  |
| 44 | MX25U25643G | MXIC | 256Mb | 1.65 ~ 2.0V | -40 ~ 85℃ | 133MHz Fast Read | 54MHz | 0XC22539 | 15uA | 0.8uA | 7mA @84MHz | 缺 |  |

## 备注
- 每行物料以 AVL 表格「认证型号 / 序号」为准；参数冲突以 AVL 企业标准优先。
- 本表为跨系列共享资源；新增 MCU 家族可直接引用并按功能筛选适配型号。
