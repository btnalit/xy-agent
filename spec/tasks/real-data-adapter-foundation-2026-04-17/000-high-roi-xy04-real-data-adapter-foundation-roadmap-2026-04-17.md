# 000 高收益路线图：XY04 Real-Data Adapter Foundation

> 任务ID：000  
> 日期：2026-04-17  
> 状态：Done  
> 主规范：`用户任务说明（XY04）`、`/vol1/1000/codexcli/AGENTS.md`、`/vol1/1000/codexcli/xianyu-agent-platform/AGENTS.md`

## 1. 目标

1. 建立“只读数据源 provider/adapter 抽象层”，为后续 Playwright/H5/真实上游接入预留稳定扩展位。
2. 将现有 `DemoReadFoundationProvider` 迁移到抽象层下运行，并保持现有 API 路由与响应契约完全兼容。
3. 引入 provider resolver/factory，让 FastAPI 通过抽象解析 provider，消除直接硬编码 demo provider 的耦合。
4. 补齐抽象层与兼容性测试，确保当前 demo 行为不退化、测试继续全绿。

## 2. 高收益批次策略（ROI）

1. 先做（高收益/低风险）：冻结任务口径、验收标准、门禁与证据路径（000）。
2. 再做（核心重构）：新增 adapter 抽象 + demo provider 适配 + resolver 接线，保持接口行为不变（001/002）。
3. 最后做（收口）：补测试、补文档、执行门禁、产出报告与结题复盘（003/004/00n）。

## 3. 起始基线（2026-04-17）

| 指标 | 当前值 | 目标值 | 备注 |
|---|---:|---:|---|
| provider 抽象层（接口/协议） | 0 | 1 | 需支持 6 个 read-only tool 能力点 |
| provider 解析方式 | main.py 直接 new demo provider | 通过 resolver/factory 解析 | 对外 API 不变 |
| 可挂载 adapter 实现目录 | 0 | >= 1 结构化目录 | 预留 Playwright/H5/real upstream 扩展位 |
| hermes read-only API 路由兼容性 | 已稳定 | 100% 保持 | 不改路径/方法/字段 |
| 自动化测试通过数 | 13/13 | >=13/13 | 在 `.venv` 内执行 |

## 4. 任务拆解建议

| ID | 优先级 | 任务 | 预期收益 | 风险 |
|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结 | 长任务执行面与证据规则一次性收敛 | 低 |
| 001 | P0 | provider/adapter 抽象与目录骨架 | 明确扩展点，降低未来真实源接入改动面 | 中 |
| 002 | P0 | demo provider 重构 + resolver 接线 | 保持现有 API 行为并解除硬编码耦合 | 中 |
| 003 | P0 | 测试与文档契约更新 | 回归可验证，架构说明与代码同步 | 中 |
| 004 | P0 | 门禁执行与证据沉淀 | 发布前质量收口可追溯 | 中 |
| 00n | P0 | 全局翻盘审查与结题 | 汇总 KPI/兼容性/风险/下一步 | 中 |

## 5. 统一门禁

1. `PYTHONPATH=apps/hermes-mcp-server .venv/bin/python -m pytest apps/hermes-mcp-server/tests`
2. `.venv/bin/python -m compileall apps packages`
3. `docker compose -f infra/compose/docker-compose.yml config`
4. 人工契约核对：`docs/architecture/mcp-tools.md`、`README.md` 与实现一致
5. 只读边界核对：不连接真实闲鱼、不执行真实写操作、保留审批边界语义

## 6. 风险控制

- 风险1：重构 provider 后破坏现有 API 返回结构。
  - 控制措施：保持 response_model 不变并保留现有 endpoint 测试回归。
  - 回滚策略：resolver 默认仍指向 demo adapter，可快速切回。
- 风险2：过度设计导致 MVP 阶段复杂度上升。
  - 控制措施：仅引入最小抽象（协议 + registry + demo 实现），不提前接真实系统。
  - 回滚策略：保留 demo provider 逻辑完整可独立运行。
- 风险3：未来写操作边界在抽象层被模糊。
  - 控制措施：接口仅覆盖 read-only 能力，建议接口继续返回审批提示，不提供写 API。
  - 回滚策略：文档和测试中持续固定只读边界。

## 7. 节奏

- Day 0 / Hour 0：完成 000 建档与口径冻结。
- Day 0 / Hour 1：完成 001（抽象层与 adapter 目录骨架）。
- Day 0 / Hour 2：完成 002（demo provider 适配 + resolver 接线）。
- Day 0 / Hour 3：完成 003（测试+文档）与 004（门禁）。
- Day 0 / Hour 4：完成 00n 结题审查。

## 8. 000 结论

- 长任务资产：已建立并实化更新。
- 可立即推进的下一任务：`001`。
- 需用户决策项：无。
