# 书籍文本与发布位置

本站是 Pedro Duarte Faria 的《Introduction to Zig: a project-based book》英文版独立镜像。原书：<https://pedropark99.github.io/zig-book/>；原仓库：<https://github.com/pedropark99/zig-book>。书籍版权归作者所有，按仓库中的 [CC BY 4.0 许可](LICENSE)分享；本仓库保留原作者署名和英文原文。

- 在线地址：<https://izrino.github.io/zig-book/>，与 `/zig-docs/` 是两个独立的 GitHub Pages 项目。
- **可编辑的英文正文**：根目录的 `index.qmd` 和下表中的 `Chapters/*.qmd`。章节顺序以 `_quarto.yml` 的 `book.chapters` 为准，**不要按文件名数字排序**。
- **已生成的英文网页**：`docs/index.html`、`docs/Chapters/*.html`。GitHub Pages 从 `main` 分支的 `/docs` 发布；这些 HTML 是构建产物，不应作为翻译源。
- **其他可见文本**：`_quarto.yml` 含书名、副标题和作者元信息；`Assets/button.html`、`Assets/leanpub-button.html`、`Assets/paypal-button.html`、`Assets/revolut-button.html` 含按钮文案；`Assets/references.bib` 含参考文献条目；图片与代码示例分布在 `Cover/`、`Figures/`、`ZigExamples/`。`docs/search.json`、`docs/site_libs/` 等是生成资源，不要直接翻译。

## 正文章节（原书顺序）

| 页 | 英文源文件 | 标题 |
| --- | --- | --- |
| 欢迎页 | `index.qmd` | Welcome |
| 1 | `Chapters/01-zig-weird.qmd` | Introducing Zig |
| 2 | `Chapters/03-structs.qmd` | Control flow, structs, modules and types |
| 3 | `Chapters/01-memory.qmd` | Memory and Allocators |
| 4 | `Chapters/01-base64.qmd` | Project 1 - Building a base64 encoder/decoder |
| 5 | `Chapters/02-debugging.qmd` | Debugging Zig applications |
| 6 | `Chapters/05-pointers.qmd` | Pointers and Optionals |
| 7 | `Chapters/04-http-server.qmd` | Project 2 - Building a HTTP Server from scratch |
| 8 | `Chapters/03-unittests.qmd` | Unit tests |
| 9 | `Chapters/07-build-system.qmd` | Build System |
| 10 | `Chapters/09-error-handling.qmd` | Error handling and unions |
| 11 | `Chapters/09-data-structures.qmd` | Data Structures |
| 12 | `Chapters/10-stack-project.qmd` | Project 3 - Building a stack data structure |
| 13 | `Chapters/12-file-op.qmd` | Filesystem and Input/Output (IO) |
| 14 | `Chapters/14-zig-c-interop.qmd` | Zig interoperability with C |
| 15 | `Chapters/13-image-filter.qmd` | Project 4 - Developing an image filter |
| 16 | `Chapters/14-threads.qmd` | Introducing threads and parallelism in Zig |
| 17 | `Chapters/15-vectors.qmd` | Introducing Vectors and SIMD |
| 参考文献 | `Chapters/references.qmd` | References |

后续中文翻译应单独建立中文版源文件与发布目录，不覆盖上述英文 `.qmd` 或 `/docs` 里的英文页面。原项目的完整构建说明在英文 [README.md](README.md)；编辑源文件后，需要 Quarto、R 和 Zig 构建并重新提交 `docs/` 才会更新 Pages。当前未创建中文占位页面，也未翻译英文内容。
