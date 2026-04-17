# XY02 任务报告：002 FastAPI 只读端点实现与集成

## 1. 基本信息

- 任务ID：`002`
- 任务名称：FastAPI 只读端点实现与集成
- 报告日期：2026-04-17
- 执行人：Codex
- 对应看板项：`spec/tasks/mvp1-read-foundation-2026-04-17/xy02-taskboard-2026-04-17.md`

## 2. 目标与范围

- 目标：在 `hermes-mcp-server` 暴露 6 个 MVP-1 只读工具端点并接入 demo provider。
- 范围（文件/模块）：`apps/hermes-mcp-server/app/main.py`、`apps/hermes-mcp-server/app/__init__.py`。
- 非目标：真实账号连接、写操作执行链路、鉴权体系。

## 3. 变更摘要（前端-后端-数据库全链路）

- 前端：无变化。
- 后端 API：新增/明确 6 个 `/tools/xianyu_*` 端点；保留 `/demo/dashboard` 兼容路由。
- 服务层：路由层调用 `DemoReadFoundationProvider`。
- 数据层/仓储：无变化（内存 demo 数据）。
- 数据库迁移：无变化。

## 4. 契约与兼容性自检

- HTTP 路径/方法：
  - 新增 `GET /tools/xianyu_get_dashboard`
  - 新增 `GET /tools/xianyu_list_orders`
  - 新增 `GET /tools/xianyu_list_items`
  - 新增 `GET /tools/xianyu_list_unread_chats`
  - 新增 `POST /tools/xianyu_suggest_reply`
  - 新增 `GET /tools/xianyu_daily_report`
  - 保留 `GET /demo/dashboard`
- 请求字段：按输入模型校验，分页参数均有范围限制。
- 响应字段：统一包含 envelope（`request_id`、`evidence_refs`、`generated_at`、`source`）。
- SSE / WebSocket / 任务流：无变化。
- 兼容策略：保留旧 demo 路径并提供同类 dashboard 数据。

## 5. 验收与门禁结果

- 专项测试：新增 API 测试文件（执行情况见 004）。
- 构建 / lint / typecheck：`compileall` 通过（见 004）。
- 契约 / OpenAPI / schema 检查：`response_model` 绑定共享模型，人工核对通过。
- 回归测试：旧 smoke 测试仍可读取 dashboard。
- 发布门禁 / 审计脚本：由 004 统一执行。
- 新增/修改测试：`apps/hermes-mcp-server/tests/test_read_tools_api.py`、`apps/hermes-mcp-server/tests/test_smoke.py`。

## 6. KPI（Before -> After）

| 指标 | Before | After | 变化 | 结论 |
|---|---:|---:|---:|---|
| read-only 工具 API 端点数 | 1 | 6 | +5 | 完成 |
| 统一 response envelope 覆盖率 | 0% | 100% | +100% | 完成 |
| 兼容路由保留情况 | 有 `/demo/dashboard` | 仍保留 | 0 | 完成 |

## 7. 风险与处置

- 风险：依赖路径导致运行时无法加载 `xianyu-schemas`。
- 控制：在 `app/__init__.py` 添加 schema 包路径引导，并在 `main.py` 提供 fallback。
- 残余风险：环境未安装 FastAPI/Pydantic 时无法本地启动，需按 README 安装依赖。

## 8. 证据索引

- 代码：
  - `apps/hermes-mcp-server/app/main.py`
  - `apps/hermes-mcp-server/app/__init__.py`
- 测试：
  - `apps/hermes-mcp-server/tests/test_read_tools_api.py`
  - `apps/hermes-mcp-server/tests/test_smoke.py`
- 门禁报告：`spec/tasks/mvp1-read-foundation-2026-04-17/004-validation-gates-output-2026-04-17.txt`
- 契约产物：`docs/architecture/mcp-tools.md`
- 其他：`README.md`

## 9. 结论与下一步

- 本任务判定：`Done`
- 下一步建议：执行 003，补齐测试资产与文档契约更新。
