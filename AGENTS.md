# 项目级 AGENTS 说明

本项目位于 `/vol1/1000/codexcli/` 之下，默认继承上层：
- `/vol1/1000/codexcli/AGENTS.md`

## 1. 项目元信息

- 项目名称：`xianyu-agent-platform`
- 项目根目录：`/vol1/1000/codexcli/xianyu-agent-platform`
- 仓库类型：独立子项目仓库

## 2. 项目特有约束

- 技术栈：Python 3.11+、FastAPI、Pydantic、Playwright、PostgreSQL、Redis、Docker Compose
- 启动命令：`PYTHONPATH=apps/hermes-mcp-server python -m app.main`
- 测试命令：`python -m compileall apps packages`
- 构建命令：`docker compose -f infra/compose/docker-compose.yml config`
- 发布门禁：至少通过 compileall、compose config、自检文档核对
- 禁止改动目录：`spec/archive/`
- 契约文件位置：`docs/architecture/mcp-tools.md`、`docs/architecture/database-schema.md`

## 3. 建议工作方式

1. 在本项目根目录启动 `codex`
2. 中大型任务先进入长任务模式
3. 长任务资产统一放在 `spec/tasks/<topic>-YYYY-MM-DD/`
4. 任何新增工具都要先更新 `docs/architecture/mcp-tools.md`
5. 任何高风险写操作都必须先定义审批语义与审计证据

## 4. 当前项目补充说明

- 当前阶段是 MVP-0 初始化，不接真实闲鱼账号，不执行真实写操作。
- 若引入页面自动化，优先保持“读操作优先、写操作审批、失败可回放”的边界。
- 任何数据库表设计变更都要同步更新架构文档和任务资产。
