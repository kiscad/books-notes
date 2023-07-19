## Equality

- Racket 提供了多种不同的 fucntions 用于测试 the equality of two items。

  - 不同的 equality functions 性能和功能有些差异。

- `equal?` gives the right answer for all data types, though it's the slowest of the equality functions.

  ```scheme
  (equal? "foobar" (string-append "foo" "bar")) ; #t
  (equal? 42 (* 6 7)) ; #t
  (equal? 'symbol (string->symbol "symbol")) ; #t
  ```

- `eq?` 主要用于 symbols, small integers, objects。

  - `eq?` 比 `equal?` 快很多，因为它仅检查两个 items 的内存地址是否相同 (pointer comparison)。

  ```scheme
  (eq? "foobar" (string-append "foo" "bar")) ; #f
  (eq? '(1 2 3 4) (append '(1 2) '(3 4))) ; #f
  (eq? 42 (* 6 7)) ; #t
  (eq? (expr 9 999) (expt 9 999)) ; #f
  (eq? 'symbol (string->symbol "symbol")) ; #t
  ```

- `eqv?` 在 `eq?` 的基础上，可以正确比较 characters 和所有 numbers。

  ```scheme
  (eqv? 'symbol (string->symbol "symbol")) ; #t
  (eqv? (expt 9 999) (expt 9 999)) ; #t
  ```

- `=` 只能用于 number comparison.

  ```scheme
  (= 42 (* 6 7)) ; #t
  (= '(1 2 3) '(2 3 4)) ; error
  ```

  