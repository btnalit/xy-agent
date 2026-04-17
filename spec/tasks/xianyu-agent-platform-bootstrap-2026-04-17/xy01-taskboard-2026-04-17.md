# XY01 长任务模式任务看板（000~00n）

> 任务主题：xianyu-agent-platform-bootstrap  
> 创建日期：2026-04-17  
> 任务规范：`用户提供的“闲鱼运营副驾驶”系统方案 + /vol1/1000/codexcli/AGENTS.md`  
> 启动报告：`spec/tasks/xianyu-agent-platform-bootstrap-2026-04-17/000-high-roi-xy01-xianyu-agent-platform-bootstrap-roadmap-2026-04-17.md`  
> 执行日志：`spec/tasks/xianyu-agent-platform-bootstrap-2026-04-17/xy01-log.md`

## 1. 状态定义

- `Todo`：未开始
- `In Progress`：进行中
- `Blocked`：受阻
- `Done`：完成并附证据
- `Done (Waived)`：完成但有豁免说明

## 2. 看板主表

| ID | 优先级 | 任务 | 状态 | 验收标准 | 证据路径 |
|---|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结（长任务模式建档） | Done | 启动报告、看板、日志、模板齐备 | `spec/tasks/xianyu-agent-platform-bootstrap-2026-04-17/000-high-roi-xy01-xianyu-agent-platform-bootstrap-roadmap-2026-04-17.md`；`spec/tasks/xianyu-agent-platform-bootstrap-2026-04-17/xy01-taskboard-2026-04-17.md`；`spec/tasks/xianyu-agent-platform-bootstrap-2026-04-17/xy01-log.md`；`spec/tasks/xianyu-agent-platform-bootstrap-2026-04-17/xy01-task-report-template.md` |
| 001 | P0 | 初始化项目骨架与目录结构 | Done | apps/packages/infra/docs 目录齐备，README/AGENTS 已项目化 | `README.md`；`AGENTS.md`；`apps/`；`packages/`；`infra/`；`docs/` |
| 002 | P0 | 补齐架构、契约、数据库与部署文档 | Done | 系统设计、MCP tools、数据库、审批策略、compose 骨架存在 | `docs/architecture/system-design.md`；`docs/architecture/mcp-tools.md`；`docs/architecture/database-schema.md`；`docs/runbooks/approval-policy.md`；`infra/compose/docker-compose.yml` |
| 003 | P1 | 加入最小应用代码骨架与配置示例 | Done | FastAPI/worker/package 占位代码与 `.env.example` 可用 | `apps/hermes-mcp-server/app/main.py`；`apps/automation-worker/app/main.py`；`packages/xianyu-core/xianyu_core/config.py`；`packages/xianyu-schemas/xianyu_schemas/tools.py`；`.env.example` |
| 00n | P0 | 全局翻盘审查与结题 | Done | 输出结题报告，KPI/风险/门禁结论完整 | `spec/tasks/xianyu-agent-platform-bootstrap-2026-04-17/00n-global-review-report-2026-04-17.md`；`python3 -m compileall apps packages`；`docker compose -f infra/compose/docker-compose.yml config` |

## 3. 统一门禁（每任务完成必跑）

1. `python -m compileall apps packages`
2. `docker compose -f infra/compose/docker-compose.yml config`
3. 文档与 AGENTS 约束人工核对
4. 项目目录结构检查
5. Git 状态与关键文件存在性检查
