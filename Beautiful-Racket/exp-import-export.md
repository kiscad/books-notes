## Importing & Exporting

- **Bindings** can be defined in one module and shared with another.
  - The defining module is **exporting** bindings;
  - the other module is **importing** bindings.

### 1. Exporting

- By default, all bindings defined in a module are private to that module.

- To make a binding available to other modules, use `provide`:

  ```scheme
  #lang br
  (define my-var 42)
  (provide my-var)
  ```

  虽然 `provide` 语句可以写在任意位置，但通常写在一个 module 的最前面

  ```scheme
  #lang br
  (provide my-var another-var third-var)
  (define my-var 42)
  (define another-var 96)
  (define third-var 256)
  ```

- 如下想 export all newly-defined bindings in a module，可以使用语句 `(provide (all-defined-out))`

- 除了 export 自己定义的 bindings，也可以 export imported bindings 或 language bindings。比如 `(provide + *)`

  - 如果想 re-export all imported bindings from another module, 可以

    ```scheme
    #lang br
    (provide (all-from-out br))
    ```

- 在 exporting 时，可以重命名 external name: `(provide (rename-out [internal-name external-name]))`。

### 2. Exporting

- Every module gets its initial set of bindings from its expander.

- For a `module` expression, the expander is designated explicitly.

  ```scheme
  #lang br
  ;; all bindings exported by `br` expander are available here
  (module sub pollen
    ;; all bindings exported by `pollen` are available here
    )
  ```

- Bindings from other modules 可以通过 `require` 手动 import

  ```scheme
  #lang br
  (require brag/support) ; provides `token`
  (token 'FOO "bar")
  ```

- `submod` 配合 `require` 可以 import sub-modules

  ```scheme
  (module baba br
          (provide foo)
          (define foo "too hot")
          (module baby br
                  (provide foo)
                  (define foo "yummy")))
  
  (require (submod "." papa baby))
  foo ; "yummy"
  ```

### 3. Phases

- 一个 module 的 evaluation 分为几个相对独立的 phases。

  - 每个 phases 的 importing & exporint 相对独立。
  - 前一 phase 的 importing 并不会对于会面的 phase 自动 visible。

- 这种 visibility 的独立性，在编写 macro 代码时会造成一些奇怪错误。

  - macro 代码的 evaluation 可以跨越 `phase 1` (compile-time) 和 `phase-0` (runtime)。

  - ```scheme
    #lang br
    (require racket/bool)
    (define-macro (nander)
                  #'(println (and (nand #f #t) 'phase-0)))
    (nander) ; 'phase-0
    ```

  - 上面的代码可以正确执行，并输出 `'phase-0`

    - `(require racket/bool)` 为当前源码在 phase-0 引入了 `nand` binding
    - 该源码在 compile-time 可以正常宏展开，`(nander)` 被展开为 `(println (and (nand #f #t) 'phase-0'))`
    - 该源码在 runtime 阶段，可以找到 identifier `nand` 的 binding，然后正常执行。

  - ```scheme
    #lang br
    (require racket/bool)
    (define-macro (nander)
                  (println (and (nand #f #t) 'phase-1))
                  #'(println (and (nand #f #t) 'phase-0)))
    (nander)
    ```

  - 上面的代码在 phase-1 compile-time 会报错。

    - 宏定义的一条语句，会在 compile-time 执行，或者说是在当前 syntax object 之外执行，这时就会因为找不到 `nand` binding 而报错

  - Racket 中可以通过 `for-syntax` 来为 syntax object 的 compile-time 引入 bindings

    ```scheme
    #lang br
    (require racket/bool (for-syntax racket-bool))
    (define-macro (nander)
                  (println (and (nand #f #t) 'phase-1))
                  #'(println (and (nand #f #t) 'phase-0)))
    (nander)
    ```

    上面的代码可以正常执行，并在 compile-time 和 runtime 分别打印 `'phase-1` 和 `'phase-0` 两行输出

  - ```scheme
    #lang br
    (require (for-syntax racket/bool))
    (define-macro (nander)
                  (println (and (nand #f #t) 'phase-1))
                  #'(println (and (nand #f #t) 'phase-0)))
    (nander)
    ```

    - 上面的代码只为 compile-time 引入了 `nand` binding。
    - 上面代码会在 compile-time 打印 `'phase-1`；在 phase-0 会报错 `nand: unbound identifier`

  

