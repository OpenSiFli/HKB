---
title: CR-参考设计-电池系列OVP与充电器
type: mcu_check_rule
aliases: ["CR_RefDesign_Batt_OVP_Charger","电池OVP充电器审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-致命"]
sources: [[SF32LB52x_batt_Reference_Schematic],[SF32LB52x_batt],[SF32LB52_Peripheral_Power]]
mcu_family: ["SF32LB52"]
series_applicability: ["SF32LB52x(电池)"]
mcu_model: ["SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: 致命
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SF32LB52x（电池系列）官方参考设计，校验 **电池供电输入保护（OVP）+ 内置充电器配置**是否符合黄金样板：VBUS 4.6~5.5V、OVP Vout 5.1~5.7V、P-Ch MOSFET Rds<250mΩ 响应<100ns、芯片 VBUS≥4.6V、内置充电器满电 4.2~4.45V、ESD+防反接、VBAT 走线阻抗小。

## 核心硬件内容（背景）
- 电池系列**充电器为芯片内置**的 ≤560mA 锂电线性充电器，支持满电电压 **4.2V~4.45V**；仅在设计**使用片内充电器**为电池充电时，才涉及该内置充电器的参数核查（见下方特别说明）。
- 输入 VBUS 经 **OVP** 后给系统：VBUS 供电范围 **4.6V~5.5V**；OVP 示例 ETA7112（Vin 保护阈值 5.5V，Vout 5.4~5.7V）、LP5305AQVF（Vout 5.1V）；P-Ch MOSFET 内阻 **<250mΩ**、响应 **<100ns**。
- 须做 **ESD 与防反接保护**；尽量减小 POGO PIN→芯片 VBUS 走线阻抗，保证芯片 VBUS 管脚 **≥4.6V**（否则充电/工作异常）。
- VBAT 到电池焊点走线阻抗尽量小。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 解析到电池系列 VBUS/VBAT 输入级（OVP 芯片、P-Ch MOSFET、充电器配置、ESD/防反接）时触发；其中**充电器专属核查仅在使用片内充电器时适用**（见下方特别说明）。
2. **违规现象描述**：
   - 无 OVP 或选型错（Vout>5.7V、或过压保护阈值不当）→ 过压损坏 MCU；
   - 芯片 VBUS 处 <4.6V（走线/连接器压降过大）；
   - 充电器满电电压配置 >4.45V → 电池过充；
   - 缺 ESD / 防反接保护；VBAT 走线阻抗过大。
3. **风险影响说明**：过压/过充 → MCU 与电池永久损坏、起火风险（致命）。
4. **标准化整改方案**：按参数选 OVP+MOSFET（Vout 5.1~5.7V、Rds<250mΩ、响应<100ns）；保证芯片 VBUS≥4.6V；配充电器满电 4.2~4.45V；加 ESD/防反接；VBAT 走线低阻抗。
5. **知识库溯源依据**：[[SF32LB52x_batt]]；[[SF32LB52_Peripheral_Power]]；[[SF32LB52x_batt_Reference_Schematic]]。

## 审图判读特别说明 —— 内置充电器触发条件
**电池系列的充电器是芯片内置的**。由此引出关键判定原则：

- **充电器专属核查（满电电压 4.2~4.45V、最大充电电流 560mA 等）仅在设计「使用片内充电器」为电池充电时触发**。
  - 若选用**外置充电芯片**（例如「接入充电器后设备立即亮屏」场景，见官方 Checklist 第 53 条），则内置充电器核查判 **N/A**，转而核查外置充电芯片选型（需具备电源路径管理）；
  - 若**不使用片内充电器**（见官方 Checklist 第 57 条：VBUS 引脚可悬空、可省略 VBUS 端外接电容、该场景 VBAT 无对外输出能力），内置充电器核查同样判 **N/A**。
- **OVP 输入过压保护（官方 Checklist 第 52/55/56 条）与是否使用内置充电器无关**：只要 VBUS 接入外部电源，OVP 保护即必须保留，不可因「不用内置充电器」而省略。
- → **AI 审图注意**：先判定本设计是否启用片内充电器，再决定内置充电器参数核查是否适用；勿对「外置充电 / VBUS 悬空」设计误报内置充电器违规。

## 关联页面
- 芯片实体：[[SF32LB52x_batt]]｜电源：[[SF32LB52_Peripheral_Power]]｜电池电源树：[[CR_RefDesign_Batt_PowerTree]]｜绝对最大额定值：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]，Raw：raw/mcu/ref_design/SF32LB52x_batt/，设计注释（OVP 选型、VBUS 范围、充电器 4.2~4.45V、ESD/防反接）

## 待核实问题
- 无（参数来自参考设计黄金样板）。
