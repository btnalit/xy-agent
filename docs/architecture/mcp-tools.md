# MCP Tool Contract（MVP-1 Read-Only Foundation）

## 1. 设计边界

- 当前批次仅实现只读与建议接口，**不连接真实闲鱼账号**，仅返回 demo 数据。
- 所有响应统一包含：`request_id`、`evidence_refs`、`generated_at`、`source`。
- 建议类接口（如回复建议）只产出草稿，真实发送仍属于写操作，需审批。

## 2. 已落地工具（MVP-1）

| Tool Name | HTTP | Path | 输入 | 输出 data 摘要 |
|---|---|---|---|---|
| `xianyu_get_dashboard` | GET | `/tools/xianyu_get_dashboard` | `account_id`(optional) | 账号看板汇总（待处理订单、未读会话、低库存、告警） |
| `xianyu_list_orders` | GET | `/tools/xianyu_list_orders` | `status`(optional), `limit`, `page` | 订单列表（分页、状态过滤） |
| `xianyu_list_items` | GET | `/tools/xianyu_list_items` | `keyword`(optional), `status`(optional), `limit`, `page` | 商品列表（分页、关键词/状态过滤） |
| `xianyu_list_unread_chats` | GET | `/tools/xianyu_list_unread_chats` | `limit`, `page` | 未读会话列表（优先级、最近消息） |
| `xianyu_suggest_reply` | POST | `/tools/xianyu_suggest_reply` | `thread_id`, `tone`(optional), `goal`(optional) | 回复建议草稿 + 理由 + 审批边界说明 |
| `xianyu_daily_report` | GET | `/tools/xianyu_daily_report` | `date`(optional, `YYYY-MM-DD`) | 每日汇总（KPI、风险、建议动作、审批边界） |

## 3. 响应 Envelope 约束

```json
{
  "request_id": "xianyu_list_orders-6f8a2b1c9d0e",
  "evidence_refs": ["demo://orders/order-9001"],
  "generated_at": "2026-04-17T08:00:00Z",
  "source": "demo-provider",
  "tool_name": "xianyu_list_orders",
  "data": {}
}
```

## 4. 建议类接口审批边界（保留）

- `xianyu_suggest_reply` 返回字段：
  - `approval_required_for_send=true`
  - `approval_boundary_note`（明确“仅生成草稿，不执行发送”）
- `xianyu_daily_report` 返回字段：
  - `approval_boundary_note`（提示改价、上下架、发送等写动作需审批）

## 5. 后续写操作预留（未实现）

| Tool Name | 规划状态 | 审批要求 |
|---|---|---|
| `xianyu_send_reply` | 未实现 | 必须审批 |
| `xianyu_edit_item` | 未实现 | 必须审批 |
| `xianyu_adjust_price` | 未实现 | 必须审批 |
| `xianyu_publish_item` | 未实现 | 必须审批 |
| `xianyu_toggle_item_status` | 未实现 | 必须审批 |
