# Xianyu Agent Platform

Hermes 驱动的闲鱼运营副驾驶项目骨架。

目标定位：
- Hermes Agent 负责理解、决策、编排
- Xianyu MCP Server 负责工具暴露、状态聚合、审批与审计边界
- Automation Worker 负责 Playwright 浏览器自动化、会话保持、节流与失败回放

## 当前阶段

本仓库已完成 MVP-1 第一批可交付（只读基础能力），并在 XY04 完成 real-data adapter foundation：
- 共享 schema/model：dashboard、orders、items、unread chats、reply suggestion、daily report
- Hermes MCP Server 只读工具端点（默认 demo provider）
- read-only provider 抽象 + adapter 目录骨架（demo / playwright_h5 placeholder / real_upstream placeholder）
- provider resolver/factory（通过 `XIANYU_READ_PROVIDER` 选择，默认 `demo`）
- schema/service/endpoint 测试与基础门禁
- 契约文档更新（`docs/architecture/mcp-tools.md`）

## 推荐技术栈

- Python 3.11+
- FastAPI
- Pydantic v2
- SQLAlchemy（后续接入）
- Redis
- PostgreSQL
- Playwright
- Docker Compose

## 目录结构

```text
apps/
  hermes-mcp-server/     # MCP / API 入口
  automation-worker/     # 浏览器自动化 worker
  admin-console/         # 运营后台占位
packages/
  xianyu-core/           # 领域模型与配置
  xianyu-schemas/        # MCP/DTO/schema
  xianyu-playwright/     # 浏览器自动化封装
  xianyu-audit/          # 审计、快照、证据接口
infra/
  compose/               # docker compose 骨架
  docker/                # Dockerfile 占位
docs/
  architecture/          # 系统设计文档
  runbooks/              # 运维与审批手册
  prompts/               # Hermes 提示词约束
spec/
  tasks/                 # 长任务模式资产
```

## MVP-1 已实现只读工具

- `GET /tools/xianyu_get_dashboard`
- `GET /tools/xianyu_list_orders`
- `GET /tools/xianyu_list_items`
- `GET /tools/xianyu_list_unread_chats`
- `POST /tools/xianyu_suggest_reply`（只返回草稿，不发送）
- `GET /tools/xianyu_daily_report`

> 所有接口均为 demo 数据，且统一返回 `request_id` 与 `evidence_refs`。

## Adapter 解析方式（XY04）

- 默认 provider：`demo`
- 环境变量：`XIANYU_READ_PROVIDER`
- 目前可解析 key：
  - `demo`：可用，当前默认
  - `playwright_h5`：占位实现（未接真实闲鱼）
  - `real_upstream`：占位实现（未接真实闲鱼）

## 快速开始

```bash
cd /vol1/1000/codexcli/xianyu-agent-platform
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e packages/xianyu-schemas
pip install fastapi uvicorn pydantic pytest httpx
PYTHONPATH=apps/hermes-mcp-server python -m app.main
```

## 验证命令

```bash
python -m compileall apps packages
docker compose -f infra/compose/docker-compose.yml config
PYTHONPATH=apps/hermes-mcp-server python -m pytest apps/hermes-mcp-server/tests
```

## 长任务规范

本项目继承 `/vol1/1000/codexcli/AGENTS.md` 的长任务模式要求。
当前批次资产位于：
- `spec/tasks/real-data-adapter-foundation-2026-04-17/`

## 安全边界提醒

- 当前不接入真实闲鱼账号。
- 当前不执行真实写操作。
- 回复发送、改价、上/下架等写操作必须审批并留痕审计。
