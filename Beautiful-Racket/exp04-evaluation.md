## Evaluation

The **evaluation** of a Racket program 分为四个阶段：

- A source file with a **reader** attached, via the `#lang` line. The *reader* transforms the code.

- Any forms that introduce **bindings**, like `require` or `define` are resolved.

- **Macros** are expanded, starting with the outermost forms and progressing inward.

  - Macro expansion is recursive: if a macro expands to be come another macro, the new macro is also expanded.
  - The fully expanded program, has no macros, only has core syntactic forms.
  - 截止这一阶段，称为 compile time 或 phase 1。

- All expressions in the fully expanded program are evaluated, starting with the innermost expression and progressing outward.

  - If any identifier in the fully expanded program still don't have bindings, the evaluation fails with an error.

  - 这一阶段称为 runtime 或 phase 0。

    ```scheme
    (require br/verbose-app) ; 可以打印 program 的执行过程
    (* (+ 1 2) (* 3 4 (/ 5 6)))
    ```

    

