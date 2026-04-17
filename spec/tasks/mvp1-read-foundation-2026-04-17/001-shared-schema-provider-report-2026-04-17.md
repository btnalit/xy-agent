# XY02 任务报告：001 共享 schema/model 与 demo provider 实现

## 1. 基本信息

- 任务ID：`001`
- 任务名称：共享 schema/model 与 demo provider 实现
- 报告日期：2026-04-17
- 执行人：Codex
- 对应看板项：`spec/tasks/mvp1-read-foundation-2026-04-17/xy02-taskboard-2026-04-17.md`

## 2. 目标与范围

- 目标：为 MVP-1 六类只读工具建立统一共享模型，并提供 coherent demo 数据供给层。
- 范围（文件/模块）：`packages/xianyu-schemas`、`apps/hermes-mcp-server/app/services`。
- 非目标：真实闲鱼数据抓取、数据库持久化、任何写操作执行。

## 3. 变更摘要（前端-后端-数据库全链路）

- 前端：无变化。
- 后端 API：间接受益（为后续 API response_model 提供共享契约）。
- 服务层：新增 `DemoReadFoundationProvider`，覆盖 dashboard/orders/items/chats/reply/daily report。
- 数据层/仓储：无变化（仍为内存 demo 数据）。
- 数据库迁移：无变化。

## 4. 契约与兼容性自检

- HTTP 路径/方法：本任务不直接改路由。
- 请求字段：新增只读输入模型（items/chats/reply/daily report）。
- 响应字段：新增统一 envelope 与六类 data 模型。
- SSE / WebSocket / 任务流：无变化。
- 兼容策略：保留旧 `build_demo_dashboard` 返回结构（通过 provider 输出 data 子结构维持兼容）。

## 5. 验收与门禁结果

- 专项测试：新增 schema/provider 测试文件（执行记录见 004）。
- 构建 / lint / typecheck：`compileall` 在 004 统一执行通过。
- 契约 / OpenAPI / schema 检查：通过文档与模型人工对照。
- 回归测试：旧 smoke 用例保持可运行结构。
- 发布门禁 / 审计脚本：由 004 统一执行。
- 新增/修改测试：`apps/hermes-mcp-server/tests/test_read_models.py`、`apps/hermes-mcp-server/tests/test_read_provider.py`。

## 6. KPI（Before -> After）

| 指标 | Before | After | 变化 | 结论 |
|---|---:|---:|---:|---|
| 共享 read schema/model 数 | 0 | 20+ | +20+ | 完成 |
| 覆盖工具类型 | 1 | 6 | +5 | 完成 |
| 服务层 provider 能力点 | 1 | 6 | +5 | 完成 |

## 7. 风险与处置

- 风险：模型快速演进导致后续 API 破坏兼容。
- 控制：统一在 `xianyu_schemas.read_models` 中集中维护，并通过 response_model 固化。
- 残余风险：运行环境未安装依赖，自动化运行验证需后续补齐。

## 8. 证据索引

- 代码：
  - `packages/xianyu-schemas/xianyu_schemas/read_models.py`
  - `packages/xianyu-schemas/xianyu_schemas/tools.py`
  - `packages/xianyu-schemas/xianyu_schemas/__init__.py`
  - `apps/hermes-mcp-server/app/services/read_foundation.py`
  - `apps/hermes-mcp-server/app/services/dashboard.py`
- 测试：
  - `apps/hermes-mcp-server/tests/test_read_models.py`
  - `apps/hermes-mcp-server/tests/test_read_provider.py`
- 门禁报告：`spec/tasks/mvp1-read-foundation-2026-04-17/004-validation-gates-output-2026-04-17.txt`
- 契约产物：`docs/architecture/mcp-tools.md`
- 其他：无

## 9. 结论与下一步

- 本任务判定：`Done`
- 下一步建议：执行 002，完成路由层集成并落地 6 个工具端点。
