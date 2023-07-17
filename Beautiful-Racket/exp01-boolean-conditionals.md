## Booleans & Conditionals

### 1 Boolean

boolean 类型有两种取值 True 和 False。在 Racket 中。True 的常量值可以写成 `#t` 或 `#true`，False 的常量值可以写成 `#f` 或 `#false`。

在 predicate expressions 中，只有 `#f` value 被当作 False，其他任意 value 都被当作 True。

```scheme
(if #false  'true 'false) ; 'false
(if "#f"    'true 'false) ; 'true
(if 0       'true 'false) ; 'true
(if null    'true 'false) ; 'true
(if ""      'true 'false) ; 'true
(if (+ 0 0) 'true 'false) ; 'true
```

`not` 取非操作

```scheme
(not #f)    ; #t
(not #true) ; #f
(not 0)     ; #f
(not "")    ; #f
```

与或操作 `and` 和 `or` 支持短路机制。

```scheme
(and #f 'very-bad-thing)   ; #f
(or #t 'destroy-the-world) ; #t
```

All/Any 操作：`andmap` 和 `ormap` 可以对一个 list 中每个元素依次应用一个 predicate 函数，然后进行 “与”/”或“ 操作。

`andmap` 和 `ormap` 也是支持短路机制的。

```scheme
(andmap odd? '(1 2 3)) ; #f
(ormap even? '(1 2 3)) ; #t
```

### 2 Conditional

#### 2.1 `if` expression

==**if** expression== `(if test-expr then-expr else-expr)`。`test-expr` 是一个 predicate expression。`then-expr` 和 `else-expr` 两个分支只能包含单个表达式，如果分支需要包含多个表达式，可以将它们嵌套在 `let` expression 里。

```scheme
(if (= 42 (* 6 7))
    'true-result
    'false-result) ; 'true-result

(if (= 42 (* 6 7))
    (let ()
      "foo"
      42
      'true-result)
    'false-result) ; 'true-result
```

#### 2.2 `when` expression

==**when** expression==：`(when test-expr body ...+)`

如果只需要一个执行分支，可以使用 `when` expression。与 `if` expression 不同的是，`when` 的分支可以包含多个 expressions。

如果没有执行 `body` 的话，`when` expression 的 evaluation 结果为 `<#void>`。

```scheme
(when (= 42 (* 6 7))
      "foo"
      42
      'true-result)
```

#### 2.3 `cond` expression

==**cond** expression==：`(cond cond-clause ...)` 支持任意数量条件分支，每个分支包含一个 predicate 和 branch body: `[test-expr then-body ...+]`。执行过程中，会依次检查每个分支的 `test-expr`，直到遇到可执行的分支。

如果所有的分支都没有执行，`cond` expression 的结果为 `<#void>`。

```scheme
(cond
 [(= 42 (* 6 7))
  "foo"
  42
  'first-true-result]
 [(= 42 (+ 21 21)) 'second-true-result]
 [else 'else-result])
; 执行结果: 'fist-true-result
```

- 当 `cond-clause` 的 `then-body ...` 为空时，`cond-clause` 的 eval 结果为 `test-expr` 结果。

  ```scheme
  (cond
   [(or -42 #false)]
   [else 'else-result])
  ; 执行结果: -42
  ```

- `cond-clause` 中可以使用 `=>` operator 捕获 `test-expr` 的结果，供 `then-body` function 调用。

  ```scheme
  (cond
   [(or -42 #false) => abs]
   [else 'else-result])
  ; 执行结果: 42
  ```

#### 2.4 `case` expression

==**case** expression==:

```scheme
(case val-expr case-clause ...)
case-clause = [(datum ...) then-body ...+] | [else then-body ...+]
```

`case` expr 和 `cond` expr 语法结构相似，eval 逻辑如下

- At the top `val-expr` is the value to be compared.

- 每个 clause 的第一个元素为 list of items to compare；只要 `val-expr` `equal?` 其中一个元素，就会执行这个分支。

  `(datum ...)` 等价于 `'(val ...)`

```scheme
(define (c x)
  (case x
        [(foo bar)     'got-symbol]
        [("zim" "zam") 'got-string]
        [(42 84)       'got-number]
        [else          'got-nothing]))

(c 'foo)  ; 'got-symbol
(c "zim") ; 'got-string
(c 42)    ; 'got-number
(c #true) ; 'got-nothing
```

#### 2.5 `match` expression

==**match** expression== 

```scheme
(match val-expr clause ...)

clause = [pat body ...+]
       | [pat (=> id) body ...+]
       | [pat #:when cond-expr body ...+]
```

`match` is a more general version of `case`.

- `val-expr` is the value to be matched.
- `pat` in clauses, is the pattern to match.
- `body ...+` is evaluated and returned, when `pat` matches.
- `match` expr 通过**模式匹配**方式来选择执行分支。模式匹配比 `equal?` 更灵活强大。
- `match` 可以捕获 internal variables of `pat`, 用于 `body ...` evaluation。

```scheme
(struct thing (x y))

(define (m in)
  (match in
    ["foo"        'got-foo]    ; literal match
    [(? number?)  'got-number] ; predicate match
    [(list a b c) (list b)]    ; list match + assignment
    [(thing i j)  (+ i j)]     ; structure match + assignment
    [_            'no-match])) ; catches anything else

(m "foo")         ; 'got-foo
(m 42)            ; 'got-number
(m (list 1 2 3))  ; '(2)
(m (thing 25 52)) ; 77
(m "bar")         ; 'no-match
```

























