# 000 高收益路线图：XY02 MVP-1 Read-Only Foundation

> 任务ID：000  
> 日期：2026-04-17  
> 状态：Done  
> 主规范：`用户任务说明（XY02 MVP-1 read-only foundation）`、`/vol1/1000/codexcli/AGENTS.md`、`/vol1/1000/codexcli/xianyu-agent-platform/AGENTS.md`

## 1. 目标

1. 在 `packages/xianyu-schemas` 建立 MVP-1 只读基础共享 schema/model（dashboard、orders、items、unread chats、reply suggestion、daily report）。
2. 在 `apps/hermes-mcp-server` 暴露只读 FastAPI 工具端点，返回结构化、可测试、可扩展的 demo 数据。
3. 建立服务层 demo provider + 测试 + 文档收口，确保后续接入真实数据源时契约稳定。

## 2. 高收益批次策略（ROI）

1. 先做（高收益/低风险）：冻结契约与数据模型，明确只读边界和写操作审批预留字段。
2. 再做（核心交付）：实现服务层 demo provider 与 API 路由，形成最小可运行闭环。
3. 最后做（收口治理）：补齐测试、门禁验证、文档契约、任务报告和结题复盘。

## 3. 起始基线（2026-04-17）

| 指标 | 当前值 | 目标值 | 备注 |
|---|---:|---:|---|
| MVP-1 目标只读工具端点数 | 1 | 6 | 当前仅 `/demo/dashboard` |
| 共享 schema/model 数 | 0 | >= 12 | 覆盖 6 类工具输入输出 |
| 服务层 demo provider 覆盖工具数 | 1 | 6 | 当前仅 dashboard demo |
| 针对新工具的自动化测试数 | 1 | >= 8 | 新增 schema/service/api 维度 |
| 发布门禁通过率 | 0/2 | 2/2 | `compileall` + `compose config` |

## 4. 任务拆解建议

| ID | 优先级 | 任务 | 预期收益 | 风险 |
|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结 | 长任务资产与验收口径一致 | 低 |
| 001 | P0 | 共享 schema/model 与 demo provider 设计实现 | 契约稳定、服务可复用 | 中 |
| 002 | P0 | FastAPI 只读端点实现与集成 | 对外 API 面形成闭环 | 中 |
| 003 | P0 | 测试补齐（schema/service/endpoint）与文档更新 | 可验证、可回归、可交接 | 中 |
| 004 | P0 | 门禁执行与证据沉淀（compileall/compose/pytest） | 发布前质量收口 | 中 |
| 00n | P0 | 全局翻盘审查与结题 | KPI、风险、兼容性、后续计划完整 | 中 |

## 5. 统一门禁

1. `python -m compileall apps packages`
2. `docker compose -f infra/compose/docker-compose.yml config`
3. `python -m pytest apps/hermes-mcp-server/tests`
4. 人工契约核对：`docs/architecture/mcp-tools.md` 与 FastAPI 实现一致
5. 人工边界核对：只读工具不触发真实闲鱼写操作，写操作审批边界文档保留

## 6. 风险控制

- 风险1：read-only 接口命名与工具契约不一致。
  - 控制措施：统一以 `xianyu_*` tool 语义命名并更新契约文档。
  - 回滚策略：保留旧 `/demo/dashboard` 兼容路由，新增路由逐步切流。
- 风险2：demo 数据结构松散导致后续接真实源改动过大。
  - 控制措施：先固化 Pydantic 模型，服务层按模型产出。
  - 回滚策略：接口保持字段兼容，内部 provider 可替换。
- 风险3：误引入真实写动作。
  - 控制措施：本批仅只读/建议，明确 `approval_required_for_send=true` 仅作为提示，不执行发送。
  - 回滚策略：若发现副作用代码，立即移除并在看板标记 Blocked 复核。

## 7. 节奏

- Day 0 / Hour 0：完成 000 建档与口径冻结。
- Day 0 / Hour 1：完成 001（schema + provider）。
- Day 0 / Hour 2：完成 002/003（endpoint + test + doc）。
- Day 0 / Hour 3：完成 004/00n（门禁 + 报告 + 结题）。

## 8. 000 结论

- 长任务资产：已建立并完成实化更新。
- 可立即推进的下一任务：`001`。
- 需用户决策项：无。
