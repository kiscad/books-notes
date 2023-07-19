### 1. Recursive function

- Recursion is the idea of designing a function so that it calls itself.

  ```scheme
  (define (factorial n)
    (if (= n 1)
        1
        (* n (fact (- n 1)))))
  (factorial 20)
  ```

- 每个 recursive function 都由两部分组成：recursive case 和 base cases。

  - In the **recursive case**, the task is broken down into smaller versions of the same task.
  - In the **base case**, the function reaches a terminating condition.

- 在 recursive function 实现中，常常用到 named `let` expression。

  ```scheme
  (define (n->s num [radix 10])
    (define digits
      (list->vector (string->list "0123456789abcdef")))
    (let loop ([num num] [acc empty])
      (cond
       [(zero? num) (if (empty? acc)
                        "0"
                        (list->string acc))]
       [else
        (define-values (q r) (quotient/remainder num radix))
        (loop q (cons (vector-ref digits r) acc))])))
  (n->s 46 2)  ; "101110"
  (n->s 46)    ; "46"
  (n->s 46 16) ; "2e"
  ```

### 2. Recursive data type

- Recursion 的思想也同样适用于 data type，即 a data type is defined partly in terms of themselves。
- Recursive data structure is described in terms of smaller versions of itself (a `list` is made of nested `list`s) until it reaches a terminating condition (the value `null`).

### 3. Why is recusion important

- 在 FP 中，Recursion 是一种非常常用的解题技巧，可以有效避免 state mutation。
- 很多 function languages 中的 data structures 也是 recursive type。

### 4. Tail recursion

- **Tail recursion** refers to the special case where the return value of the recursive branch is only the value of the next recursive call (tail call).

- 前面的 `factorial` 函数实现可以改写为 tail-recursive 形式。

  ```scheme
  (define (factorial n [acc 1])
    (if (= 1 n)
        acc
        (factorial (- n 1) (* acc n))))
  ```

### 5. Tail-call optimization

- Tail recursion has special status in Racket because the compiler notices tail calls and optimizes them.

> Ordinarily, each call to a function, causes another set of arguments to be saved on the **call stack**.
>
> Later, as the return values are calculated, arguments are removed from the call stack and replaced with the return values.

- Recursive functions 的层层调用，容易导致调用栈溢出 (stack overflow)。
- Racket 对于 tail call 的执行过程做了优化。
  - 在 tail call 场景下，the return value, is just the result the next call of the function, not depending on the current arguments.
  - 在执行过程中，Racket sees a tail call, it simply discards the current arguments on the call stack, and replaces them with the arguments of the tail call.
  - 这种执行优化，使得 tail call 并不会增加 call stack 开销。

