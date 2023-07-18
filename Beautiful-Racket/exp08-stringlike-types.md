Racket 中 stringlike types 包括了 `string`, `symbol`, `identifier`, `keyword` 和 `path string`。

- 这些 stringlike types 本质上都是 sequence of Unicode characters.
- stringlike types 之间可以相互转换。

### 1. String

- String 字面值，用双引号来表示。

  ```scheme
  "one string"
  "two \"strings\""
  ```

- By default, strings will print as literal expressions (can be reused as input).

  - To print strings in the friendly way, use `display` or `displayln`
  - To print strings in the raw style, use `print` or `println`

  ```scheme
  (display "two \"strings\"") ; two "strings"
  (print "two \"strings\"") ; "two \"strings\""
  ```

- Racket 提供了很多常见的 string-manipulation functions，如 `string-split`, `string-join`, `string-append`, `format` 等

### 2. Here string & @-expression

- Racket 支持两种方式来创建 multi-line strings。

  - **here string** starts with `#<<` and a delimiter name, followed by the string starting on the next line, ending with the delimiter on its own line.

    ```scheme
    (define str #<<here-string-delimiter
    A wonderful
    multiline string
    that goes on
    seemingly
    forever.
    here-string-delimiter
    )
    ```

  - **@-expression** is a special textual kind of S-expression, by adding the `at-exp` meta-language to the `#lang` line.

    ```scheme
    #lang at-exp br
    (define str @string-append{
      A wonderful
      multiline string
      that goes on
      seemingly
      forever.})
    (display str)
    ```

    相比于 here string，@-expression 可以嵌入 sub-expressions，类似于 string formatting。

    ```scheme
    #lang at-exp br
    (define base 2)
    (define pow 8)
    (define str @string-append{
      A wonderful
      multiline string
      that goes on
      @(number->string (expt base pow)) years.})
    (display str)
    ```

### 3. Symbol

- A **symbol** is like a string, but written with a single `'` prefix, rather than surrounding double quotes.

- A symbol cannot contain spaces unless the whole symbol is surrounded with `|` vertical bars.

  ```scheme
  'symbol ; 'symbol
  '|two-word symbol| ; '|two-word symbol|
  ```

- Symbols have a special property: they are **interned**.

  - Racket ensures that all instances of a particular symbol refer to only one object in memory.
  - Symbol comparision 可以使用 pointer comparing `eq?`，效率比 string comparison 要快。

- Symbol 和 String 可以相互转换，`string->symbol`, `symbol->string`。

### 4. Identifier

- An **identifier** is a name that appears in a program.

- Within a datum, an identifier is represented with a symbol.

  ```scheme
  (define foo "see")
  (define bar "saw")
  (string-append foo bar)
  '(string-append foo bar)
  ```

  - 在 S-expression `(string-append foo bar)` 中，`string-append`, `foo` 和 `bar` 都是 identifiers
  - S-expression 转换为 datum 后 `'(string-append foo bar)`，其中的 `string-append`, `foo` 和 `bar` 都是 symbols。

- Datum 可以手动进行 evaluate，这时其中的 symbols 将被转换为 identifier

  ```scheme
  (evaluate '(string-append foo bar))
  ```

  如果想 datum 中的 symbol 在 `evaluate` 时不变为 identifier，可以多加一个 `'` quote。

  ```scheme
  (evaluate '(cons 'foo 'bar)) ; '(foo . bar)
  (evaluate (list 'cons ''foo ''bar)) ; '(foo . bar)
  ```

### 5. Keyword

- A **keyword** is used to introduce a keyword argument either in a function definition or a call to that function.

  ```scheme
  (define (f #:base x #:pow y)
    (expt x y))
  (f #:base 2 #:pow 8) ; 256
  ```

- 一般情况下，keywords 不被看作是 data，而是作为 label。

### 6. Comment

- A line comment begins with `;`

- A multiline comment is delimited with `#|` and `|#`.

- A single S-expresison can be commented with `#;`.

  ```scheme
  ; comment
  "not a comment"
  #|
  a nice
  multiline
  comment
  |#
  (list 1 2 #;(list 'comment) 3 4)
  ```

### 7. Path String

- A **path string** is not a distinct type, but rather the subset of strings that can be converted into a valid **path**.

- Racket 的很多文件操作函数，即支持 path 也支持 path string。

  ```scheme
  (file-exists? (string->path "/usr/bin/racket"))
  (file-exists? "/usr/bin/racket")
  ```

### 8. Path

- A **path** represents a file location.
- Path 不是常见的 Unicode string，而是 byte string。
- 大多数文件路径都可以在 string 和 path 之间来回转换，`path->string`, `string->path`。
- It's unwise to manipulate paths by converting them to strings and back again.
  - `path->string` is intended for making user-readable version of paths.



