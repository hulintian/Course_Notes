# 随机过程
- 教材

# 概率论基础
- review

- 概率空间
- 特征函数

### 概率空间

- example: 抛硬币

- 样本空间： 一个集合，所有元素是实验的全体结果
- 样本点：一个试验的结果
- 随机事件：样本空间的某个子集

- 概率空间
- 概率
- Def:
- 事件域

- 概率性质

- 单调递增事件列
- 单调递减事件列

 $$ lim $$

- 条件概率 Def （条件概率也是概率，能当概率来看）； $let (\Omega,\Tau,P)$
$$ 
P(B | A) = \frac{P(AB)}{P(A)} 
$$


- 定理1.1.2 乘法公式
    - 若 $A_i \in \Tau , i = 1,2,...,n 且P(A_1A_2...A_n) > 0, 则$

    $$ 
    P(A_1A_2...A_n)  = P(A_1)P(A_2|A_1)P(A_3|A_1A_2)...P(A_n|A_1A_2...A_{n-1})
    $$

    - 条件概率拆分，或事件树视角

- 全概率公式
    - $设B \in \Tau,A_i \in \Tau, P(A_i) > 0, i=1,2,..., 且A_iA_j=\Phi, i\neq j, i,j = 1,2, ..., \cup^{\infty}_{i=1} A_i \supset B 则$

$$
    P(B) = \sum^{\infty}_{i=1}P(A_i)P(B | A_i)
$$
    - 用于没办法直接求一个条件的概率时

- Bayes 公式
    - $设B \in \Tau,P(B)>0, A_i \in \Tau, P(A_i)>0, i=1,2,...,且A_iA_j=\Phi, i \neq j, i,j=1,2,..., \cup^{\infty}_{i=1} A_i \supset B_i$

    $$
        P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum^{\infty}_{j=1}P(A_j)P(B|A_j)}
    $$

- 事件独立性
    - 事件域的独立性

- 定理1.1.4 $设A，B，C \in \Tau相互独立,则$
    1. A 与 BC
    2. A 与 $B \cup C$
    3. A 
    4. ..

## 随机变量及分布
- 随机变量是概率论的主要研究对象
- 试验结果是数值化的，或与数值相联系的
- 用分布函数描述概率特性

- Def 1.2.1 $设(\Omega,\Tau, P)为一概率空间，定义在\Omega上的实值函数X(.)，如果 \forall x \in R, {\omega | X(\omega) \leq x} \in \Tau，则称X是\Tau的随机变量（Random Varible, r.v.）称$
$$
F(x) = P(X \leq x)  - \infty \lt x \lt + \infty \\
为随机变量X的分布函数（Cumulative Distrubution Function, \textbf{CDF}）.
$$

- 分布函数$F(x)$的性质：
    - 和函数相关的性质都适用
    - 单调不减
    - 右连续
    -  $F(-\infty) == lim_{x \to -\infty}F(x) = 0$
    -  $F(\infty) == lim_{x \to \infty}F(x) = 1$

- 随机变量类型：离散&连续

- 离散型随机变量
    - 随机变量X可取有限个或可列无限个
    - 用分布率描述 $\textbf{PMF}$
    $$
    P(X = x_i) = p_i, i=1,2,...
    $$

- 连续型随机变量
    - $设随机变量X的分布函数为F(x)，如果存在非负可积符函数f(x)$
    - 概率密度函数（$\textbf{PDF}$） $f(x)$

    $$
    F_X(x) = P(X \leq x) = \int^{x}_{-\infty} f_X(t)dt
    $$

- Def 1.2.2 n维随机变量（n维随机向量）

# TODOs
- 回忆微积分系列公式
