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