## 1. Intro

`stacker` 语言，是一个 stack-based calculator。一个 `stacker` 程序样例：

```scheme
#lang stacker
4
8
+
3
*
```

- 程序的每一行表示一个 argument，`stacker` 语言维护了一个 stack 结构，来装载 arguments。
- `stacker` 读到一个数字时会压入 stack；读到一个 `+` 或 `*` 运算符时会从 stack 中弹出两个数字，进行运算并将运算结果压入 stack。
- stack 数据结构，用 `list` 来实现，list 最左边的元素为栈顶元素。
- 一个 `stacker` 程序执行结束后，stack 栈顶元素就是执行结果。

`stacker` 语言的功能很简单，通过它可以熟悉基本的 the language-making workflow。

## 2. Why Make Languages

什么是编程语言？

- 从程序员的角度，编程语言将我们的想法转化为计算机能够理解的指令，使得计算机能够被我们所控制。
- 编程语言对于使用者来说，通常是黑盒。我们只需熟练使用它就可以了。
- 通过解密编程语言黑盒，我们可以开始一种新的方式来思考编程语言。

按照惯例，实现了编程语言并能转换源代码的软件，称为 **compiler** 或 **interpreter**。

- 既然 compiler 或 interpreter 也是一个程序，那么其实现与普通程序的实现，没有本质区别。
- 编译器的基本任务是 “读取输入，进行运算，返回结果”。这与 function 的概念是一致的。宽泛来讲，一个编程语言就是一个特殊的函数，或一个函数可以看作是一个 DSL。

设计上，编程语言对程序中可能发生的情况做了基本的规则约束。

- 规定了什么样的源代码是可接受的，源代码的语义是什么。

文化上，编程语言除了是一种编写程序的工具，也是一种发现新的编程方式的工具。

在讨论 DSL 和其他编程语言时，我们将从广义上，**把语言看作是描述数据或数据操作的任何结构化符号**。

为什么我们要学习制作编程语言？

- enlarge the solution space. 通过设计 DSL，可以让解决方案更易扩展更易演进。
- 有些问题很适合用 DSL 来解决。这样的问题一般称为“宽通道问题”，即可能的输入范围很大，但输出范围相对较小。
- DSL 可以作为作为胶水工具，用来填补大工具链中的漏洞。比如为 python 语言编写一个预处理器
- 通过 DSL 方式，可以为程序提供一个更好的使用接口。
- 掌握一些高级的编程想法

用 Racket 实现一门编程语言分为三步：

- design the notation and behavior of the new language
- write a Racket program, taking source code of the new language, and converting its notation and behavior to an equivalent Racket program.
  - 这一步有时称为 source-to-source compiler 或 transcompiler.
- Run the new equivalent Racket program.

## 3. Setup

每一个 racket-implemented language 由两个 components 组成：

- A `reader`, which converts the source code from a string into Racket-style parenthesized forms, also known as *S-expressions*.
- A `expander`, which determines how these parenthesized forms correspond to real Racket expressions, which are then evaluated to produce a result.

本书中编程语言实现代码常用的文件头为

```scheme
#lang br
```

- `#lang` line 告诉 DrRacket 使用 `br` module 作为 reader。
- 对于我们实现的新语言的源代码，可以使用 `#lang reader "stacker.rkt"` 来指定源代码的 reader。

### Racket Basics

- Racket 代码的 basic building block 是 **S-expression**。S-expression 可以是：
  - a single value (e.g. `2`, `"blue"`)，
  - a variable (`edge`)，或者
  - a function call (e.g. `(* 21 2)`)
- **Function call** goes between parentheses.
  - All parenthesized S-expressions are treated as function calls.
  - Function name sits in the first position, followed by arguments.
  - 这种风格称为 prefix notation。
- Every S-expression is evaluated to a value.
- S-expression 可以任意深度嵌套。
- True/false 表示为 `#t`/`#f`。
  - 在 conditional forms 中，只有 `#f` value 被认为是 false，其他任意值都是 true，包括 `0`, `null`

### Project Setup

```scheme
; stacker.rkt
#lang br/quicklang
```

- `br/quicklang` language，来自 `beautiful-racket` language，它和 Racket 基本一致，就是在 Racket 上加了一些额外功能。

```scheme
; stacker-test.rkt
4
8
+
3
*
```

## 4. The Reader

> The reader converts the source code from a string into Racket-style forms.

源码样例

```scheme
4
8
+
3
*
```

`stacker` reader 可以将源代码转换为如下形式：

```scheme
(handle 4)
(handle 8)
(handle +)
(handle 3)
(handle *)
```

`handle` 函数将来自 `expander`。之后 `expander` 将 `reader` 的输出转换成真正的 Racket expression。

---

Racket 在执行 the source code of `stacker` 时，会调用 `stacker` reader 的 `read-syntax` 函数，将源代码传递给 reader。所以每个 reader 必须 export a `read-syntax` function。

- `read-syntax` 函数有两个参数：the `path` to source file 和 a `port` for reading data from the file.
- `read-syntax` 函数返回 the code describing a module, packaged as a **syntax object**.
- 然后 Racket 使用 returned module 来替换原始代码。
- 然后 returned module 会调用 expander，生成 a full expansion of the module。
- 最后 Racket interpreter 执行 the expanded module。

---

`reader` 的一个实现样例：

```scheme
(define (read-syntax path port)
  (define src-lines (port->lines port))
  (datum->syntax #f '(module lucy br
                             42)))
(provide read-syntax)
```

- `(define (read-syntax path port) ...` 定义了函数 `read-syntax`
- `(provide read-syntax)` export 函数。Racket 中所有 definitions 都是默认 private的，要公开就需要使用 `provide`。
- `read-syntax` 函数主要执行两个任务。
  - 首先从 `port` 读取源代码。
    - A `port` is a generic interface for input/output that can be read/written incrementally.
    - `port-lines` 返回 a list of strings
  - 然后 return code describing a module。
    - **module** 是 Racket 项目代码的一个基本组织单元
    - module 在 Racket 中是一个 expression
    - `'(module ...)`, quote 函数将 expression 转换成 **datum**, 表示源码的数据结构 (list)。
    - `datum->syntax` 将 datum 转换为 syntax object。它的第一个参数为 program context to be associated with code，第二个参数为 datum。
    - A **syntax object** is just a datum with some extra info attached, including its context with a program.

- module expression 的基本格式为

  ```scheme
  (module module-name which-expander
          42       ; the body of the module
          "foobar" ; contains expressions
          (+ 1 1)  ; to expand & evaluate
          ...)
  ```

有了上面的 reader 样例代码，现在 `stacker-test.rkt` 程序已经可以执行起来了。只是其执行结果始终为 42。

---

`stacker` reader 的实现

```scheme
(define (read-syntax path port)
  (define src-lines (port->lines port))
  (define src-datum (format-datums '(handle ~a) src-lines))
  (define module-datum `(module stacker-mod br
                                ,@src-datums))
  (datum->syntax #f module-datum))
(provide read-syntax)
```

- `(define src-datums (format-datums '(handle ~a) src-lines))`

  将 list of strings 转换为 list of datums

  `format-datums` 的第一个参数为 format string，`~a` 为占位符。

  源码行 `"4"` 将被转换为 `'(handle 4)`，注意转换后 4 没有双引号。

- ``quasiquote` 的作用和 `quote` 基本一致，但可以在运行时向 datum 插入 values，或者可以看作是 formated quote。

  插入 single value，需要使用 `unquote` 运算符 `,`

  ```scheme
  (define x 42)
  `(41 ,x 43) ; '(41 42 43)
  ```

  插入 a list of values，需要使用 `unquote-splicing` 运算符 `,@`

  ```scheme
  (define xs (list 42 43 44))
  `(41 ,@xs 45) ; '(41 42 43 44 45)
  ```

- `(define module-datum (quasi-quote (module stacker-mod br ,@src-datums)))`

  这行代码将 list of datums 插入到 module 中，然后定义为变量 module-datum

---

前面的 `stacker` reader 还无法独立运行，因为缺少 `handle` 函数。但是，我们现在向验证一个 reader 的返回结果是否正确，应该怎么办呢？

我们可以在 `format-datums` 的 format datum 前再加一个 quote，`format-datums ''(handle ~a) src-lines)`。这样 reader 返回的代码就变成了 `'(handle 42)`，而非 `(handle 42)`。

下面是 reader 的验证输出：

```scheme
'(handle)
'(handle 4)
'(handle "hello world")
'(handle #t)
```

- 上面第一行的 `'(handle)` 是由 `#lang ...` 行生成的

---

Reader 已经基本完成，接下来实现 expander，expander 也在 `stacker.rkt` 文件中实现。

在开始 expander 实现前，我们需要将 `read-syntax` 定义中指定的 expander 从 `br` 替换为 `"stacker.rkt"`，即新语言的 expander。另外，double quote 也要改回来。

## 5. The Expander

### Introduce Macros

Racket 中有些 "函数" 看起来和普通函数一样，比如 `(and cond-a cond-b cond-c)`。但是它们并不会 invoked at runtime，而是 replaced at compile-time。比如前面的 `and` 表达式会被替换为

```scheme
(if cond-a
    (if cond-b
        cond-c
        #f)
    #f)
```

这些特殊的“函数”，称为宏 Macros。

> Macros have a restricted interface: they take certain code as input (packaged as a syntax object), and return other code as output (also as syntax object).
>
> Macros 有时也称为 syntax transformers.

Macro 和普通 code 的关系，类似于 regular expression 和 string 的关系。

Macros 也被称为 synactic forms 或 forms，以强调 macro 不执行 evaluation 操作，而是实现 code templates。

Three golden rules of Macros:

- At compile time, a macro takes one code fragment as input, and convert it to a new code fragment. The input and output code fragments are all syntax object.
- Because compile time happens before run time, all macros operate before any run-time functions.
- A macro can only treat its input code as a literal syntactic entity. It cannot evaluate arguments or expressions within that code, because those values are only available at run time.

### What does the Expander do

The expander's job is to prepare the code so Racket can evaluate it.

> The code can be evaluated only if every name (identifier) used in the code has a connection to an actual value or function.

The expander prepares the code for evaluation, by ensuring that **every identifier has a binding**.

- A connection from identifier to an actual value or function, is called a **binding**.

- Once an identifier has a binding, it becomes a **variable**.

Within the expander, we have three basic techniques for adding bindings to code:

- We can **define macros** that rewrite certain code as other code at compile time.
- We can **define functions** that are invoked at runtime.
- We can **import bindings** from existing Racket modules, which can include both macros and functions.

### Designing the Expander

`stacker` expander 要完成的任务：

- Provide bindings for three identifiers: `handle`, `+`, `*`
- 实现一个 stack 数据结构，提供 store, read, 等操作，让 `handle` 使用
- Provide a special macro `#%module-begin` to get everything started.

### 实现 Expander output

expander 的输入样例：

```scheme
(module stacker-mod "stacker.rkt"
        (handle)
        (handle 4)
        (handle 8)
        (handle +)
        (handle 3)
        (handle *))
```

Racket 通过调用 `read-syntax` 函数来使用 reader，然后通过调用 `#%module-begin` macro 来使用 expander。

- **Every expander must export a `#%module-begin` macro.**

Racket 调用 `#%module-begin` macro 将 module 内容传给它

```scheme
(#%module-begin
  (handle)
  (handle 4)
  (handle 8)
  (handle +)
  (handle 3)
  (handle *))
```

下面是在 expander 中创建 `#%module-begin` 的样例

```scheme
(define-macro (stacker-mod-begin HANDLE-EXPR ...)
  #'(#%module-begin
     HANDLE-EXPR ...))
(provide (rename-out [stacker-mod-begin #%module-begin]))
```

- 函数的输入参数一般定义为若干个 normal args；而 macro 的输入参数，一般定义为一个 syntax pattern。
  - `define` 不支持 syntax pattern，`define-macro` 支持
- **Syntax pattern** 类似于 regular expression，可以匹配解析提取 input code object。
- `stacker-mod-begin` 为 macro name
- `HANDLE-EXPR` 是一个 pattern variable, 也就是 a named match within the syntax pattern.
  - 后接的 `...`，表示这个 pattern variable 将 match 传入的每一行代码。
- `#'(#%module-begin HANDLE-EXPR ...)` 为 macro 的返回值。
  - `#'` 可以将代码转换为 syntax object，类似于 `'` 将代码转换为 datum。
- `#'` prefix 不仅生成 datum，还会 capture the current lexical context。
  - **Lexical context** 就是 a list of available variables。
  - 这使得 syntax object 在后续执行时，能够访问代码中的变量。
  - 通过 capture the pattern variable `HANDLE-EXPR ...`，所有的 code lines 被插入到 syntax object 中。
- `#'(#%module-begin)'` 内部的 `#%module-begin` 是来自 `br/quicklang` 的 identifier。
  - 所以这里的含义是，take the input code and pass it to the next `#%module-begin` macro from `br/quicklang`。
- 因为 expander 引入了一个 `#%module-begin` 的同时要 export 一个 `#%module-begin`，所以这里的 `provide` expression 里面嵌入了一个 `rename-out` expression。

---

现在我们想验证一下 expander 的 `#%module-begin` 是否正常工作，但是我们还没有定义 `handle`。

- 可以使用之前同样的方式，在返回的 syntax object 内的 `HANDLE-EXPR` 前加 `'` prefix。
- 这样返回的 code lines 就不会真的执行起来了。测试源码的输出和之前 reader 应该是一样的。
- 这样新的语言，从源码到 reader 到 expander 到 evaluation 的完整流程就跑通了，虽然结果不正确。

---

### 实现 expander binding

前面完成了 expander 三个任务中的第一个，现在来实现第二个："implmenting a stack and creating bindings for our identifiers"。

下面是 stack 的实现

```scheme
(define stack empty)

(define (pop-stack!)
  (define arg (first stack))
  (set! stack (rest stack))
  arg)

(defin (push-stack! arg)
  (set! stack (cons arg stack)))
```

`handle` 函数的实现如下：

```scheme
(define (handle [arg #f])
  (cond
   [(number? arg) (push-stack! arg)]
   [(or (equal? + arg) (equal? * arg))
    (define op-result (arg (pop-stack!) (pop-stack!)))
    (push-stack! op-result)]))
(provide handle)
(provide + *)
```

- `(define (handle [arg #f]) ...` 定义了函数 `handle`，函数有一个参数 `arg`，参数有一个默认值 `#f`。这样函数调用 `(handle)` 时，`arg` 为 `#f`。
- expander 还要提供 `+` 和 `*` 的 bindings。它们在 `br/quicklang` 已经定义了，这里只需 re-export 即可。

先运行测试代码就不会报错了，但是也不会打印计算结果。

- 要想打印计算结果，只需在 `#%module-begin` macro 内的 `HANDLE-EXPR ...` 后面加一行代码 `(display (first stack))` 即可。

到这里，我们就实现了一门编程语言啦 :confetti_ball: :fireworks:

## 6. Recap

- A language in Racket can be though of as a source-to-source compiler, that converts the source code of a new language into ordinary Racket code, then runs it normally.
- Every language has a reader and a expander.
  - The reader is responsible for the form of the code; the expander is responsible for its meaning.
- The reader converts the source code of the new language into Racket-style parenthesized forms called S-expressions.
  - The reader must `provide` a function `read-syntax`. Racket passes two arguments to this function: the `path` to the source file, and an input `port` for reading the source code.
  - After converting the source to S-expressions, the function must return Racket code describeing a module (syntax object).
  - Back at the source file, Racket replaces the source code with this module code.
- The `expander` determines how the S-expressions generated to real Racket expressions, by ensuring that every identifier has a binding.
  - The expander must `provide` a macro called `#%module-begin`. Racket takes the code from inside module expression generated by the reader and passes it to this macro.
  - This macro must return new Racket code (syntax object). Racket replaces the module expression generated by the reader with this new code.
- Once the expander finishes its work, the new language has been translated into oridnary Racket code. It's evaluated as a Racket program to produce a result.
- Racket supports a special class of functions called **macros**.
  - Macros can copy & rewrite code at compile time.
  - All macros take a code fragment as input and return a new code fragment as output.
- A syntax object can also hold a reference to the **lexical context** at a certain point in the program, so that code inside the syntax object can see all the variables defined at that point.
  - We can use the `#'` prefix to turn any code into a syntax object, by converting it to a datum and capturing its lexical context.













