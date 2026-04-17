# Xianyu Agent Platform 系统设计

## 1. 目标

构建一个“Hermes 驱动的闲鱼运营副驾驶”，默认辅助、逐步自动、高风险动作审批。

## 2. 总体架构

```text
[Hermes Agent]
    │
    │ MCP tools
    ▼
[Xianyu MCP Server]
    │
    ├── Order Service
    ├── Item Service
    ├── Chat Service
    ├── Workflow Service
    ├── Approval Service
    └── Audit / Memory Adapter
    │
    ▼
[Automation Worker Layer]
    ├── Playwright browser workers
    ├── Session/Profile manager
    ├── Cookie/Login keeper
    ├── DOM extractor / H5 API wrapper
    └── Risk-control throttler
    │
    ▼
[Xianyu Web / H5]
```

旁路组件：PostgreSQL、Redis、MinIO、Prometheus、Grafana。

## 3. 分层职责

### Hermes Agent
- 理解自然语言运营目标
- 调用 MCP 工具
- 汇总日报、建议、回复草稿
- 对高风险动作发起审批

### Xianyu MCP Server
- 暴露业务语义级工具
- 聚合订单、商品、消息、任务视图
- 持久化任务、审批、审计日志
- 为 Worker 提供统一任务入口

### Automation Worker
- 管理浏览器 profile
- 保持登录态
- 控制节流、代理、随机化行为
- 采集页面与执行真实交互

## 4. 实施阶段

### MVP-1：只读 + 建议
- dashboard
- orders
- items
- unread chats
- reply suggestion
- daily report

### MVP-2：低风险写操作
- send reply
- edit item
- adjust price
- toggle item status

### MVP-3：强副作用动作
- ship order
- bulk pricing
- publish item
- follow-up automation

## 5. 安全边界

1. 一账号一 profile
2. 所有写操作走任务队列
3. 高风险动作强制审批
4. 每次执行保留截图、DOM 快照、参数、结果
5. 失败任务可重试、可人工接管、可回放
