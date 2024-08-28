### 1. Syntax pattern

- A **syntax pattern** is a tool for matching elements within a **syntax object**.

  - Syntax patterns are used extensively in macros, especially for separating the input into named pieces so they can be rearranged.

- `define-macro` and `define-macro-cases` rely on syntax patterns to define calling patterns.

  ```scheme
  (define-macro (m foo) #'"match")
  (m foo) ; "match"
  (m bar) ; error: no matching case for pattern
  ```

  - The macro `m` only matches the literal identifier `foo`.

  ```scheme
  (define-macro-cases m2
    [(m2) "first"]
    [(m2 foo) "second"]
    [(m2 foo ARG) #'ARG]
    [else "no match"])
  (m2) ; "first"
  (m2 foo) ; "second"
  (m2 foo "bar") ; "bar"
  (m2 bar) ; "no match"
  ```

### 2. Syntax template

- Syntax patterns cooperate closely with **syntax templates**.

- A syntax template is an expression that creates a syntax object.

  Within a macro definition or `with-pattern` expression, any datum prefixed with `#'` is treated as a syntax template.

  In a syntax template, internal references to pattern variables created by earlier syntax patterns are automatically replaced with their underlying matched value.

- Syntax pattern are often used throughout a macro to destructure syntax objects and syntax templates.

  ```scheme
  (define-macro (m3 MID ... LAST)
    (with-pattern ([(ONE TWO THREE) (syntax LAST)]
                   [(ARG ...) #'(MID ...)])
      #'(list ARG ... THREE TWO ONE)))
  (m3 25 42 ("foo" "bar" "zam")) ; '(25 42 "zam" "bar" "foo")
  ```

  - `(m3 MID ... LAST)` is a syntax pattern that defines the possible input arguments to the macro, and matches them to pattern variables.
  - `(syntax LAST)` is a syntax template containing only the element matched by `LAST`. This element is matched/destructured into another syntax pattern, `(ONE TWO THREE)`.
  - `#'(MID ...)` is a syntax template containing the elements matched by `MID ...`. These elements are matched to the syntax pattern `(ARG ...)`.
  - `#'(list ARG ... THREE TWO ONE)` is a syntax template containing the matched elements inside a `list`.

### 3. Vocabulary

A syntax pattern 可以由 5 种类型组成

1. ==**literal**==, which only matches itself. Numbers, strings, and symbols are always literals.

   In `define-macro`, `define-macro-cases`, and `with-pattern`, identifiers that are not in UPPERCASE are treated as literals.

   ```scheme
   (define-macro-cases num
     [(num 42) "match"]
     [else "nope"])
   (num 42) ; "match"
   (num 25) ; "nope"
   
   (define-macro-cases str
     [(_ "foo") "match"]
     [else "nope"])
   (str "foo") ; "match"
   (str foo) ; "nope"
   
   (define-macro-cases sym
     [(_ 'foo) "match"]
     [else "nope"])
   (sym 'foo) ; "match"
   (sym 'bar) ; "nope"
   
   (define-macro-cases id
     [(id foo) "match"]
     [else "nope"])
   (id foo) ; "match"
   (id bar) ; "nope"
   ```

   对于 literal identifier 的匹配需要注意的是，它不仅匹配 name 而且匹配 binding。

   ```scheme
   (module mod br
     (provide mac)
     (define foo 0)
     (define-macro-cases mac
       [(_ foo) "match"]
       [else "nope"]))
   
   (require (submod "." mod))
   (mac foo) ; "nope"
   ```

   上面的代码中，macro 定义中 `foo` literal 有 binding 且在 `mod` 内。 而在 `(mac foo)` 调用中 `foo` 没有 binding。感觉 identifier literal 没有合适的应用场景。

2. ==**pattern variable**== (or wildcard), which can match anything (including a list of things) and assigns the matched item a name.

   Once a pattern variable is defined, all appearances of the pattern variable within a syntax object are replaced with the matched value.

   ```scheme
   (define-macro (self ARG) #'ARG)
   (self "foo") ; "foo"
   (self (list 1 2 3)) ; '(1 2 3)
   
   (define-macro (add-three ARG) #'(+ ARG ARG ARG))
   (add-three 42) ; 126
   ```

   The special wildcard `_` can matches anything, and can be used any times in a syntax pattern, but it cannot appear in a syntax template.

   - It's useful for signaling that an element of the syntax datum is being ignored.

   ```scheme
   (define-macro (odds FIRST _ THIRD _ FIFTH)
     #'(list FIRST THIRD FIFTH))
   (odds 1 2 3 4 5) ; '(1 3 5)
   ```

3. ==**sublist pattern**==, will only match elements arranged with the same parenthesization.

   If you know a certain element will be a list, a sublist pattern can be used to immediately match elements inside that list. Sublist patterns can be nested to any depth.

   ```scheme
   (define-macro (m NUMS)
     (with-pattern ([(FIRST SECOND THIRD) #'NUMS])
       #'(list THIRD SECOND FIRST)))
   (m (1 2 3)) ; '(3 2 1)
   
   (define-macro (m2 (FIRST SECOND THIRD))
     #'(list THIRD SECOND FIRST))
   (m2 (1 2 3)) ; '(3 2 1)
   ```

4. ==**ellipsis**==, which has to follow a pattern variable, and matches as many items as it can (similar to the "greedy" `*` operator in regex).

   ```scheme
   (define-macro (ellip ARG ...)
     #'(list ARG ...))
   (ellip 1 2 3)   ; '(1 2 3)
   (ellip "a" "b") ; '("a" "b")
   (ellip)         ; '()
   ```

   If a pattern variable has an ellipsis, when the variable appears in template, the ellipsis must also appear.

   ```scheme
   (define-macro (bad-ellip ARG ...)
     #'(list ARG))
   ; error: missing ellipsis with pattern variable in template
   ```

   You can only have one ellipsis in each sublist of the pattern, including the top level.

   ```scheme
   ; OK: one ellipsis per sublist
   (define-macro (m (FOO ...) (BAR ...))
     #'(list FOO ... BAR ...))
   (m (1 2 3) (4 5 6)) ; '(1 2 3 4 5 6)
   
   ; not OK: two ellipsis at top level, (BAR ...) always empty
   (define-macro (m2 FOO ... BAR ...)
     #'(list BAR ... FOO ...))
   (m2 1 2 3 4 5 6) ; '(1 2 3 4 5 6)
   ```

5. ==**dot**==, which has to precede a pattern variable at the end of a list, and matches all remaining items in the list starting at the dot.

   The resulting pattern variable can be used in two ways:

   - used alone, it's treated as a list of items;
   - used with another dot, it's spliced into the result.

   ```scheme
   (define-macro (m . ARGS) #'ARGS)
   (m + 1 2 3) ; 6
   
   (define-macro (m2 . ARGS) #'(list . ARGS))
   (m2 + 1 2 3) ; '(#<procedure:+> 1 2 3)
   ```

### 4. Limitations

- 这里的 syntax pattern 有一些局限，比如无法提供 optional match，类似于 `?` in regex。
- `syntax/parse` library 提供了更丰富的 vocabulary of syntax patterns.

