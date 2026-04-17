# XY03 长任务模式任务看板（000~00n）

> 任务主题：XY03 environment bootstrap and GitHub push prep  
> 创建日期：2026-04-17  
> 任务规范：`用户要求 Hermes 直接管理 Codex CLI 持续推进项目` + `/vol1/1000/codexcli/AGENTS.md` + `AGENTS.md`  
> 启动报告：`spec/tasks/env-bootstrap-and-github-push-2026-04-17/000-high-roi-xy03-env-bootstrap-and-github-push-roadmap-2026-04-17.md`  
> 执行日志：`spec/tasks/env-bootstrap-and-github-push-2026-04-17/xy03-log.md`

## 1. 状态定义

- `Todo`：未开始
- `In Progress`：进行中
- `Blocked`：受阻
- `Done`：完成并附证据
- `Done (Waived)`：完成但有豁免说明

## 2. 看板主表

| ID | 优先级 | 任务 | 状态 | 验收标准 | 证据路径 |
|---|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结（长任务模式建档） | Done | 路线图、看板、日志、模板齐备并具备可执行口径 | `spec/tasks/env-bootstrap-and-github-push-2026-04-17/000-high-roi-xy03-env-bootstrap-and-github-push-roadmap-2026-04-17.md`；`spec/tasks/env-bootstrap-and-github-push-2026-04-17/xy03-taskboard-2026-04-17.md`；`spec/tasks/env-bootstrap-and-github-push-2026-04-17/xy03-log.md`；`spec/tasks/env-bootstrap-and-github-push-2026-04-17/xy03-task-report-template.md` |
| 001 | P0 | 环境引导与 GitHub 远端准备 | Done | `.venv` 创建、依赖安装、git identity 与 origin 远端配置完成 | `.venv/`；`git remote -v`；`git config user.name`；`git config user.email`；`spec/tasks/env-bootstrap-and-github-push-2026-04-17/001-env-and-remote-bootstrap-report-2026-04-17.md` |
| 002 | P0 | 根因定位与运行时兼容修复 | Done | 确认 Pydantic 注解冲突为根因；修复后 hermes-mcp-server 测试可收集并通过；运行时版本约束与文档一致 | `packages/xianyu-schemas/xianyu_schemas/tools.py`；`pyproject.toml`；`README.md`；`AGENTS.md`；`spec/tasks/env-bootstrap-and-github-push-2026-04-17/002-runtime-compat-fix-report-2026-04-17.md` |
| 003 | P0 | 门禁验证与文档收口 | Done | pytest、启动 smoke、compileall、compose config 通过；README 反映真实依赖与运行方式 | `spec/tasks/env-bootstrap-and-github-push-2026-04-17/003-validation-and-docs-report-2026-04-17.md`；`README.md` |
| 004 | P0 | 推送准备与证据沉淀 | Done | GitHub 远端就绪、工作区收口、任务资产与验证证据齐全 | `spec/tasks/env-bootstrap-and-github-push-2026-04-17/004-push-prep-report-2026-04-17.md` |
| 00n | P0 | 全局翻盘审查与结题 | Done | 输出结题报告，汇总 KPI、门禁、风险与下一步 | `spec/tasks/env-bootstrap-and-github-push-2026-04-17/00n-global-review-report-2026-04-17.md` |

## 3. 统一门禁（每任务完成必跑）

1. `. .venv/bin/activate && PYTHONPATH=apps/hermes-mcp-server python -m pytest apps/hermes-mcp-server/tests -q` ✅
2. `timeout 10s env PYTHONPATH=apps/hermes-mcp-server .venv/bin/python -m app.main` ✅（以超时 124 正常退出，但服务完成启动/关闭日志）
3. `python3 -m compileall apps packages` ✅
4. `docker compose -f infra/compose/docker-compose.yml config` ✅
5. `git remote -v`、`git config user.name`、`git config user.email` ✅
