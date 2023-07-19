[toc]

Racket 提供的数据结构有 pair, list, hash table, association list, vector, struct type。下面这些数据结构的对比表格

| Data Structure   | Access     | Values   | Index       | Mutable? |
| ---------------- | ---------- | -------- | ----------- | -------- |
| pair             | random     | two      | nothing     | no       |
| list             | sequential | variable | nothing     | no       |
| hash table       | random     | variable | keys        | optional |
| Association list | sequential | variable | `car`       | no       |
| vector           | random     | fixed    | integers    | optional |
| struct type      | random     | fixed    | identifiers | optional |

- Hash table, vector, 和 structure 三种类型都有 mutable 和 immutable 两种变体。能使用 immutable 类型变体就使用 immutable 变体；需要使用 mutable variant 才使用 mutable variant。

### 1. pairs

- A `pair` instance holds two values. Once created, it cannot be changed.

  ```scheme
  (cons 42 43)       ; '(42 . 43)
  (cons "see" "saw") ; '("see" . "saw")
  (cons 'this 'that) ; '(this . that)
  (cons + -)         ; '(#<procedure:+> . #<procedure:->)
  ```

- `car` 访问第一个 value，`cdr` 访问第二个 value。

  ```scheme
  (car (cons 42 43))       ; 42
  (cdr (cons 'this 'that)) ; 'that
  ```

- `pair?` predicate 判断一个 value 是否为 pair。

- pair 是一种比较底层的数据类型，其他的数据类型，如 list，是基于 pair 构建的。

### 2. lists

- `list` can hold any number of values
- `list` is made from a sequence of linked pairs，所以 list 适合遍历访问的场景
- 随机访问操作 `list-ref` 仅适合 short lists。

#### 2.1 `list` 和 `quote`

- 使用 `list` function 可以创建 list 实例

  ```scheme
  (list * 42 58) ; '(#<procedure:*> 42 58)
  (list)         ; '() empty list
  (list a b c)   ; error: `a` is not defined
  ```

- 使用 `quote`/`'`, 可以创建一个特殊的 list: `datum`

  ```scheme
  (quote (* 42 58)) ; 等价于 (list '* '42 '58)
  '(* 42 58)        ; 等价于 (list '* '42 '58)
  '()               ; 等价于 (list) empty list
  '(a b c)          ; 等价于 (list 'a 'b 'c)
  ```

- **注意**：对于有些输入参数 `list` function 和 `quote` function 可以产生等价的结果。

  对于 Racket，number, string 和 boolean 常量都认为是 "self-quoting" 的，即它们已经是 datum form 了。但是 variable identifiers 和 expressions 不是 "self-quoting" 的。

  Self-quoting 可以理解为：`42` 和 `'42` 是完全等价的。

  ```scheme
  (equal? (list 1 2 3) '(1 2 3))   ; true
  (equal? (list "a" #t) '("a" #t)) ; true
  (equal? (list + (* 6 7)) '(+ (* 6 7))) ; false
  ```

- List 的变量名一般以 `s` 结尾，已表明其包含多个 values。list of list 变量名可以用两个 `s` 结尾。

  ```scheme
  (define int 42)
  (define ints '(41 42 43))
  (define intss '((41 42 43) (44 45 46)))
  ```

#### 2.2 `quasiquote`

- `quasiquote` 的作用和 `quote` 是一样的，但 `quasiquote` 的参数 list 可以插入 expressions that will be evaluated before quoting。
- 感觉 `quasiquote` 有点类似于 format-string，可以在 runtime 创建不同的 datum。
- Quasiquote 也有两种形式：函数 `quasiquote` 和 prefix `` ` `` backtick

- 要在 quasiquote 中插入 single value，可以使用 `unquote` operator `,` 

  ```scheme
  (define x 42)
  `(41 ,x 43) ; '(41 42 43)
  ```

- 在 quasiquote 中插入 a list of values，可以使用 `unquote-splicing` operator `,@`

  ```scheme
  (define xs (list 42 43 44))
  `(41 ,@xs 45) ; '(41 42 43 44 45)
  ```

#### 2.3 List 基础操作函数

- `list?` 检查一个 S-expression 是否为 list

- `empty?` 检查一个 S-expression 是否为 empty list，等价于 `null?`

- `length` 计算 list 元素个数

- `flatten` 压平 nested list。

  ```scheme
  (flatten '(1 (2 3 (4 5 (6) 7) 8 9))) ; '(1 2 3 4 5 6 7 8 9)
  ```

- `apply` append a list of values to the argument list for a function

  ```scheme
  (+ 1 2 3 4 5 6 7 8 9) ; 45
  (apply + '(1 2 3 4 5 6 7 8 9)) ; 45
  ```

- `map` apply a function to every value in a list, and return a list of values.

  ```scheme
  (map abs (list -1 2 -3 4)) ; '(1 2 3 4)
  (map + '(1 2 3) '(10 20 30)) ; '(11 22 33)
  ```

- `for-each`, like `map`, apply a function to every value of a list; unlike `map`, ignore the return values.

  ```scheme
  (for-each displayln (list -1 2 -3 4))
  ```

- `filter` take the values from a list that match a predicate function, and discard the others.

  ```scheme
  (filter odd? '(1 2 3 4 5 6 7 8 9)) ; '(1 3 5 7 9)
  ```

- `cons` inserts a value at the front of a list.

- `append` joins multiple lists into a single list.

  ```scheme
  (append '(1 2 3) '(4 5 6) '(7 8 9)) ; '(1 2 3 4 5 6 7 8 9)
  ```

- `car` or `first` get the first value of a list.

- `cdr` or `rest` get the tail of a list after the first value.

- `range` makes a list of numbers

  ```scheme
  (range 6)       ; '(0 1 2 3 4 5)
  (range 1 6)     ; '(1 2 3 4 5)
  (range 1.5 6)   ; '(1.5 2.5 3.5 4.5 5.5)
  (range 0 6 2)   ; '(0 2 4)
  (range 0 3 0.5) ; '(0 0.5 1.0 1.5 2.0 2.5)
  ```

#### 2.4 Recursion with list

```scheme
(define (square x) (* x x))

(define (squarer xs)
  (if (empty? xs)
      empty
      (cons (square (first xs))
            (squarer (rest xs)))))
```

### 3. Vectors

- A **vector** is a fixed-length array of arbitrary values.

- Unlike list, a vector supports random access and update of its elements.

- A mutable vector can be made with `vector`.

- Values are retrieved with `vector-ref`, and changed with `vector-set!`.

  ```scheme
  (define vec (vector 'sym "str" 42)) ; '#(sym "str" 42)
  (vector-ref vec 0) ; 'sym
  (vector-set! vec 1 "bar")
  vec ; '#(sym "bar" 42)
  ```

- Vector written directly as expressions are immutable. 

  - For a vector as an expression, an optional length can be supplied.
  - A vector as expression implicitly `quote` its content.

  ```scheme
  #(name (that tune)) ; '#(name (that tune))
  #4(baldwin bruce)   ; '#(baldwin bruce bruce bruce)
  ```

- Vector 和 list 可以相互转换，`vector->list`, `list->vector`。

### 4. Hash Table

- A **hash table** is a mapping of keys to values, which can be any data type.

- Hash values can be retrieved with `hash-ref`.

- `hash` can create an immutable hash table.

  ```scheme
  (define ht (hash
              'foo "bar"
              '(1 2 3) expt
              42 #'(start-zombie-apocalypse)))
  (hash-ref ht '(1 2 3)) ; #<procedure:expt>
  (hash-ref ht 42) ; #<syntax:5:17 (start-zombie-apocalypse)>
  (hash-ref ht 'foo) ; "bar"
  ```

- `make-hash` can create a mutable hash table. For an mutable hash table, values can be added, deleted, or updated.

  ```scheme
  (define mht (make-hash))
  (hash-set! mht 'foo "bar")
  (hash-ref mht 'foo) ; "bar"
  (hash-set! mht 'foo 42)
  (hash-ref mht 'foo) ; 42
  ```

- hash table 默认使用 `equal?` 来 compare keys；

  - 如果所有 keys 都是 symbol，可以使用 `hasheq`, or `make-hasheq`，这种方式创建的 hash-table 使用 `eq?` comparing keys，速度很快。
  - 如果所有 keys 都是 symbol 或 number，可以使用 `hasheqv` 或 `make-hasheqv`，这种方式创建的 hash-table 使用 `eqv?` comparing keys，速度也较快。

### 5. Association List

- Association list 其实不是一种独立的数据结构，而是 list of pairs of key and value。

  ```scheme
  (define assns (list (cons 'k1 "v1") (cons 'k2 "v2")))
  (define assns (map cons (range 5) '(a b c d e)))
  
  (define keys (map car assns))
  (define vals (map cdr assns))
  ```

- `assoc` 可以通过 key 来查询 pair

  ```scheme
  (define assns (map cons (range 2 7) '(a b c d e)))
  (assoc 3 assns) ; '(3 . b)
  ```

- association list 可以当作 dictionary 使用

  ```scheme
  (require racket/dict)
  (define assns (map cons (range 2 7) '(a b c d e)))
  (dict-ref assns 3) ; 'b
  ```

### 6. struct type

- A **struct** type is a user-defined data structure with an arbitrary number of fields.

  - Like hash table, a struct type allows access to its fields by name.
  - Like Vector, the number of fields is fixed by the struct type definition.
  - A struct type 是一个独立的类型。

- `struct` form 默认定义了 a custom structure type, 然后定义了一些 predicts, getters, setters (when mutable) functions for each field.

  ```scheme
  (struct style
          (color size weight)
          #:transparent #:mutable)
  (define s (style "red" 42 'bold))
  s               ; (style "red" 42 'bold)
  (style? s)      ; #t
  (style-color s) ; "red"
  (set-style-color! s "blue")
  (style-color s) ; "blue"
  ```

  - Field option `#:transparent` 使得 struct type printable
  - Field option `#:mutable` 是的 fields mutable

### 7. Class

- **Class** 在 racket 中不像在其他语言中那么重要。但在 Racket 中，class 仅在个别 library 中使用，如 GUI framework。
  - 这主要是因为 class 依赖于 state and mutation，而 Racket 语言本身鼓励 immutable and functional。
  - 在 OOP 中，我们常常将 function 看作是 data object 的属性 (方法)；而在 FP 中，我们将 data object 看作是 function 的输入。