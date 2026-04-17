# XY05 长任务模式任务看板（000~00n）

> 任务主题：XY05 playwright-h5 readonly adapter  
> 创建日期：2026-04-17  
> 任务规范：`用户任务说明（XY05）` + `/vol1/1000/codexcli/AGENTS.md` + `AGENTS.md`  
> 启动报告：`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/000-high-roi-xy05-playwright-h5-readonly-adapter-roadmap-2026-04-17.md`  
> 执行日志：`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/xy05-log.md`

## 1. 状态定义

- `Todo`：未开始
- `In Progress`：进行中
- `Blocked`：受阻
- `Done`：完成并附证据
- `Done (Waived)`：完成但有豁免说明

## 2. 看板主表

| ID | 优先级 | 任务 | 状态 | 验收标准 | 证据路径 |
|---|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结（长任务模式建档） | Done | 路线图、看板、日志、模板齐备且口径可执行 | `spec/tasks/playwright-h5-readonly-adapter-2026-04-17/000-high-roi-xy05-playwright-h5-readonly-adapter-roadmap-2026-04-17.md`；`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/xy05-taskboard-2026-04-17.md`；`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/xy05-log.md`；`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/xy05-task-report-template.md` |
| 001 | P0 | `playwright_h5` offline/mock adapter 实现 | Done | adapter 不再抛 `NotImplementedError`；存在 settings/session placeholder/extraction pipeline/fixture-backed path | `apps/hermes-mcp-server/app/adapters/read_providers/playwright_h5.py`；`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/001-playwright-h5-offline-adapter-report-2026-04-17.md` |
| 002 | P0 | resolver 与 provider 兼容性校验 | Done | `playwright_h5` 可被 resolver 选中；默认 `demo` 保持不变 | `apps/hermes-mcp-server/tests/test_read_provider_resolver.py`；`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/002-resolver-compat-report-2026-04-17.md` |
| 003 | P0 | 测试与文档更新 | Done | 新增 offline/mock adapter 测试；README 和 mcp-tools 文档更新 | `apps/hermes-mcp-server/tests/test_playwright_h5_adapter.py`；`README.md`；`docs/architecture/mcp-tools.md`；`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/003-tests-doc-contract-report-2026-04-17.md` |
| 004 | P0 | 门禁执行与证据沉淀 | Done | pytest、compileall、compose config 通过并留痕 | `spec/tasks/playwright-h5-readonly-adapter-2026-04-17/004-validation-gates-output-2026-04-17.txt`；`spec/tasks/playwright-h5-readonly-adapter-2026-04-17/004-validation-gates-report-2026-04-17.md` |
| 00n | P0 | 全局翻盘审查与结题 | Done | 输出结题报告，含 KPI/门禁/兼容性/风险/下一步 | `spec/tasks/playwright-h5-readonly-adapter-2026-04-17/00n-global-review-report-2026-04-17.md` |

## 3. 统一门禁（每任务完成必跑）

1. `PYTHONPATH=apps/hermes-mcp-server .venv/bin/python -m pytest apps/hermes-mcp-server/tests -q` ✅
2. `python3 -m compileall apps packages` ✅
3. `docker compose -f infra/compose/docker-compose.yml config` ✅
4. 文档一致性核对：`README.md` + `docs/architecture/mcp-tools.md` ✅
5. 安全边界核对：不连接真实闲鱼、不执行真实 Playwright 浏览或写操作 ✅
