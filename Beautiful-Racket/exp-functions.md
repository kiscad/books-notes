## Functions

- A **function** is a set of expressions that's only evaluated when explicitly invoked at runtime.

  - Optionally, a function can take arguments as input, and return values as output.

- 创建和使用 function 主要因为三种相互重叠的目的：

  - To **delay** the evaluation of a set of expressions.
  - To allow **repeated** evaluation of a set of expressions.
  - To **generalize** a set of expressions by using input arguments.

- Function 可以像普通 value 一样进行 binding and pass around.

  ```scheme
  (define plus +)
  (define another-plus +)
  (eq? plus another-plus) ; #t
  ```

- Function 可以使用 `defin` form 进行定义/创建。

  ```scheme
  (define (plus x y)
    (+ x y))
  ```

- Function 可以没有 identifier binding，即 anonymous function。

  ```scheme
  ((lambda (x y) (+ x y)) 30 12) ; 42
  ```

  - **Lambda** is sometimes used as a synonym for function.
  - A lambda without arguments, is sometimes called a **thunk**.

- In Racket, functions are also called **procedures**.

  - A function that takes one argument and returns a Boolean, is often called a **predicate**.
  - `procedure?` 可以检查一个 value 是否为函数。

- Racket 中函数调用的两种方式：

  - Directly in an expression: `(func arg1 arg2 ...)`
  - Indirectly by passing to high-order functions: `(apply func (list arg1 arg2 ...))`

- 函数的输入参数

  - 输入参数的数量称为 the **arity** of the function。

  - 函数参数默认为 positional arguments，即按照位置绑定。

  - Racket 也支持 keyword arguments，且 keyword args 可以出现在 argument list 任意位置

    ```scheme
    (define (sub #:foo foo-val y)
      (sub foo-val y))
    (sub 12 #:foo 30) ; 18
    ```

  - Positional args 和 keyword args 都可以提供 default value。一般不带默认值的参数要排在前面。

    ```scheme
    (define (add-defaults x [y 10] #:z [z 1])
      (+ x y z))
    (add-defaults 100 20) ; 121
    (add-defaults 500) ; 511
    ```

  - Racket 函数支持 `rest argument`, 可以接受任意数量输入参数。rest argument 一般放在参数列表最后，且不能有默认值。在函数内 rest arg 为一个 list。

    ```scheme
    (define (add-rest x . others)
      (apply + x others))
    (add-rest 1 2 3 4 5 6 7 8 9) ; 45
    ```

- 函数的输出

  - Racket function 没有 return 语句，其 evaluation 的 last value 为函数返回值。

  - 虽然不常用，但 Racket 函数可以返回多个 values。

    ```scheme
    (define (two-vals x y) ; returns two values
      (values (+ x y) (* x y)))
    ; `define-values` accepts two return values
    (define-values (sum prod) (two-vals 11 3))
    ```

- 函数命名规则

  - Predicate 函数名，以 `?` 结尾，如 `string?`, `void?`

  - 可以 mutate the state of an existing variable or data structure 的函数，名称一般以 `!` 结尾，如 `set!`, `vector-fill!`, `read-bytes!`

  - 如果已存在一个处理 single value 的函数，那么其处理 multi values 的变体函数，其名称一般以 `*` 结尾。比如 `regexp-match` 与 `regex-match*`，`string-append` 与 `string-append*`。

    The `*` suffix can also denote a variant that treats multiple args as nested rather than parallel: `for` vs. `for*`, `let` vs. `let*`.

  - A variant function with a narrower field of operation uses a `/` with a qualifier suffix. 比如 `defin` vs. `define/contract`, `equal?` vs. `equal?/recur`, `let` vs. `let/cc`.

  - Functions that convert from one data type to another have an infixed `->`. 比如 `string->number`, `char->integer`, `datum->syntax`.

  - Functions that are contract combinators end with `/c`. 比如 `list/c`, `and/c`, `hash/c`.

  - Parameters are often named with a `current-` prefix, 比如 `current-directory`, `current-input-port`, `current-namespace`.

- Racket 是一种 函数式编程语言

  - Functional programming is a style of programming where functions receive certain data as input, process only that data, and return a result.
  - 在函数式编程中，我们避免两件事情
    - *Mutation*, changing data in-place rather than returning a value
    - Relying on *state*, extra context that's not provided as input.
  - 一个软件中总有一部分是无法用 FP 实现的，这样的函数一般用于实现 side effects。
  - The rule of thumb in Racket is to use functional programming when you can, and depart from it when you must.

  