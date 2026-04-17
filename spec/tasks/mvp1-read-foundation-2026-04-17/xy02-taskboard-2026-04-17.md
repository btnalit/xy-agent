# XY02 长任务模式任务看板（000~00n）

> 任务主题：XY02 MVP-1 read-only foundation  
> 创建日期：2026-04-17  
> 任务规范：`用户任务说明（XY02）` + `/vol1/1000/codexcli/AGENTS.md` + `AGENTS.md`  
> 启动报告：`spec/tasks/mvp1-read-foundation-2026-04-17/000-high-roi-xy02-mvp1-read-foundation-roadmap-2026-04-17.md`  
> 执行日志：`spec/tasks/mvp1-read-foundation-2026-04-17/xy02-log.md`

## 1. 状态定义

- `Todo`：未开始
- `In Progress`：进行中
- `Blocked`：受阻
- `Done`：完成并附证据
- `Done (Waived)`：完成但有豁免说明

## 2. 看板主表

| ID | 优先级 | 任务 | 状态 | 验收标准 | 证据路径 |
|---|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结（长任务模式建档） | Done | 路线图、看板、日志、模板齐备并具备可执行口径 | `spec/tasks/mvp1-read-foundation-2026-04-17/000-high-roi-xy02-mvp1-read-foundation-roadmap-2026-04-17.md`；`spec/tasks/mvp1-read-foundation-2026-04-17/xy02-taskboard-2026-04-17.md`；`spec/tasks/mvp1-read-foundation-2026-04-17/xy02-log.md`；`spec/tasks/mvp1-read-foundation-2026-04-17/xy02-task-report-template.md` |
| 001 | P0 | 共享 schema/model 与 demo provider 实现 | Done | 6 类工具 schema/model 完整；provider 输出 coherent demo 数据；不触发真实写操作 | `packages/xianyu-schemas/xianyu_schemas/read_models.py`；`packages/xianyu-schemas/xianyu_schemas/tools.py`；`packages/xianyu-schemas/xianyu_schemas/__init__.py`；`apps/hermes-mcp-server/app/services/read_foundation.py`；`apps/hermes-mcp-server/app/services/dashboard.py`；`spec/tasks/mvp1-read-foundation-2026-04-17/001-shared-schema-provider-report-2026-04-17.md` |
| 002 | P0 | FastAPI 只读端点实现与集成 | Done | 6 个 MVP-1 只读/建议端点可调用；响应包含 request_id/evidence_refs；保留兼容路由 | `apps/hermes-mcp-server/app/main.py`；`apps/hermes-mcp-server/app/__init__.py`；`spec/tasks/mvp1-read-foundation-2026-04-17/002-read-api-endpoints-report-2026-04-17.md` |
| 003 | P0 | 测试补齐与文档契约更新 | Done | 新增 schema/service/endpoint 测试；README 与 mcp-tools 文档更新并反映审批边界 | `apps/hermes-mcp-server/tests/conftest.py`；`apps/hermes-mcp-server/tests/test_read_models.py`；`apps/hermes-mcp-server/tests/test_read_provider.py`；`apps/hermes-mcp-server/tests/test_read_tools_api.py`；`apps/hermes-mcp-server/tests/test_smoke.py`；`README.md`；`docs/architecture/mcp-tools.md`；`spec/tasks/mvp1-read-foundation-2026-04-17/003-tests-doc-contract-report-2026-04-17.md` |
| 004 | P0 | 门禁执行与证据沉淀 | Done (Waived) | `compileall`、`compose config` 通过；pytest 因环境缺依赖记录豁免与后续动作 | `spec/tasks/mvp1-read-foundation-2026-04-17/004-validation-gates-output-2026-04-17.txt`；`spec/tasks/mvp1-read-foundation-2026-04-17/004-validation-gates-report-2026-04-17.md` |
| 00n | P0 | 全局翻盘审查与结题 | Done | 输出结题报告，汇总 KPI、门禁、兼容性、风险与下一步 | `spec/tasks/mvp1-read-foundation-2026-04-17/00n-global-review-report-2026-04-17.md` |

## 3. 统一门禁（每任务完成必跑）

1. `python3 -m compileall apps packages` ✅
2. `docker compose -f infra/compose/docker-compose.yml config` ✅
3. `PYTHONPATH=apps/hermes-mcp-server python3 -m pytest apps/hermes-mcp-server/tests` ⚠️（环境缺少 pytest/fastapi/pydantic，已记录豁免）
4. 文档契约与代码一致性人工核对（`docs/architecture/mcp-tools.md`）✅
5. 只读边界与审批语义核对（不执行真实写操作）✅
