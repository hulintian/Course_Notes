# 矩阵论

## 1.1 预备知识
- 自学

### 1.1.1 映射
- Def1 
    设$X$,$Y$为两个非空集合，若存在一个对应法则$f$，使得对$X$中的每个元素$x$，按照对应法则$f$，在$Y$中有唯一确定的元素$y$与之对应，则称$f$为从$X$到$Y$的映射，记作
    $$
        f : X \to Y 或 f : x \mapsto y = f(x), x \in X
    $$

    - 定义域
    - 值域
    - 两个映射相等（$f$和$g$为对应法则），要证明:
        - 定义域向同 $D_f = D_g$
        - 对应法则相同 $\forall x \in D_f=D_g$ 有$f(x) = g(x)$
    - 单射
    - 满射（满）
    - 双射（一一对应）

### 1.1.2 乘积映射
    
设$X,U,Y$是3个非空集合，有映射$g:X \to U$ 与 $y:U \to Y$ 由映射$g$对$\forall  x \in X, \exist !u = g(x) \in U$，再由映射 $y$ ，$\exist! y = f(u) \in Y$（其中，“$\exist!$”为**存在唯一的**）

对$\forall x \in X, \exist! y = f(u) = f[g(x)$形成了一个$X \to Y$的新映射，称为$f$与$g$的**乘积映射**（$g$与$f$的**复合映射**），记作$f \circ g: X \to Y$，即
$$
    (f \circ g)(x) = f[g(x)], x \in X,
$$
$u$ 称为中间元素

### 1.1.3 逆映射

- **单位映射**（恒等映射） $f: X \to X$，记作$I_X$

- 有非空集合$X,Y$，设有映射$f:X \to Y$和$g: Y \to X$，使得$f \circ g = I_Y$且$g \circ f = I_X$，则称 $f$ 是**可逆映射**，$g$ 为 $f$ 的**逆映射**记为$g = f^{-1}$
    - 案： $\\y=f(x),\\g(f(x)) = x, \\g(y) = x,\\f(g(y)) = y,\\f \circ g : Y \to Y$

### 1.1.4 数域

- Def2，设$\mathbb{F}$是复数集的非空子集，其中$0 \in \mathbb{F}$，$1 \in \mathbb{F}$，如果两个数的和、差、积、商（除数不为0）仍是$\mathbb{F}$中的数，则称$\mathbb{F}$为数域
    
        案：有零元，有单位元

- 闭包：在数集$P$中的任意两数作某一运算，运算结果仍在$P$中，称数集$P$对这个运算是**封闭的**

- 常用数域
    - 有理数域 $\mathbb{Q}$
    - 实数域 $\mathbb{R}$
    - 复数域 $\mathbb{C}$
    - 自然数集 $N$ 和 整数集 $Z$ 对除法运算不封闭，不是数域
    - 有理数域是任何数域的子集

### 1.1.5 实矩阵和复矩阵

- 若$\mathbf{A} = [a_{ij}]_{m \times n}，a_{ij}$均为实数（其中$i=1,2,\cdots,m;j=1,2,\cdots,n$）,则称$\mathbf{A}$为$m$行$n$列的实矩阵
- 若$\mathbf{A} = [a_{ij}]_{m \times n}，a_{ij}$均为复数（其中$i=1,2,\cdots,m;j=1,2,\cdots,n$）,则称$\mathbf{A}$为$m$行$n$列的复矩阵

- 矩阵的共轭 $\overline{\mathbf{A}}$
- 矩阵的共轭转置(埃尔米特Hermite) $\mathbf{A^{H}}$，具有的性质：
    1. $\overline{\mathbf{A} + \mathbf{B}} = \overline{\mathbf{A}} + \overline{\mathbf{B}}(\mathbf{A},\mathbf{B} \in \mathbb{C}^{m \times n})$;
    2. $\overline{\mathbf{A}  \mathbf{B}} = \overline{\mathbf{A}}  \overline{\mathbf{B}}(\mathbf{A} \in \mathbb{C}^{m \times s},\mathbf{B} \in \mathbb{C}^{s \times n})$;
    3. $\mathbf{A}^{H} = \overline{\mathbf{A}}^{T} = \overline{\mathbf{A}^{T}}(\mathbf{A} \in \mathbb{C}^{m \times n})$;
    4. $(\mathbf{A} + \mathbf{B})^{H} = \mathbf{A}^{H} + \mathbf{B}$;
    5. $(k\mathbf{A})^{H} = \overline{k}\mathbf{A}^{H},(k \in \mathbb{C};\mathbf{A} \in \mathbb{C}^{m \times n})$;
    6. $(\mathbf{AB}^{H}) = \mathbf{B}^{H}\mathbf{A}^{H}(\mathbf{A} \in \mathbb{C}^{m \times s},\mathbf{B} \in \mathbb{C}^{s \times n})$;
    7. $(\mathbf{A}^{H})^{H} = \mathbf{A}(\mathbf{A} \in \mathbb{C}^{m \times n})$

<!--#### 实矩阵与复矩阵对比

- 太多了，不想写了
| 实矩阵 | 复矩阵 |
| --- | --- |
| **向量的长度（模）**<br>向量 $\mathbf{\alpha} = $ | **向量的长度（模）**<br> |
-->

- 正交
- 需要复习 1.1.1 - 1.1.5 实矩阵、复矩阵
- 群、环？数域、有理数域、实数、复数域
- 共轭矩阵
- 转置 --> 共轭转置 Hermite
- 向量默认按列写
- **Hermite阵**：$\mathbf{A}^{H} = \mathbf{A}$
- 正交阵 -> 在复矩阵中 酉矩阵(Unitary Matrix)(复方阵$\mathbf{A}$满足$\mathbf{A}^{H}\mathbf{A} = \mathbf{E}$)
    
        案：酉是参照日语翻译，日语中“酉”为“unit”音译

- 相似，正交相似，酉相似
##### 矩阵合同定义

设 $A, B$ 是两个 $n \times n$ 的实矩阵（或复矩阵）。如果存在一个 **可逆矩阵** $P$，使得

$$
B = P^{T} A P
$$

那么称矩阵 $A$ 与 $B$ **合同**（congruent），记作

$$
A \cong B
$$

##### 相似(复矩阵称酉相似)

$$
    B = P^{-1} A P
$$

## 1.2 线性空间

- 参照现实主中的空间
    - 运算：加、数乘
    - 线性空间：更抽象的，点可以是任何东；“加法”、“数乘”，要求封闭，1 -- 单位元

- 线性空间的定义：
    - 。。。8条
    - 零元、单位元、对称
    - 验证线性空间，证明8条要满足的条件

- 常见的线性空间
    1. n维数组向量空间 $F^n(F)$（简记$F^n$）；n维实数组向量空间$R^n$；n维复数组向量空间$C^n$
    2. 数域F上一个一元多项式空间$F[x](F)$，简记为$F[x]$；次数小于n的多项式，再添上零多项式构成$F[x]_n$
    3. $F^{m \times n}$
    4. <!--区间$[a,b]$上连续的复数空间$C[]$-->

- 定理1 
    1. 零元唯一，负元唯一，如何证明？
    2. 加法消去率：$\forall x,y,z \in V if x+y = x+z, 则y=z$
    3. 
    4. 

- Def2: 线性表示
    $$ 
        \beta = k_1\alpha_1 + k_2\alpha_2 + \dots + k_m\alpha_m
    $$

- Def3: 线性相关、线性无关
    $$
        k_1\alpha_1 + k_2\alpha_2 + \dots + k_m\alpha_m = 0
    $$

- Def4: 级大无关组，秩

- 定理2：关于线性空间中向量组的性质

- Def5: 基底，维数$dim$（最小表示的一个架构，这个架构的个数）

- 定理3

- 常用空间的**自然基底**和**秩**

- Def6：坐标
