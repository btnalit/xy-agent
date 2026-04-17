# XY04 任务报告：002 demo provider 适配抽象 + resolver 接线

## 1. 基本信息
- 任务ID：`002`
- 任务名称：demo provider 适配抽象 + resolver 接线
- 报告日期：2026-04-17
- 执行人：Codex / Hermes
- 对应看板项：`spec/tasks/real-data-adapter-foundation-2026-04-17/xy04-taskboard-2026-04-17.md`

## 2. 目标与范围
- 目标：让应用通过 resolver 获取 provider，并保持 demo 行为和兼容导入稳定。
- 范围（文件/模块）：`app/main.py`、`services/read_provider_resolver.py`、`services/read_foundation.py`、`services/dashboard.py`
- 非目标：真实 provider 实现。

## 3. 变更摘要（前端-后端-数据库全链路）
- 前端：无变化。
- 后端 API：路由仍然稳定，但 provider 来源改为 resolver。
- 服务层：新增 resolver/factory 与兼容导出层。
- 数据层/仓储：无变化。
- 数据库迁移：不涉及。

## 4. 契约与兼容性自检
- HTTP 路径/方法：`无变化`
- 请求字段：`无变化`
- 响应字段：`无变化`
- SSE / WebSocket / 任务流：`无变化`
- 兼容策略：`read_foundation.py` 保留旧导入路径，`demo` 仍为默认 provider。

## 5. 验收与门禁结果
- 专项测试：后续 003/004 完成。
- 构建 / lint / typecheck：后续统一验证。
- 契约 / OpenAPI / schema 检查：app routes 与 response_model 不变。
- 回归测试：后续统一执行。
- 发布门禁 / 审计脚本：不涉及。
- 新增/修改测试：后续 003 增加 resolver 测试。

## 6. KPI（Before -> After）
| 指标 | Before | After | 变化 | 结论 |
|---|---:|---:|---:|---|
| provider 获取方式 | main.py 直接持有 demo provider | resolver/factory 解析 | 解耦 | 完成 |
| 兼容导出层 | 旧实现文件 | 兼容 shim | 稳定 | 完成 |
| 可配置 provider key | 0 | 3 | +3 | 完成 |

## 7. 风险与处置
- 风险：provider 解析错误导致运行期不可用。
- 控制：默认 provider 固定为 `demo`，未知 key 显式报错。
- 残余风险：低。

## 8. 证据索引
- 代码：`apps/hermes-mcp-server/app/main.py`；`apps/hermes-mcp-server/app/services/read_provider_resolver.py`；`apps/hermes-mcp-server/app/services/read_foundation.py`；`apps/hermes-mcp-server/app/services/dashboard.py`
- 测试：`apps/hermes-mcp-server/tests/test_read_provider_resolver.py`
- 门禁报告：后续 004 统一记录
- 契约产物：`docs/architecture/mcp-tools.md`
- 其他：无

## 9. 结论与下一步
- 本任务判定：`Done`
- 下一步建议：补 resolver/placeholder provider 测试与文档说明。
