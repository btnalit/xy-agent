# 000 高收益路线图：XY03 Environment Bootstrap and GitHub Push Prep

> 任务ID：000  
> 日期：2026-04-17  
> 状态：Done  
> 主规范：`用户要求由 Hermes 直接管理 Codex CLI 持续推进项目`、`/vol1/1000/codexcli/AGENTS.md`、`/vol1/1000/codexcli/xianyu-agent-platform/AGENTS.md`

## 1. 目标

1. 在当前宿主环境中建立可运行的 Python 3.11 虚拟环境，并安装 XY02 所需运行/测试依赖。
2. 通过系统化调试修复 hermes-mcp-server 当前在 Python 3.11 + Pydantic v2 下的启动/测试失败问题。
3. 完成 XY03 的验证、文档收口、GitHub 远端绑定与后续推送准备。

## 2. 高收益批次策略（ROI）

1. 先做：绑定 GitHub 远端、建立 venv、安装依赖，消除“无法验证”的基础阻塞。
2. 再做：复现失败、定位根因、最小修复，并让 pytest / 启动 / compileall / compose config 通过。
3. 最后做：回写任务资产、生成正式报告、准备首次提交与推送。

## 3. 起始基线（2026-04-17）

| 指标 | 当前值 | 目标值 | 备注 |
|---|---:|---:|---|
| 可运行虚拟环境 | 0 | 1 | `.venv` 建立并安装依赖 |
| hermes-mcp-server 测试通过数 | 0/13 | 13/13 | XY02 当时因缺依赖未通过 |
| API 启动状态 | 失败 | 成功 | 至少完成启动/关闭 smoke |
| GitHub 远端绑定 | 0 | 1 | 绑定 `btnalit/xy-agent` |
| 长任务资产实化程度 | 模板 | 完整 | 路线图/看板/日志/报告齐全 |

## 4. 任务拆解建议

| ID | 优先级 | 任务 | 预期收益 | 风险 |
|---|---|---|---|---|
| 000 | P0 | 启动与口径冻结 | 长任务资产与执行边界一致 | 低 |
| 001 | P0 | 环境引导与 GitHub 远端准备 | 建立验证与推送基础 | 低 |
| 002 | P0 | 根因定位与运行时兼容修复 | 让测试与 API 启动恢复 | 中 |
| 003 | P0 | 门禁验证与文档收口 | 形成可复核交付物 | 低 |
| 004 | P0 | 推送准备与证据沉淀 | 为首次提交/推送做收口 | 低 |
| 00n | P0 | 全局翻盘审查与结题 | 汇总 KPI、风险、验证、后续动作 | 中 |

## 5. 统一门禁

1. `. .venv/bin/activate && PYTHONPATH=apps/hermes-mcp-server python -m pytest apps/hermes-mcp-server/tests -q`
2. `timeout 10s env PYTHONPATH=apps/hermes-mcp-server .venv/bin/python -m app.main`
3. `python3 -m compileall apps packages`
4. `docker compose -f infra/compose/docker-compose.yml config`
5. Git 远端与身份配置核对：`git remote -v`、`git config user.name`、`git config user.email`

## 6. 风险控制

- 风险1：运行时为 Python 3.11，而项目文档/配置原先偏向 3.12。
  - 控制措施：修正 `requires-python` 与文档表述到与真实环境一致。
  - 回滚策略：若后续迁移到 3.12，再单独开批次调整。
- 风险2：Pydantic 在类型解析阶段因字段名与类型名冲突导致收集失败。
  - 控制措施：先复现并确认根因，再做最小别名修复。
  - 回滚策略：若修复不兼容，保持 schema 字段名不变，仅调整内部类型引用。
- 风险3：GitHub 推送凭据暴露风险。
  - 控制措施：Hermes 仅临时使用用户提供凭据进行推送准备，不写入仓库文件。
  - 回滚策略：推送完成后建议用户旋转/撤销该 PAT。

## 7. 节奏

- Day 0 / Hour 0：完成 000 建档与口径冻结。
- Day 0 / Hour 1：完成 001（venv + 依赖 + GitHub 远端）。
- Day 0 / Hour 2：完成 002（根因修复与兼容性调整）。
- Day 0 / Hour 3：完成 003/004/00n（验证、文档、结题与推送准备）。

## 8. 000 结论

- 长任务资产：`已建立并完成实化`
- 可立即推进的下一任务：`001`
- 需用户决策项：`无`
