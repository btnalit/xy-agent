# XY04 任务报告：001 provider/adapter 抽象与目录骨架

## 1. 基本信息
- 任务ID：`001`
- 任务名称：provider/adapter 抽象与目录骨架
- 报告日期：2026-04-17
- 执行人：Codex / Hermes
- 对应看板项：`spec/tasks/real-data-adapter-foundation-2026-04-17/xy04-taskboard-2026-04-17.md`

## 2. 目标与范围
- 目标：建立只读 provider 抽象和未来数据源实现的目录骨架。
- 范围（文件/模块）：`app/adapters/read_providers/*`
- 非目标：真实闲鱼接入。

## 3. 变更摘要（前端-后端-数据库全链路）
- 前端：无变化。
- 后端 API：新增 provider abstraction，不改路由。
- 服务层：为后续 resolver/adapter 接线做准备。
- 数据层/仓储：无变化。
- 数据库迁移：不涉及。

## 4. 契约与兼容性自检
- HTTP 路径/方法：`无变化`
- 请求字段：`无变化`
- 响应字段：`无变化`
- SSE / WebSocket / 任务流：`无变化`
- 兼容策略：通过协议抽象扩展内部结构，不影响外部契约。

## 5. 验收与门禁结果
- 专项测试：后续 003/004 统一验证。
- 构建 / lint / typecheck：后续统一验证。
- 契约 / OpenAPI / schema 检查：外部接口不变。
- 回归测试：后续统一验证。
- 发布门禁 / 审计脚本：不涉及。
- 新增/修改测试：后续 003 补齐。

## 6. KPI（Before -> After）
| 指标 | Before | After | 变化 | 结论 |
|---|---:|---:|---:|---|
| provider 抽象协议 | 0 | 1 | +1 | 完成 |
| adapter 目录骨架 | 0 | 1 | +1 | 完成 |
| 未来 provider 占位实现 | 0 | 2 | +2 | 完成 |

## 7. 风险与处置
- 风险：抽象层引入后可能造成实现分散。
- 控制：以单一 `ReadFoundationProvider` 协议收口。
- 残余风险：低。

## 8. 证据索引
- 代码：`apps/hermes-mcp-server/app/adapters/read_providers/base.py`；`demo.py`；`playwright_h5.py`；`real_upstream.py`
- 测试：后续 003 补齐
- 门禁报告：后续 004 统一记录
- 契约产物：无新增外部契约
- 其他：`apps/hermes-mcp-server/app/adapters/read_providers/__init__.py`

## 9. 结论与下一步
- 本任务判定：`Done`
- 下一步建议：将 demo provider 通过 resolver 接入 app，消除硬编码。
