# 000 高收益路线图：XY05 Playwright-H5 Read-Only Adapter

> 任务ID：000  
> 日期：2026-04-17  
> 状态：Done  
> 主规范：`用户任务说明（XY05）`、`/vol1/1000/codexcli/AGENTS.md`、`/vol1/1000/codexcli/xianyu-agent-platform/AGENTS.md`

## 1. 目标

1. 把 `playwright_h5` adapter 从纯占位实现升级为有意义的 offline/mock 只读 adapter。
2. 保持 XY04 形成的 resolver 架构、默认 `demo` provider 与现有 API 契约不变。
3. 为后续真实浏览器/H5 采集接入预留 session/config/extraction pipeline 结构，但当前不连接真实闲鱼。
4. 补齐测试、文档与长任务资产，确保变更可验证、可追溯。

## 2. 高收益批次策略（ROI）

1. 先做：冻结 XY05 范围和门禁，明确“不连真实闲鱼、只做 offline/mock”的边界。
2. 再做：实现 `playwright_h5.py` 的最小可用 offline/mock adapter，并通过 resolver 可选中。
3. 最后做：补测试、补文档、跑门禁、回填报告并收口。

## 3. 起始基线（2026-04-17）

| 指标 | 当前值 | 目标值 | 备注 |
|---|---:|---:|---|
| `playwright_h5` adapter 行为 | 仅抛 `NotImplementedError` | 可返回 offline/mock envelopes | 不触网 |
| `playwright_h5` 专项测试 | 0 | >= 4 | dashboard/orders/items/unread chats |
| 测试总数 | 21 | >= 25 | 保持全绿 |
| 默认 provider 行为 | demo | demo | 不改变 |

## 4. 任务拆解建议

| ID | 优先级 | 任务 | 预期收益 | 风险 |
|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结 | 执行边界、门禁与证据规则收敛 | 低 |
| 001 | P0 | `playwright_h5` offline/mock adapter 实现 | adapter 不再是死占位 | 中 |
| 002 | P0 | resolver 与 provider 行为兼容性校验 | 默认 demo 保持、playwright_h5 可安全选择 | 中 |
| 003 | P0 | 测试与文档更新 | 变更可回归、边界清晰 | 低 |
| 004 | P0 | 门禁执行与证据沉淀 | 质量收口 | 低 |
| 00n | P0 | 全局翻盘审查与结题 | KPI/风险/下一步汇总 | 中 |

## 5. 统一门禁

1. `PYTHONPATH=apps/hermes-mcp-server .venv/bin/python -m pytest apps/hermes-mcp-server/tests -q`
2. `python3 -m compileall apps packages`
3. `docker compose -f infra/compose/docker-compose.yml config`
4. 文档一致性核对：`README.md`、`docs/architecture/mcp-tools.md`
5. 安全边界核对：不连接真实闲鱼、不执行真实 Playwright 浏览或写操作

## 6. 风险控制

- 风险1：为了做“真一点”的 adapter 而误接入真实网络。
  - 控制措施：只实现 fixture/mock path；明确 offline_mode 默认开启。
  - 回滚策略：保留 demo provider 作为默认值。
- 风险2：破坏现有 resolver 或 demo 行为。
  - 控制措施：新增专项测试，确保 `demo` provider 与现有路由继续通过。
  - 回滚策略：`XIANYU_READ_PROVIDER` 默认仍为 `demo`。
- 风险3：文档与代码分层描述不一致。
  - 控制措施：本批同步更新 README 与 mcp-tools 文档。
  - 回滚策略：以测试与实现为准重新收口文档。

## 7. 节奏

- Day 0 / Hour 0：完成 000 建档与口径冻结。
- Day 0 / Hour 1：完成 001（adapter offline/mock 实现）。
- Day 0 / Hour 2：完成 002/003（resolver 兼容验证 + 测试/文档）。
- Day 0 / Hour 3：完成 004/00n（门禁、报告、结题）。

## 8. 000 结论

- 长任务资产：已建立并完成实化。
- 可立即推进的下一任务：`001`。
- 需用户决策项：无。
