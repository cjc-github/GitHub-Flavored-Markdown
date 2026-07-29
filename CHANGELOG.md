# 更新日志

本项目采用`YYYY.MM.PATCH`格式的日期版本号。月份内的兼容性修正增加PATCH版本；大规模结构调整可以直接进入新的月份版本。

## [Unreleased]

### 新增

- 未定义引用式链接和非法本地路径检查。
- actionlint工作流语法验证和Dependabot配置。
- HTML实体索引及26个字母分页。
- 为标题、目录、文本格式、列表、链接、图片、表格和数学功能补齐Markdown/GFM、HTML与LaTeX实现或替代说明。

### 调整

- 扩大Markdown结构检查范围，并覆盖全部维护文档和实体分页。
- 将支持情况表改为CommonMark、正式GFM、GitHub平台和HTML后备四层模型。
- 固定GitHub Actions依赖到具体提交SHA。

### 修复

- 清理拆分文档中的无意义行尾空白。
- 恢复图片章节和GitHub组件章节在首次拆分时错位的内容。

## [2026.07.0] - 2026-07-29

### 新增

- 正式GFM规范补充、GeoJSON、TopoJSON和ASCII STL示例。
- 本地资源、标题锚点、生成文档和Markdown结构检查。
- 检查器单元测试、GitHub Actions和外部链接定期巡检。
- 贡献指南、行为准则、安全策略、支持说明和Issue/PR模板。

### 修复

- 音频链接、链接文本、折叠标签、图片语法和汇总表编号。
- Emoji文档中的表格列数错误。
- HTML实体生成脚本对当前工作目录的依赖。
