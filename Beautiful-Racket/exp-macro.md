### 1. Macro

- A **macro** is a special kind of function that runs at compile time, consuming certain code as input and rewriting it as new code.
  - Macro is also called **syntax transformer** or **syntactic form**.
- The code resulting from a macro is called the **expansion** of the macro.

### 2. Why Macro

Macro 的价值主要在两个层面上：

1. At the program level, macro allow us to implement ideas in code, that cannot be achieved with ordinary functions.

   例子：在打印 expression 结果的同时，也打印 expression 本身

   ```scheme
   (define-macro (report EXPR)
      #'(begin
         ; EXPR used as literal data, and quoted as a datum
         (displayln (format "input is ~a" 'EXPR))
         EXPR)) ; EXPR used for its result
   
   (report (* 1 2 3 4))
   ```

   - Macro 有点类似于 C preprocessor，但功能更强大。
   - Macros enforce **hygiene**, which is a set of rule about how macro-generated code will interfact with other code.

2. At the compiler level, macros allow forms to be expressed in terms of more primitive forms, all the way down to a set of core syntactic forms.

   - 因为 macro，Racket 维持一个 small set of core syntactic forms, 同时提供很多高级语法特性。

     比如 `if` 是 core syntactic form，而 `and`, `or`, `when` 都是用到 `if` 的 macros。

   - In a Racket-implemented langauge, we often use macros within the `expander` to convert the forms of our language into standard Racket forms.

### 3. Interface & Operation

- Macros are functions that take one syntax object as input and return another syntax object.
  - These **syntax objects** contain literal code, packaged with metadata like lexical context and source location.

- A macro extracts the pieces of the input syntax object and rearranges them into new code.

  - This is done with **syntax patterns**, which match pieces to **pattern variables**.

  - 下面的 `and` macro 的实现样例

    ```scheme
    (define-macro-cases and
      [(and) #'#t]
      [(and COND) #'COND]
      [(and COND OTHER-CONDS ...) #'(if COND
                                        (and OTHER-CONDS ...)
                                        #f)])
    ```

  - Unlike nested expressions, which are evaluated from the inside out, nested macros are evaluated from the outside in.

    This makes it possible for macros to generate references to other macros, which in turn are expanded.

### 4. Why not macro

- Macros 有一些内在的局限性：
  - they perform one service: rewriting code.
  - they can only consume and return syntax objects.
  - they run at compile time, so they cannot know anything about the runtime meaning of their input.

### 5. Mixing Macros & Functions

- 关于何时使用 macros 还是 functions 的一些建议

  - Don't use a macro where a function will work equally well.

    Save macros for the situations where a function won't work.

    ```scheme
    (define-macro (add . XS) #'(apply + (list . XS)))
    (define (add . xs) (apply + xs))
    ```

  - Design the macro to emit as little code as possible.

    Where possible, refactor code into an external helper function. (Because of hygiene, this is easy to do.)

    ```scheme
    (define-macro (mac NUM)
      #'(begin
        (displayln 'NUM)
         (if (even? NUM)
             (do-thing NUM)
             (do-other-thing NUM)))) ; bad implementation
    
    (define-macro (mac2 NUM)
      #'(begin
         (displayln 'NUM)
         (test-and-do-something NUM))) ; good implementation
    (define (test-and-do-something x)
      (if (even? x)
          (do-thing x)
          (do-other-thing x)))
    ```

    