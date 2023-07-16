## Forword

上世纪90年代初，人们对于编程语言的一些技术特性进行了激烈的讨论：

- GC (garbage collection) 是否能完全替代手动内存管理
- First-class functions 和 closure 对于普通程序员是否友好
- 保证 static type systems 的完备性的努力是否必要

虽然这些技术现在都认为是理所当然的，但当时还是有争议的。编程语言的技术集是逐渐演变的。

---

Language extensibility, 是一个古老而有趣的主题，从 Lisp Macro 就有了。

但是为什么绝大部分人并不经常使用 macro 来扩展语言呢？因为，虽然 macro 在原理是很酷的，但实际使用时额外开销太大（主要是程序理解上的开销，而非执行层面）。

和 first-class function 一样，macro 为代码增加了一个额外的维度。这对于程序员的认知负担是很大的考验。此外 macro hygiene 背后的理论过于艰深。

---

“Beautiful Racket" 这本书展示了如何在实际问题中使用 Racket macro，让你感受到使用 macro 的好处。



## Introduction

本书教你如何 “面向语言编程”，也就是如何设计和实现编程语言。我们将使用 Racket 作为工具语言来制作其他语言。

学习面向语言编程，将使你成为更好的程序员。编程语言是程序员的基础工具，可能你可以熟练使用一门编程语言，但你很可能对于这门编程语言本身却一无所知。

本书的知识，将使你更加精通一般化语言，提高你的语言鉴赏能力。

学习面向语言编程，会让你掌握更深层次的、完全不同的编程方法。

编程语言，没有一个固定的定义。除了一般的通用编程语言，你可以为满足某个问题，或满足少数几个人而设计一门语言，也称为 domain-specific language (DSL)。

## Setup

- 安装 Racket
- 安装 `beautiful-racket` package
  - 启动 `DrRacket`, 点击 `File > Install Package...`, 输入 `beautiful-racket` 进行安装
  - 命令行安装方式：`$raco pkg install --auto beautiful-racket`
  - 命令行验证：`$racket -l br/test`
- 将 `beautiful-racket` 设置为默认语言
  - 启动 `DrRacket`，选择 `Language > Choose Language`, `Show Details`, 在 `Automatic #lang line` section, 选择 `Always use the same #lang line`, 输入 `#lang br`, OK 确定
- 更新 package `raco pkg update --update-deps beautiful-racket`

