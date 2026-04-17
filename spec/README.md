# Spec 目录说明

本目录用于存放项目的任务规范、长任务资产、验收记录与报告。

## 推荐结构

```text
spec/
  README.md
  tasks/
    <topic>-YYYY-MM-DD/
  archive/
  templates/
    long-task -> 共享长任务模板

src/
tests/
docs/
```

## 使用建议

1. 中大型任务统一在 `spec/tasks/<topic>-YYYY-MM-DD/` 下建档
2. 每个长任务至少包含：
   - `000-high-roi-...md`
   - `<task_code>-taskboard-...md`
   - `<task_code>-log.md`
   - `<task_code>-task-report-template.md`
3. 已结束任务可在合适时机移入 `archive/`

## 模板来源

- 通用长任务模板来自：
  - `/vol1/1000/codexcli/spec/templates/long-task/`

如果当前项目有自己的模板要求，可在项目内新增更具体模板。
