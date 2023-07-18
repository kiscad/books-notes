## Numbers

Racket 中的 number 和其他语言中的 number 有两点不同：

- Racket numbers 默认是 complex numbers。

  ```scheme
  (complex? 3) ; #t
  (real-part 3) ; 3
  (imag-part 3) ; 0
  (= 3 3+0i) ; #t
  (* +i +i) ; -1
  ```

- Racket 区分 **exact** and **inexact** numbers.

  - An *exact* number is a number whose real and imag parts are both integers or rational fractions.

  - Racket 默认情况下，尽可能使用 exact numbers。

    ```scheme
    (+ 1/3 1/5) ; 8/15
    ```

  - An *inexact* number 一般为浮点数，包含小数点的数。

  - 三角函数和对数函数的返回值都是 inexact numbers；含有 inexact number 的算数表达式，其结果也是 inexact number。

    ```scheme
    (exact? 3.0) ; #f
    (exact? 3.0+4i) ; #f
    (exact? (sin 1)) ; #f
    (exact? (* 3.0 3)) ; #f
    ```

  - Exact numbers 的计算效率一般比 inexact numbers 低一些。

    - `inexact->exact` 和 `exact->inexact` 可以对 exact 和 inexact numbers 进行相互转换。

- Racket 的常用 numberic functions，可以接受任意数量输入；其他语言一般只支持二元或一元运算。

  ```scheme
  (* 1 2 3 4) ; 1 * 2 * 3 * 4 = 24
  (/ 1 2 3 4) ; 1 / 2 / 3 / 4 = 1/24
  (< 1 2 3 4) ; 1 < 2 < 3 < 4 = true
  (apply < (range 100)) ; #t
  ```

- Racket 的整数字面量，也支持2，8，16 表示形式。

  ```scheme
  #x10 ; 16
  #o20 ; 16
  #b10000 ; 16
  ```

- Number 和 String 类型相互转换：`number->string`, `string->number`。