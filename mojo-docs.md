# Mojo language basics

- Mojo 是一门高性能的系统编程语言。

- 语法上，Mojo 借鉴了 Python 的简洁特点，兼容了 Python 的动态类型特性。同时 Mojo 支持系统编程需要的 type-safety, memory-safety 等特性。

- Mojo 是一门编译型语言，区别于 Python 的解释型语言。

  - Mojo 源码文件后缀为 `.mojo`
  - 有别于 Python，Mojo 的代码都要封装在 function 或 struct 内。程序的入口函数为 `main()`。

  

- Mojo 函数支持默认值参数和关键字参数



```python
fn pow(base: Int, exp: Int = 2) -> Int:
  return base ** exp
let z = pow(exp=3, base=2)
let z = pow(2)
```



- `fn` 函数参数支持 mutability/ownership specifiers 来保证函数的 memory safety。

- `borrowed` 为默认的 mutability specifier, 表示参数为 immutable references。`fn foo(x: Int):` 等价于 `fn foo(borrowed x: Int):`

- `inout` 可以将参数声明为 mutable reference，即函数对参数值的修改可以被外部观察到。

- `owned` 表示函数参数将通过值传递的方式获得一个 value 的唯一访问权。根据是否发生 value copy 可以分为两种方式：

  - 默认会发生 value copy。

    ```python
    fn foo(owned x: String) -> String:
      x += "~"
      return x
    fn main():
      let a: String = "hello"
      let b = foo(a)
      print(a) # "hello"
      print(b) # "hello~"
    ```

  - 实参变量加后缀 `^` 可以取消 value copy，即外部变量的值转移给函数参数，外部变量变为 uninitialized 状态。

- 程序的本质是 "data + operation"。function 是对 operation 的抽象；structure 是对 data 的抽象。

- `struct` 用来构建 abstractions of types

- 类似于 Python `class`，`struct` 也支持 methods, operator overloading, decorator 等

- 有别于 Python `class`，`struct` 是完全静态的，不支持 dynamic dispatch 和 runtime changes (如添加字段)

  ```mojo
  struct Pair:
    var first: Int
    var second: Int
    
    fn __init__(inout self, first: Int, second: Int):
      self.first = first
      self.secon = secon
    fn dump(self):
      print(self.first, self.second)
  ```

- Copy assignment

$$
\left\{ Va : \frac{D}{Vpx t + t}, \  Vp : \frac{D Vpx}{Vpx t + t}\right\}
$$

If you are dealing with objects created from the `gp` package, the useful algorithms are in the elementary curves and surfaces libraries.

The common math algorithms library provides a C++ implementation of the most frequently used mathematical algorithms.

表格：

<center><strong>表 2 全球/中国桌面操作系统市场份额占比（%）</strong></center>

| OS   | Windows | macOS | Unknown | Linux | Chrome OS | 其他 |
| ---- | ------- | ----- | ------- | ----- | --------- | ---- |
| 全球 | 76.56   | 17.1  | 2.68    | 1.93  | 1.72      | 0.01 |
| 中国 | 87.55   | 5.44  | 6.24    | 0.75  | 0.01      | 0.01 |



