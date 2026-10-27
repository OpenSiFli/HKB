# HKB —— SiFli 硬件知识库（Hardware Knowledge Base）

> 一个**可直接下载到本地、供 AI 工具检索与原理图评审使用**的 SiFli（思澈科技）MCU 硬件知识库。
> **无网页版、不走文档站点构建**——本仓库的目的就是让你 `git clone` 下来，用本地 AI 助手 / RAG 直接读取，回答硬件设计问题、评审原理图。

---

## 一、这是什么

HKB（Hardware Knowledge Base）把分散在规格书、用户手册、硬件设计指南、参考设计、官方 Checklist、AVL 物料清单与工程复盘中的 SiFli MCU 硬件知识，结构化沉淀为一套**纯文本 / Markdown 知识资产**，供开发者在本地离线使用：

- **AI 硬件问答**：把本仓库作为上下文喂给 AI 助手，检索封装、引脚、电气参数、外设、电源架构、约束禁忌等问题。
- **原理图评审（Schematic Review）**：依据仓库内的校验规则（`check_rules`）与设计规范（`design_rules`）、参考设计（黄金样板），让 AI 对照检查你的原理图。

> 说明：本地 Obsidian 知识库是这份仓库的内容来源，二者内容一致、只是载体不同。本仓库**不经过 Sphinx / 文档站点构建**，也不部署任何网页版。为保持仓库轻量、纯文本，**原始参考资料（规格书 PDF、数据表等）不随本仓库分发**，仅以结构化提取后的 Markdown 页面形式沉淀于此。

---

## 二、内容结构

知识库按两大平级类别组织：

### 1. MCU 全系列硬件知识库（`wiki/mcu/`）

以芯片实体为核心，覆盖：

- **芯片实体（chip_entity）**：封装、引脚、电气参数、极限规格、典型电路、约束禁忌、勘误、原厂/企业规范。
- **外设专项（peripheral）**：GPIO / 电源 / 时钟 / GPADC / 音频 / 蓝牙射频 / 串口（UART-I2C-SPI-CAN）/ 存储（MPI-SD-eMMC）/ 定时器 PWM / 显示与图形（ePicasso·LCD·DCMI·eZip）等。
- **引脚复用矩阵（PINMUX）**：大核 GPIO 完整复用总表 + matrix index + LCD mux；以官方 xlsx 为权威依据。
- **硬件设计指南（Hardware Design Guide）**：官方 wiki 硬件设计指南，3.3V 系列与电池系列各一份。
- **参考设计原理图（Reference Schematic）**：官方参考设计结构化提炼（黄金样板），含电源架构 / 关键 BOM / 设计要点——原理图评审的主要对照基准。
- **校验规则（Check Rules / `CR_*`）**：审图规则库，覆盖多电源域、绝对最大额定值、EPAD 接地、低功耗浮空 IO、48M/32K 晶振、BLE 天线、USB 差分对、复位电平、BOOT 寄存器、I2C 总线卡死、存储互斥、接口电平匹配、电池 OVP/电源树等——**原理图 AI 评审的核心依据**。
- **设计规范（Design Rules / `DR_*`）**：电源架构、GPIO 默认 PUPD 高阻、低功耗 IO 保持、复位设计、调试接口、BOOT 模式、PA34 电源键引脚作普通 GPIO 使用等。
- **故障案例（Fault Cases / `FC_*`）**：I2C 总线卡死、调试接口失效、Hibernate 合封漏电、SDMMC-FIFO 溢出等工程复盘。
- **AVL 合格物料库**：SiFli 官方 AVL 认证物料清单（晶体 / Buck 电感 / Nor Flash / SPI Nand / SD Nand / LCD 驱动），BOM 选型优先级高于器件原厂规格书，覆盖**全系列 SIFLI MCU**。

#### 已覆盖芯片家族（两大家族，各含两个独立系列，不可合并看待）

| 家族 | 系列 | 供电特征 |
| --- | --- | --- |
| **SF32LB52** | `SF32LB52X`（大写 X）= 3.3V 供电系列 | 无充电电路，主电 PVDD，GPIO 由 VDDIOA 供电 |
| | `SF32LB52x`（小写 x）= 电池供电系列 | 内置 560mA 充电，电源引脚 VBUS/VBAT/VCC |
| **SF32LB57** | `SF32LB57X`（大写 X）= 3.3V 供电系列 | 无充电电路，主电 PVDD，GPIO 由 VDDIOA 供电 |
| | `SF32LB57x`（小写 x）= 电池供电系列 | 内置充电模块，电源引脚 VBUS/VBAT/VCC/VSYS |

> 📌 文档标题大小写与芯片系列**一致**：3.3V 系列用大写 X（如 DS5202-SF32LB52X），电池系列用小写 x（如 DS5201-SF32LB52x）。

### 2. 开发板（Dev Board）硬件知识库（`wiki/dev_board/`）

以原理图为主要入库依据，提取开发板 11 项核心参数（平台 / 芯片 / 模组 / 上芯方式 / 存储配置 / 供电方式 / 外设 / 调试接口 / 适用场景 / 使用指南文档 / 图纸），与 MCU 知识库单向引用（不修改 MCU 侧文件）。

---

## 三、给开发者的使用方法

```bash
git clone https://github.com/OpenSiFli/HKB.git
```

克隆后，把整个仓库目录作为上下文提供给你的 AI 工具即可，**无需任何构建步骤**：

- **AI 硬件问答**：直接询问，例如
  - "SF32LB52x 电池系列的电源引脚有哪些？充电电流多大？"
  - "SF32LB57X 的 GPIO 默认上下拉状态是什么？"
  - "Audio ADC 单端输入需要多大的隔直电容？"
- **原理图评审**：把你的原理图（或器件清单 / 关键网络）连同仓库内的 `check_rules` / `design_rules` 一起交给 AI，让它逐条对照校验规则，给出评审意见与整改建议。
- 若你的工具支持本地知识库 / RAG / MCP，可将本仓库配置为其中一个知识源，提升检索精度。

> 所有页面以双链（Obsidian 风格 `[[...]]`）互相关联；在支持双链的查看器（如 Obsidian）中体验最佳，不支持时也不影响纯文本检索。

---

## 四、内容状态

本仓库用于承载上述硬件知识库，内容正从内部知识库持续迁移填充中。**原始参考资料（规格书 PDF、数据表等）不随本仓库分发**，仓库内仅保留结构化提取后的 Markdown 页面。

---

## 五、相关资源

- SiFli 官网：<https://www.sifli.com/>
- 芯片选型与开发板 Wiki（中文 / English）：<https://wiki.sifli.com/> 、<https://wiki.sifli.com/en/>
- SDK 文档：<https://docs.sifli.com/>
- SiFli SDK（GitHub）：<https://github.com/OpenSiFli/SiFli-SDK>
- 官方论坛（BBS）：<https://bbs.sifli.com/>
- 商务联系：sales@sifli.com

---

## 六、License

本仓库文档采用 **Apache License 2.0**，详见 [LICENSE](./LICENSE)。
