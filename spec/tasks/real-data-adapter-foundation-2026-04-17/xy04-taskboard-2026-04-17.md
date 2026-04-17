# XY04 长任务模式任务看板（000~00n）

> 任务主题：XY04 real-data adapter foundation  
> 创建日期：2026-04-17  
> 任务规范：`用户任务说明（XY04）` + `/vol1/1000/codexcli/AGENTS.md` + `AGENTS.md`  
> 启动报告：`spec/tasks/real-data-adapter-foundation-2026-04-17/000-high-roi-xy04-real-data-adapter-foundation-roadmap-2026-04-17.md`  
> 执行日志：`spec/tasks/real-data-adapter-foundation-2026-04-17/xy04-log.md`

## 1. 状态定义

- `Todo`：未开始
- `In Progress`：进行中
- `Blocked`：受阻
- `Done`：完成并附证据
- `Done (Waived)`：完成但有豁免说明

## 2. 看板主表

| ID | 优先级 | 任务 | 状态 | 验收标准 | 证据路径 |
|---|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结（长任务模式建档） | Done | 路线图、看板、日志、模板齐备且口径可执行 | `spec/tasks/real-data-adapter-foundation-2026-04-17/000-high-roi-xy04-real-data-adapter-foundation-roadmap-2026-04-17.md`；`spec/tasks/real-data-adapter-foundation-2026-04-17/xy04-taskboard-2026-04-17.md`；`spec/tasks/real-data-adapter-foundation-2026-04-17/xy04-log.md`；`spec/tasks/real-data-adapter-foundation-2026-04-17/xy04-task-report-template.md` |
| 001 | P0 | provider/adapter 抽象与目录骨架 | Done | 存在 read-only provider 协议/抽象；新增 adapter 模块结构可挂载未来实现；不接入真实闲鱼 | `apps/hermes-mcp-server/app/adapters/read_providers/base.py`；`apps/hermes-mcp-server/app/adapters/read_providers/__init__.py`；`apps/hermes-mcp-server/app/adapters/read_providers/demo.py`；`apps/hermes-mcp-server/app/adapters/read_providers/playwright_h5.py`；`apps/hermes-mcp-server/app/adapters/read_providers/real_upstream.py`；`spec/tasks/real-data-adapter-foundation-2026-04-17/001-provider-abstraction-structure-report-2026-04-17.md` |
| 002 | P0 | demo provider 适配抽象 + resolver 接线 | Done | FastAPI 通过 resolver 获取 provider；demo provider 实现抽象；路由/契约保持兼容 | `apps/hermes-mcp-server/app/main.py`；`apps/hermes-mcp-server/app/services/read_provider_resolver.py`；`apps/hermes-mcp-server/app/services/read_foundation.py`；`apps/hermes-mcp-server/app/services/dashboard.py`；`spec/tasks/real-data-adapter-foundation-2026-04-17/002-demo-provider-resolver-wiring-report-2026-04-17.md` |
| 003 | P0 | 测试与文档契约更新 | Done | 新增/更新 abstraction/resolver 测试；endpoint 回归保持绿；README + mcp-tools 反映新分层 | `apps/hermes-mcp-server/tests/test_read_provider_resolver.py`；`README.md`；`docs/architecture/mcp-tools.md`；`spec/tasks/real-data-adapter-foundation-2026-04-17/003-tests-doc-contract-report-2026-04-17.md` |
| 004 | P0 | 门禁执行与证据沉淀 | Done | `.venv` pytest、compileall、compose config 结果完整留痕 | `spec/tasks/real-data-adapter-foundation-2026-04-17/004-validation-gates-output-2026-04-17.txt`；`spec/tasks/real-data-adapter-foundation-2026-04-17/004-validation-gates-report-2026-04-17.md` |
| 00n | P0 | 全局翻盘审查与结题 | Done | 输出结题报告，含 KPI/门禁/兼容性/风险/下一步 | `spec/tasks/real-data-adapter-foundation-2026-04-17/00n-global-review-report-2026-04-17.md` |

## 3. 统一门禁（每任务完成必跑）

1. `PYTHONPATH=apps/hermes-mcp-server .venv/bin/python -m pytest apps/hermes-mcp-server/tests` ✅
2. `.venv/bin/python -m compileall apps packages` / `python3 -m compileall apps packages` ✅
3. `docker compose -f infra/compose/docker-compose.yml config` ✅
4. 契约文档一致性核对：`README.md` + `docs/architecture/mcp-tools.md` ✅
5. 只读边界核对：不连接真实闲鱼、不执行真实写操作、审批边界描述保持 ✅
