### 1. Identifier

- An **identifer** is a name that appears in a program.
- The meaning of the name is determined by the identifier's **binding**, which is an association between an identifier and some other items, such as a specific value, a function, a macro, or other identifier.
- An identifier with a binding is called a **variable**.
  - An identifier without a binding is called an *unbound* identifier.

### 2. Naming convention

- An identifer can be written with any Unicode characters, except whitespace, and the following reserved characters: `(`, `)`, `[`, `]`, `{`, `}`, `"`, `'`, `,`, `` ` ``, `;`, `#`, `|`, `\`.

- Numbers cannot be used as identifiers

  ```scheme
  (define 42a "value") ; ok
  (define 42 "value") ; not ok
  ```

- Idiomatically, identifiers are written in lowercase, with hyphens between words.

  ```scheme
  lowercased
  lowercased-with-hyphens
  ```

### 3. Make binding

Identifier bindings 主要有三种创建方式：

- Explicit binding forms like `defin`, `let` or `lambda`.

  These bindings can shadow existing bindings outside the form.

  ```scheme
  (define x 42)
  (define y 100)
  (let ([y 42]) (+ x y)) ; 84
  
  (define z 1000)
  (define f (lambda ([z 42]) (+ x y z)))
  (f) ; 184
  ```

- Import bindings from other modules with a form like `require`

  Bindings within the module will shadow imported bindings.

  ```scheme
  (module mod1 br
          (define foo "zim")
          (provide foo))
  (require (submod "." mod1))
  foo ; "zim"
  
  (module mod2 br
          (define bar "zam")
          (provide bar))
  (require (submod "." mod2))
  (define bar "bang")
  bar ; "bang"
  ```

  An error will arise if two imported modules `provide` bindings for the same identifier.

  ```scheme
  (module mod1 br
          (define foo "zim")
          (provide foo))
  (require (submod "." mod1))
  
  (module mod2 br
          (define foo "zam")
          (provide foo))
  (require (submod "." mod2))
  ;; error: identifier `foo` imported twice
  ```

- Make bindings with macro.

  ```scheme
  (define-macro (define-as-42 ID)
                #'(define ID 42))
  (define-as-42 foo)
  foo ; 42
  ```

### 4. Scope

- Every identifier binding has a **scope** that determines where in the program the binding is visible.
  - Outside that scope, the binding won't work.
  - The scope of binding depends on how & where the identifier is introduced.

1. **Expression scope**: a binding created within a expression is only visible within that expression.

   ```scheme
   (define (get-bar)
     (define bar 42)
     (let ([bar 92])
       bar))
   (get-bar) ; 92
   bar ; error: unbound identifier
   ```

2. **Module scope**: a binding created at the top level of a module, with `define` or `require`, is visible throughout the module.

   ```scheme
   (define top 40)
   
   (define (f1)
     (let ()
       (let ()
         (let ()
           top))))
   (f1) ; 40
   
   (define (f2)
     (let ([top 41])
       (let ([top 42])
         (let ([top 43])
           top))))
   (f2) ; 43
   ```

3. **Macro scope**: an identifer and its binding both created by a macro, is only visible to other code created by the same macro.

   ```scheme
   (define-macro (make-macro-scoped-foo)
                 #'(begin
                    (define foo 42)
                    (* foo 2)))
   (make-macro-scoped-foo) ; 84
   foo ; unbound identifier
   ```

   But if a macro adds a binding to an existing identifier, that binding will not have macro scope. Instead, it adopts the scope of the identifier.

   ```scheme
   (define-macro (bind-existing-ident ID)
                 #'(begin
                    (define ID 42)
                    (* ID 2)))
   (bind-existing-ident foo) ; 84
   foo ; 42
   ```

   

