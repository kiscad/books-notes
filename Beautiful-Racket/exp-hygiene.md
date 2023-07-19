### 1. Hygiene

- **Hygiene** is the organizing policy of Racket's macro system.

  - Understanding hygiene is the key to understanding how macro work, and by extension, how to write good macros of your own.

- **Hygiene** answers: When the macro-generated code is evaluated, how should we *determine the bindings of the identifiers inside*?

- We have two choices:

  - Determine the binding according to what the identifiers mean at the place where the macro was defined. (**definition site**)

    This is Racket's default policy, and part of what is implied by hygiene.

  - Determine the bindings according to what the identifiers mean at the place where the macro was invoked. (**calling site**)

    Sometimes this is the behavior we want, so Racket lets us "break hygiene" when we need to.

- To determine the binding of an identifier, we look inside the **lexical context** attached to the code, which holds all the available bindings.

  So hygiene can be seen as a way of managing lexical contexts.

  ```scheme
  (define x 42)
  (define-macro (mac)
    #'(begin
       (define x 84)
       (println x)))
  (mac); 84
  (println x) ; 42
  ```

### 2. What problem does Hygiene solve?

- Hygiene can be seen as a way of making macros more composable, which is a general design goal of functional languages.
- Macros cannot know anything about the bindings used at the calling site.
- Therefore, the best way to ensure consistent behavior is to make macro generated code as self-contained as possible.

### 3. The golden rules

1. **Code produced by a macro adopts the lexical context of the macro-definition site.**

   ```scheme
   (define x 42)
   (define-macro (mac) #'(println x))
   (mac) ; 42
   ```

   上面代码中，the `mac` macro can create code that refers to `x`, because `x` has a binding at the macro-definition site, albeit outside the macro.

2. **Within code produced by the macro, new bindings can shadow existing bindings at the definition site** (similar to how `let` works).

   ```scheme
   (define x 42)
   (define-macro (mac)
     #'(begin
        (define x 84)
        (println x)))
   (mac); 84
   ```

3. **Bindings introduced by a macro are only visible to other code produced by that macro.**

   ```scheme
   (define x 42)
   (define-macro (mac)
     #'(begin
        (define x 84)
        (println x)))
   (mac) ; 84
   (println x) ; 42
   ```

   The corollary to this rule is that bindings introduced by a macro are **not visible outside** the macro.

   ```scheme
   (define-macro (define-x)
     #'(define x 42))
   (define-x)
   (println x) ; error: unbound identifier
   ```

4. **Every identifier retains its binding from its original lexical context.**

   ```scheme
   (define x 42)
   (define-macro (mac OUTER-X)
     #'(begin
        (define x 84)
        (println x)
        (println OUTER-X)))
   (mac x)
   ; 84
   ; 42
   ```

### 4. Breaking Hygiene

- Sometimes, a macro needs to introduce identifiers into the lexical context of the calling site. These identifiers are called **unhygienic**.

  - It's wise to reserve them until needed.

- A common use for unhygienic identifiers are macros that extend `define` by modify the given identifier name.

  ```scheme
  (define-macro (define-$ (ID ARG ...) BODY ...)
    (define id$-datum (format-datum '~a$ (syntax->datum #'ID)))
    (with-pattern ([ID$ (datum->syntax #'ID id$-datum)])
      #'(define (ID$ ARG ...)
          BODY ...)))
  (define-$ (f x) (* x x))
  (f$ 5) ; 25
  ```

  - we extract the datum from `#'ID` with `syntax->datum`.
  - we use `format-datum` to make a new datum with a `$` appended.
  - the *unhygenic identifier* is created with `datum->syntax`, where the first argument is the lexical context for the new identifier.
  - we match the new identifier to the pattern variable `ID$`.
  - Within the template, we use `ID$` in the name position of a standard `define` form.

- There's no best way to create an unhygienic identifier, but the machanics always remain the same.

  If the `syntax->datum`/`datum->syntax` gets tiresome, you can use `prefix-id` and `suffix-id` as helper functions to simplify creation of unhygienic identifiers.

  - They create a new identifier derived from the name and lexical context of an existing identifier.

  ```scheme
  (define-macro (define$ (ID ARG ...) BODY ...)
    (with-pattern ([ID$ (suffix-id #'ID '$)])
      #'(define (ID$ ARG ...)
          BODY ...)))
  (define-$ (f x) (* x x))
  (f$ 5) ; 25
  ```

  