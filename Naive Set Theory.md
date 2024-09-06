[公理化集合论 - 维基百科，自由的百科全书 (wikipedia.org)](https://zh.wikipedia.org/wiki/%E5%85%AC%E7%90%86%E5%8C%96%E9%9B%86%E5%90%88%E8%AE%BA)
## 1. 外延公理 (Axiom of Extension)

- **Set**，表示一些事物的集合。术语 Set 有时也写做 Collection 或 Class。
- 本书不关注 Set 的精确定义是什么，而关注 Set 具有哪些性质和操作。
- Set 内的事物称为 elements 或 members。Element 可以是原子对象也可以是 Set。
	- 本书的重点正是形而上的 Set 与 Set of sets
- **Belonging 属于关系** 是集合的一个基础概念，记作 $x\in A$
	- 如果 $x$ 是集合 $A$ 的 element，则称 $x \text{ belongs to } A$, 记作 $x\in A$
- Set 和 Element 的符号一般化约定：
	- Element 小写 Set 大写，比如 $a\in A$
	- Element 为字母表头部字母，Set 为字母表尾部字母，比如 $A \in X$
	- Element 为常规字体，Set 为花体，比如 $X \in \mathbb C$
- **Equality 相等关系** 是集合之间的基础关系，记作 $A = B$。
- **外延公理** 表述了集合的唯一性，即两个集合相等，当且仅当它们包含相同的元素。
- **Inclusion/Subset** 是两个集合的基础关系，如 $A \subset B$
	- Inclusion 具有反身性 (reflexive)，即 $A \subset A$
	- 真子集/真包含/proper inclusion: 当 $A\subset B$ 且 $A\neq B$ 时，$A$ 是 $B$ 的真子集。
	- Inclusion 具有传递性：当 $A\subset B$ 且 $B\subset C$, 那么 $A\subset C$
	- Inclusion 是反对称的，Equality 是对称的：如果 $A=B$ 那么 $B=A$
- Inclusion 与 Belonging 概念上相似，但存在重要的性质差异
	- Inclusion 具有反身性，而 Belonging 不具备
	- Inclusion 具有传递性，而 Belonging 不具有

## 2. 分类公理 Axiom of Specification

- 分类公理，也称为分离公理 (Axiom of Separation)：对于任意一个集合和一个性质，可以构造出一个包含所有满足该性质 (**assertion**) 的元素的子集。
- 断言 Assertion, 有两种基础形式 Assertion of belonging 和 Assertion of equality。
	- 所有其他 Assertion statement 都是通过逻辑运算符组合 primitive assertions 构造的。
- 构建复合断言的逻辑运算符有 7 种：
	- `and`
	- `or`
	- `not`
	- `if ... then ...` (implies)
	- `if and only if`
	- `for some` (exists)
	- `for all`
- 分类公理正式描述：对于任何集合 $A$ 和任何条件 $S(x)$, 都存在一个集合 $B$, 其中的元素恰好是 $A$ 中满足条件 $S(x)$ 的那些元素 $x$；即 $B=\{ x \in A : S(x)\}$。
	- 断言 Assertion 和 条件 Condition 意思相同。\

## 3. 无序对 Unordered Pairs

- 空集 $\varnothing$ 不包含任何元素。这是本书定义的第一个 Set。
	- 根据分类公理，$\varnothing = \{x\in A: x\neq x\}$, 其中 $A$ 为任意集合，即空集 $\varnothing$ 是任意集合的子集；
	- 根据延申公理，空集 $\varnothing$ 是唯一的。
- **配对公理 Axiom of Pairing**: 对于任意两个集合 $a$ 和 $b$, 一定存在一个集合 $A$ 使得 $a\in A$ 和 $b\in A$
	- 仅包含元素 $a$ 和 $b$ 的集合 $\{a, b\}$ 称为 (unordered) **pair**。
	- 根据分类公理，Pair $\{a, b\} = \{x\in A: x=a \text{ or }x=b\}$ 一定存在
	- 根据延伸公理，Pair $\{a, b\}$ 是唯一的
- 对于任意集合 $a$, 可以构建一个 unordered pair $\{a, a\}$，一般写做 $\{a\}$。
	- $\{a\}$ 称为 the singleton of $a$，其中 $\{a\}$ 和 $a$ 是两个完全不同的集合
	- Singleton 是一种特殊的 Unordered Pair.
	- 类似地，$\{\varnothing\}$ 是空集 $\varnothing$ 的 singleton。
- 一些记号约定
	- 条件 $S(x)$ 指定的集合，记作 $\{x: S(x)\}$
	- 如果 $S(x)=x=a \text{ or }x=b$, 那么 $\{x:S(x)\}$ 可以写做 $\{x: x=a\text{ or }x=b\}$ 或 $\{a, b\}$
	- 如果 $S(x) = x \in A$, 那么 $\{x: S(x)\}$ 等价于 $\{x:x\in A\}$ 和 $A$
	- 对于集合 $A$ 和条件 $S(x)$, $\{x: x\in A\text{ and }S(x)\}$ 也会写作 $\{x\in A: S(x)\}$
- Class 是比 Set 更模糊和泛化的概念
	- 一个 Condition 指定的“集合”，或者 the extension of a condition, 称为 Class。

## 4. Unions and Intersections 并集和交集

- **并集公理 Axiom of Union**: 对于任意一组集合（set of Sets) $\mathcal C = \{X: X\in \mathcal C\}$，都存在一个集合 $U$，使得对于任意元素 $x\in X$，那么 $x\in U$。
	- 根据分类公理，并集公理可以表示为 $\{x\in U: x\in X \text{ for some } X\in\mathcal C\}$ 或 $U = \{x: x\in X \text{ for some }X\in\mathcal C\}$
	- 上面的 $x\in X \text{ for some } X\in \mathcal C$ 也会写作：$\text{for some }X (x\in X \text{ and }X\in\mathcal C)$
- 集合 $U$ 称为这组集合 $\mathcal C$ 的并集，常常记作 $\bigcup\mathcal C$,  $\bigcup \{X:X\in\mathcal C\}$ 或 $\bigcup_{X\in\mathcal C} X$
- 并集，具有如下一些基础性质
	- 空集的并集是空集 $\bigcup\{X:X\in\varnothing\} = \varnothing$ 或者 $\bigcup \varnothing = \varnothing$
	- 集合 $A$ 的 singleton 的并集是 $A$: $\bigcup\{X:X\in\{A\}\} =A$ 或者 $\bigcup\{A\} = A$
	- Pair of sets 的并集 $\bigcup\{X:X\in\{A,B\}\}$ 记作 $A\cup B = \{x:x\in A\text{ or }x\in B\}$
		- 特例：pair $\{a, b\} = \{a\} \cup \{b\}$
		- 三元组 triple: $\{a, b, c\} = \{a\}\cup\{b\}\cup\{c\}$
		- 四元组 quadruple 也类似
	- $A \cup \varnothing = A$
	- 交换律：$A\cup B = B\cup A$
	- 结合律：$A\cup(B\cup C) = (A\cup B)\cup C$
	- 幂等性：$A\cup A = A$
	- $A\subset B\text{ if and only if } A\cup B = B$
- **交集 Intersection**：$A\cap B = \{x: x\in A\text{ and }x\in B\}$ 
	- 更一般化的情况，可以写成 $V = \{x: x\in X \text{ for every } X\in \mathcal C\}$
- 交集，具有的一些基础性质 (facts)
	- $A\cap \varnothing = \varnothing$
	- $A\cap B = B\cap A$
	- $A\cap(B\cap C) = (A\cap B)\cap C$
	- $A\cap A = A$
	- $A\subset B\text{ if and only if }A\cap B=A$
- **互斥 disjoint**：如果两个集合 $A\cap B=\varnothing$, 那么集合 $A$ 和 $B$ 被称为是互斥的。
	- 如何一组集合(set of sets) 中两两互斥，则称这组集合是互斥的 pairwise disjoint。
- **分配律 Distributive law**:
	- $A\cap(B\cup C) = (A\cap B)\cup(A\cap C)$
	- $A\cup(B\cap C) = (A\cup B)\cap(A\cup C)$

## 5. 补集和幂集 Complements and Powers

- **相对补集 Relative Complement**：集合 $A$ 和 $B$ 的差集 $A-B$, 也称为 $B$ 在 $A$ 中的相对补集。
	- $A-B = \{x\in A: x\notin B\}$
- 绝对补集 absolute complement：集合 $A$ 的绝对补集记作 $A^{\complement}$
	- $(A^{\complement})^{\complement} = A$
	- $\varnothing^\complement = E,\quad E^\complement = \varnothing$, 其中任何集合都是集合 $E$ 的子集
	- $A\cap A^\complement = \varnothing,\quad A\cup A^\complement = E$
	- $A\subset B\text{ if and only if } B^\complement \subset A^\complement$
	- De Morgan 定律: $(A\cup B)^\complement = A^\complement \cap B^\complement,\quad (A\cap B)^\complement = A^\complement\cup B^\complement$
- **对称差 symmetric difference**: $A+B = (A-B)\cup(B-A)$, 也称为布尔和 Boolean sum.
	- $A + \varnothing = A$
	- $A + A = \varnothing$
	- $A+B = B+A$
	- $A + (B+C) = (A+B) + C$
- 由于不存在一个包罗万象的 Universe Set, 上面的一些操作会出现令人困惑的情况。
	- 我们往往聚局限于某个特定集合 $E$ 及其子集的集合 $\mathcal C$，$\{x\in E:\}$。
- **幂公理 Axiom of power**: 对于任意一个集合 $E$ 都存在一个集合 $\mathcal P$, 使得如果 $X\subset E$ 则 $X\in\mathcal P$.
	- 幂集 $\mathcal P(E) = \{X: X\subset E\}$
	- $\mathcal P(\varnothing) = \{\varnothing\}$
	- $\mathcal P(\{a\}) = \{\varnothing, \{a\}\}$
	- $\mathcal P(\{a, b\}) = \{\varnothing, \{a\}, \{b\}, \{a,b\}\}$
	- 一个 $n$-elements 集合的幂集包含 $2^n$ 个元素。
	- $E = \bigcup \mathcal P(E)$
	- $\bigcap \mathcal P(E) = \varnothing$

## 6. 有序对 Ordered Pairs

- 有序对，是一个基础的数学概念，用于表示两个元素之间的关系。表示形式为 $(a, b)$, 其中 $a$ 是第一个元素，$b$ 是第二个元素。
- 有序对 $(a, b)$ 可以被定义为集合 $\{a, \{a, b\}\}$。
	- 如果 $a\neq b$, 则 $(a,b)=\{\{a\},\{a,b\}\}$ 和 $(b, a)=\{\{b\},\{a, b\}\}$ 表示不同的有序对
	- 如果 $a=b$, 则 $(a,b)=(b, a)=\{\{a\}\}$ 表示同一个有序对
- Cartesian product 笛卡尔积：描述了两个集合形成的所有可能有序对的集合。
	- 集合 $A$ 和 $B$ 的笛卡尔积定义为 $A\times B = \{(a, b)|a\in A\text{ and }b\in B\}$
- 给定有序对集合 $R$，计算每个有序对第 1 或 2 个元素的集合，称为投影操作 (projection)。
	- $A = \{a: \exists\ b \text{ s.t. }(a, b)\in R\}$
	- $B=\{b:\exists\ a\text{ s.t. } (a, b)\in R\}$
- 有序对的应用：
	- 坐标系：在平面直角坐标系中，点的坐标是实数集 $\mathbb R$ 的笛卡尔积 $\mathbb R\times\mathbb R$
	- 关系和函数：如果 $R$ 是集合 $A\times B$ 的子集，那么 $R$ 就是从 $A$ 到 $B$ 的关系；函数则是特定类型的关系
	- 数据结构：笛卡尔积用于定义数据结构，如元组和记录
	- 概率论：笛卡尔积用于描述两个随机变量的联合分布

## 7. Relations 关系

- 基于有序对和笛卡尔积，我们可以定义 **Relation 关系**为有序对的集合：
	- 设 $A$ 和 $B$ 为集合，若 $R\subset A\times B$，称 $R$ 为从 $A$ 到 $B$ 的二元关系，简称关系。
	- 当 $A=B$ 时，称 $R$ 为 $A$ 上的二元关系；
	- 若 $(a,b)\in R$, 可以简记为 $aRb$
- 一个关系 $R$ 在第一和第二个元素的投影，称为 the **domain** and the **range** of $R$，记作 $\text{dom }R$ 和 $\text{ran } R$.
	- $\text{dom } R = \{ x\ |\ \exists\ y\text{ s.t. } x R y\}$
	- $\text{ran }R = \{y\ |\ \exists x\text{ s.t. } x R y\}$
- Relations 的一些特例
	- 空关系 $\varnothing$
	- 如果关系 $R\subset X\times Y$, 则称 $R$ 为 a relation from $X$ to $Y$
	- 如果关系 $R\subset X\times X$, 则称 $R$ 为 a relation in $X$
	- 如果 $xRx\text{ for all }x\in X$, 则称 $R$ 具有自反性 (Reflexive)
	- 如果 $xRy$ implies $yRx$, 则称 $R$ 具有对称性 (symmetric)
	- 如果 $xRy$ and $yRz$ implies $xRz$, 则称 $R$ 具有传递性 (transitive)
- 一个关系 $R$ in $X$ 称为**等价关系 (Equivalence relation)**, 如果 $R$ 具备自反性 (reflexivity)、对称性 (symmetry) 和传递性 (transitivity)。
	- 最小的等价关系是恒等关系 (relation of equality) $I_A=\{(x,x)\ |\ x\in A\}$
	- 最大的等价关系是Cartesian product $E_X=X\times X$
- 集合 $X$ 的**划分 (Partition)** 是由 $X$ 的若干个非空子集构成的集合 $\mathcal C$, 其中这些子集互不相交，且并集为原集合 $X$.
- 等价关系与集合划分：等价关系为集合的划分提供了一个结构化的方式。每一个划分都可以通过定义适当的等价关系来实现。
	- **等价类**：对于一个等价关系 $R$ 和元素 $x\in X$, 所有与 $x$ 等价的元素的集合，称为等价类 $[x]$，即 $[x]=\{t\in X\ |\ xRt\}$。
		- 所有的等价类构成的集合，称为一个划分 Partition。
		- 对于恒等关系，每个等价类都是一个 singleton.
		- 对于 Cartesian product, 只存在一个等价类，即 $X$ 自身
	- **商集**：由一个等价关系所定义的划分称为 $X$ 关于 $R$ 的商集，记作 $X/R$，其中每个元素都是一个等价类。

## 8. Functions 函数

- 给定两个集合 $X$ 和 $Y$, 如果关系 $f\subset X\times Y$ 满足如下条件：
	- **单值性**：对于每个元素 $x\in X$，都存在唯一的元素 $y\in Y$, 使得 $(x, y)\in f$
	- **全域性**：对于每个元素 $y\in Y$, 都存在至少一个元素 $x\in X$，使得 $(x,y)\in f$
	- 则称关系 $f$ 是从 $X$ 到 $Y$ 的一个函数，记作 $f: X\rightarrow Y$
- 记号
	- 对于函数，我们一般将 $(x,y)\in f$ 或 $xfy$ 写做 $f(x)=y$ 形式
	- $x$ 称为 argument, $y$ 称为 value；$f(x)=y$ 读作 $f$ maps or transforms $x$ into $y$.
	- 所有的函数 $f: X\rightarrow Y$ 都是 power set $\mathcal P(X\times Y)$ 的子集，power set 也记作 $Y^X$
	- 




