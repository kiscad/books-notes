

- A **module** is the basic organizational unit of code in Racket.

### 1. 理解 module 的三个基本规则：

1. All program code is contained in a module, through the use of `module` or one of its variants.

    A module expression includes a name, an expander, and a body containing other expressions.

    ```scheme
    (module module-name expander
          other-expressions
          to-expand
          and-evaluate ...)
    ```

2. The **expander** supplies the initial bindings that are available to expressions inside the module.

    If these expressions refer to bindings not provided by the expander, or not otherwise imported within the module, then the module will not run.

3. Modules are "lazy" in the sense that the code inside a module never runs until that module is explicitly requested (by a `require` from elsewhere).

### 2. Source files with a `#lang` line

- `#lang` line 是一个伪装的 module expression.

  Every source file with a `#lang` line expands to a single module expression at the top level. 比如：

  ```scheme
  #lang br
  (* 6 7)
  ```

  会展开成

  ```scheme
  (module my-module br
          (* 6 7))
  ```

### 3. Submodule

- Modules can be nested inside each other to create hierarchies of **submodules**.

  Submodules are defined with the same `module` syntax as regular modules.

- Submodule 的使用有两条规则：

  - A submodule can `require` its enclosing module, or vice versa, but not both.
  - Contrary to Racket's usual evaluation rules, a submodule does not automatically run when its enclosing module runs; likewise, running a submdule does not automatically run its enclosing module.

  ```scheme
  #lang br
  (module tired br
    (sleep 1000)
    (module awake br
      (define greeting "Good morning")
      (provide greeting)
      (module also-tired br
        (sleep 10000))))
  (require (submod "." tired awake))
  greeting ; "Good morning" without waiting
  ```

  - `submod` allows access to submodules through a pathlike notation. In this case, `"."` means "start in the current module", and `tired awake` is the "path" to the submodule.

### 4. Special Module Forms

- `module+` defines a module that adopts all the bindings of the surrounding module. It can still `define` and `provide` additional bindings.
  - It can also be defined in separate pieces: all `module+` expressions with the same name will be combined into a single submodule.
- `module*` defines a module that can `require` its enclosing module, but not vice versa.

### 5. Main submodule

- Any code in a `main` submodule will be evaluated when the enclosing module is run directly in Racket or from the command line, but not when the module is imported with `require`.

- This allows a module to `provide` bindings but specify additional behavior for when it's invoked directly.

  ```scheme
  #lang br
  (define launch-rocket (displayln "whee"))
  (displayln "3 2 1...")
  (module+ main
    (launch-rocket))
  ; 3 2 1...
  ; whee
  ```

### 6. Test Submodule

- In Racket, you can put unit tests inside a submodule named `test`, which usually declared with `module+`.

### 7. Reader module

- When a language is specified on the `#lang` line, Racket will first try to invoke the reader for that language.
- The first place Racket looks for a reader is in a `reader` submodule of the source file indicated.
