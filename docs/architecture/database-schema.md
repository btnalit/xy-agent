# 数据库表结构草案

## 核心表

### accounts
- id
- platform
- login_state
- last_login_check_at
- risk_level
- proxy_id
- session_valid_until

### browser_profiles
- id
- account_id
- browser_profile_path
- user_data_dir
- last_used_at

### items
- id
- account_id
- platform_item_id
- title
- status
- price
- stock
- views
- favorites
- last_synced_at

### orders
- id
- account_id
- platform_order_id
- buyer_name
- status
- total_amount
- created_at
- updated_at
- last_synced_at

### chat_threads
- id
- account_id
- platform_thread_id
- buyer_name
- unread_count
- last_message_at
- last_synced_at

### chat_messages
- id
- thread_id
- sender_role
- content
- sent_at

### tasks
- id
- account_id
- task_type
- status
- priority
- payload_json
- retry_count
- created_at
- updated_at

### task_runs
- id
- task_id
- started_at
- finished_at
- status
- error_message
- screenshot_path
- dom_snapshot_path

### approvals
- id
- task_id
- approver
- status
- reason
- decided_at

### audit_logs
- id
- actor_type
- actor_id
- action
- tool_name
- parameters_json
- result_json
- created_at

### snapshots
- id
- account_id
- page_type
- screenshot_path
- dom_snapshot_path
- created_at

## 约束建议
- `tasks(status, account_id)` 建索引
- `orders(platform_order_id)` 唯一
- `items(platform_item_id)` 唯一
- `chat_threads(platform_thread_id)` 唯一
- `task_runs(task_id, started_at)` 组合索引
