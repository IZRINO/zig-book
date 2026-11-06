# 《Zig 语言入门：基于项目的实操指南》中文开源版

<a href="https://izrino.github.io/zig-book/zh-CN/"><img src="Cover/cover-artv3.png" width="220" height="320" class="cover" align="right" alt="Zig 语言入门书籍封面"/></a>

> 本项目是 Pedro Duarte Faria 所著经典开源技术读物 **《Introduction to Zig: a project-based book》** 的**中文全译本**。  
> 遵循知识共享署名许可协议（[CC BY 4.0](LICENSE)）开源共享，完整保留原书版权与英文原文。

[![Zig](https://img.shields.io/badge/Zig-0.17-F7A41D?style=flat&logo=zig&logoColor=black)](https://ziglang.org/)
[![Quarto](https://img.shields.io/badge/Built%20with-Quarto-4D5891?style=flat&logo=quarto&logoColor=white)](https://quarto.org/)
[![GitHub Pages](https://img.shields.io/badge/Online%20Reading-GitHub%20Pages-success?style=flat&logo=githubpages&logoColor=white)](https://izrino.github.io/zig-book/zh-CN/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

## 📖 在线阅读入口

* 🇨🇳 **中文版在线阅读**：[https://izrino.github.io/zig-book/zh-CN/](https://izrino.github.io/zig-book/zh-CN/)
* 🌐 **英文原版在线阅读**：[https://izrino.github.io/zig-book/](https://izrino.github.io/zig-book/)
* 💡 **双语无缝切换**：阅读时随时点击网页顶栏或侧边栏的 `🌐 语言 / Language`，即可一键在**当前对应章节**的中英文之间精准互跳，并保留阅读锚点！

---

## 💡 为什么选择这本书学习 Zig？

Zig 是一门专注于构建高性能、高可靠底层软件的新一代系统级编程语言。本书拒绝枯燥生硬的纯语法罗列，而是遵循经典的“做中学（Project-Based）”理念，通过 **4 个逐步递进的真实工程项目** 带你全面吃透 Zig 的核心设计精髓：

1. **实战 1：手写 Base64 编解码器** —— 彻底拆解位运算（Bitwise Operators）、查找表（Lookup Table）优化与字节流转换。
2. **实战 2：从零手写轻量 HTTP 服务器** —— 玩转底层 TCP 套接字（Sockets）、网络 I/O、HTTP 报文解析与并发连接处理。
3. **实战 3：手写通用泛型栈（Stack）** —— 深度理解 Zig 独门绝技：编译期计算（Comptime）与无开销泛型元编程。
4. **实战 4：开发图像灰度滤镜** —— 掌握复杂指针运算、内存分配策略与 SIMD 向量化硬件级并行加速。

---

## ✨ 中文版翻译特色

* **开发者日常口语**：通俗自然、生动流畅，彻底告别冰冷生硬的机翻腔調。
* **专业术语规范精准**：
  * `Optionals` $\rightarrow$ 可选类型（告别 Null 引用地狱）
  * `Allocators` $\rightarrow$ 内存分配器（显式内存控制）
  * `Comptime` $\rightarrow$ 编译期执行（告别传统宏魔法）
  * `Tagged Unions` $\rightarrow$ 带标签联合体
  * `Slices` $\rightarrow$ 切片
* **0 依赖轻量构建**：中文源文件已去除 knitr/R 动态环境依赖，采用纯净 Quarto Markdown，单条命令秒级编译。

---

## 📚 全书完整章节目录

| 章节 | 中文源文件 | 英文源文件 | 核心主题 |
| :--- | :--- | :--- | :--- |
| **欢迎页** | `zh-CN/index.qmd` | `index.qmd` | 全书介绍与原作者背景 |
| **第 1 章** | `zh-CN/Chapters/01-zig-weird.qmd` | `Chapters/01-zig-weird.qmd` | 初识 Zig：语法特性与哲学对比 |
| **第 2 章** | `zh-CN/Chapters/03-structs.qmd` | `Chapters/03-structs.qmd` | 控制流、结构体、模块与类型系统 |
| **第 3 章** | `zh-CN/Chapters/01-memory.qmd` | `Chapters/01-memory.qmd` | 内存管理机制与底层分配器（Allocators） |
| **第 4 章** | `zh-CN/Chapters/01-base64.qmd` | `Chapters/01-base64.qmd` | **实战项目 1**：手写 Base64 编解码器 |
| **第 5 章** | `zh-CN/Chapters/02-debugging.qmd` | `Chapters/02-debugging.qmd` | 调试 Zig 程序：LLDB、断点与 Panic 跟踪 |
| **第 6 章** | `zh-CN/Chapters/05-pointers.qmd` | `Chapters/05-pointers.qmd` | 指针语法与可选类型（Optionals）范式 |
| **第 7 章** | `zh-CN/Chapters/04-http-server.qmd` | `Chapters/04-http-server.qmd` | **实战项目 2**：从零手写原生 HTTP 服务器 |
| **第 8 章** | `zh-CN/Chapters/03-unittests.qmd` | `Chapters/03-unittests.qmd` | 单元测试（Unit Tests）规范与最佳实践 |
| **第 9 章** | `zh-CN/Chapters/07-build-system.qmd` | `Chapters/07-build-system.qmd` | 深入 Zig 原生构建系统（`build.zig`） |
| **第 10 章** | `zh-CN/Chapters/09-error-handling.qmd` | `Chapters/09-error-handling.qmd` | 错误作为值（Errors as Values）与联合体 |
| **第 11 章** | `zh-CN/Chapters/09-data-structures.qmd` | `Chapters/09-data-structures.qmd` | 常用数据结构（ArrayList、HashMap） |
| **第 12 章** | `zh-CN/Chapters/10-stack-project.qmd` | `Chapters/10-stack-project.qmd` | **实战项目 3**：手写泛型栈数据结构 |
| **第 13 章** | `zh-CN/Chapters/12-file-op.qmd` | `Chapters/12-file-op.qmd` | 文件系统操作与底层流式 I/O |
| **第 14 章** | `zh-CN/Chapters/14-zig-c-interop.qmd` | `Chapters/14-zig-c-interop.qmd` | Zig 与 C 语言的无缝互操作（C Interop） |
| **第 15 章** | `zh-CN/Chapters/13-image-filter.qmd` | `Chapters/13-image-filter.qmd` | **实战项目 4**：开发图像灰度滤镜算法 |
| **第 16 章** | `zh-CN/Chapters/14-threads.qmd` | `Chapters/14-threads.qmd` | Zig 多线程并发与并行计算 |
| **第 17 章** | `zh-CN/Chapters/15-vectors.qmd` | `Chapters/15-vectors.qmd` | 向量类型与 SIMD 硬件指令集并行加速 |
| **参考文献** | `zh-CN/Chapters/references.qmd` | `Chapters/references.qmd` | 核心参考文献与社区资源 |

---

## 🛠️ 本地预览与重新构建

### 1. 运行本地 Web 预览服务
```bash
python -m http.server 8080 --directory docs
```
* 中文主页：`http://localhost:8080/zh-CN/index.html`
* 英文主页：`http://localhost:8080/index.html`

### 2. 重新编译中文版
确保本地已安装 [Quarto](https://quarto.org/)：
```bash
cd zh-CN
quarto render
```
编译生成物将自动更新到 `docs/zh-CN/` 目录。

### 3. 一键同步双语切换入口
```bash
python tools/sync_lang_switch.py
```

---

## 🏷️ 核心关键词与主题
`Zig` · `Zig 编程语言` · `Zig 教程` · `Zig 中文文档` · `Zig 语言入门` · `Zig 源码实战` · `系统级编程` · `C 语言现代化替代` · `Introduction to Zig` · `Pedro Duarte Faria` · `Systems Programming` · `Comptime` · `Memory Allocator` · `HTTP Server` · `SIMD`

---

## 📄 开源许可与致谢
* 本书中文翻译版本严格遵循 [CC BY 4.0 国际许可协议](LICENSE) 开源。
* 衷心感谢原作者 **Pedro Duarte Faria** 与 Zig 开源社区的杰出贡献！
