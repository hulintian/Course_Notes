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

- Def1.1.1 概率空间 
    - $设\Omega是样本空间，\Tau是\Omega的某些子集，若$
        1. $\Omega \in \Tau$
        2. $若A\in\Tau，\bar{A}\in\Tau$
        3. $若A_n\in\Tau,n=1,2,\dots ,则\bigcup^{\infty}_{n=1}\in \Tau称\Tau为事件域，或\sigma域$
    - 性质
        1. $\Phi \in \Tau$
        2. if$A,B\in\Tau$, then $A-B\in\Tau$
        3. if$A_n\in\Tau,n=1,2,\dots$ then $\cap^{\infty}_{n=1}A_n\in\Tau$
- Def1.1.2 概率
    - 设$\Omega为样本空间，\Tau是事件域，定义在\Tau上的实值函数P(\cdot)如果满足$
        1. $\forall A\in\Tau,P(A) \ge 0$
        2. $P(\Omega) = 1$
        3. $若A_n \in \Tau, n=1,2,\dots,且A_iA_j=\Phi, i \ne j i,j=1,2,\dots,则$
        $$
            P(\bigcup^{\infty}_{n=1}A_n) = \sum^{\infty}_{n=1}P(A_n)
        $$
        - $称P是(\Omega,\Tau)上的概率，P(A)为事件A的概率，(\Omega,\Tau,P)为概率空间$
- 概率性质
    1. $P(\Phi) = 0$
    2. $若A_i \in \Tau,i=1,2,\dots,n,A_iA_j = \Phi,i,j=1,2,\dots,n则\\
    P(\bigcup^{n}_{i=1}A_i) = \sum^{n}_{i=1}P(A_i)$
    3. $若A,B \in \Tau, A \subset B, 则P(B-A) = P(B) - P(A)$
    4. $若A,B \in \Tau, A \subset B, 则P(A) \le P(B)$
    5. $若A \in \Tau, 则 P(A) \le 1$
    6. $若A \in \Tau, 则 P(\bar{A}) = 1 - P(A)$
    7. $若A_n \in \Tau, n=1,2,\cdots, 则$ 
        $$P(\bigcup^{n}_{i=1}A_i) \le \sum^{n}_{i=1}P(A_i)$$
    8. $若A_n \in \Tau, n=1,2,\cdots, 则$ 
        $$
        \begin{aligned}
            P(\bigcup^{n}_{i=1}A_i) = 
                & \sum^{n}_{i=1}P(A_i) \\
                & - \sum_{1 \le i \le j \le n} P(A_iA_j) \\
                & + \sum_{1 \le i \le j \le k \le n} P(A_iA_jA_k) \\
                & - \cdots \\
                & + (-1)^{(n-1)} P(A_1A_2\cdots A_n)
        \end{aligned}
        $$

- 单调递增事件列: 一列事件$A_i,i=1,2,\cdots,n, A_n \subset A_{n+1}$
    $$
        lim_{x \to \infty} P(A_n) = P(\bigcup^{\infty}_{i=1} A_i)
    $$

- 单调递减事件列: 一列事件$A_i,i=1,2,\cdots,n, A_n \supset A_{n+1}$
    $$
        lim_{x \to \infty} P(A_n) = P(\bigcap^{\infty}_{i=1} A_i)
    $$


- 条件概率 Def （条件概率也是概率，能当概率来看）； $let (\Omega,\Tau,P)$
$$ 
P(B | A) = \frac{P(AB)}{P(A)}
$$


- 定理1.1.2 
    - 乘法公式
        - 若 $A_i \in \Tau , i = 1,2,...,n 且P(A_1A_2...A_n) > 0, 则$
        $$ 
        P(A_1A_2...A_n)  = P(A_1)P(A_2|A_1)P(A_3|A_1A_2)...P(A_n|A_1A_2...A_{n-1})
        $$
        - 条件概率拆分，或事件树视角
    - 全概率公式
        - $设B \in \Tau,A_i \in \Tau, P(A_i) > 0, i=1,2,..., 且A_iA_j=\Phi, i\neq j, i,j = 1,2, ..., \bigcup^{\infty}_{i=1} A_i \supset B 则$
    $$
        P(B) = \sum^{\infty}_{i=1}P(A_i)P(B | A_i)
    $$
        - 用于没办法直接求一个条件的概率时
    - Bayes 公式
        - $设B \in \Tau,P(B)>0, A_i \in \Tau, P(A_i)>0, i=1,2,...,且A_iA_j=\Phi, i \neq j, i,j=1,2,..., \bigcup^{\infty}_{i=1} A_i \supset B_i$
        $$
            P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum^{\infty}_{j=1}P(A_j)P(B|A_j)}
        $$

- 事件独立性
    - $设(\Omega,\Tau,P)是一个概率空间，A_i \in \Tau, i=1,2,\cdots,如果对于任意的k(1 \lt k \le n) 及 1 \le i_1 \lt i_2 \lt \cdots \lt k \le n, 有$
    $$
        P(A_{i_1}A_{i_2}\cdots A_{i_k}) = P(A_{i_1}) P(A_{i_2}) \cdots P(A_{i_k}) 则称A_1,A_2,\cdots,A_k 相互独立
    $$
        人话：A是样本空间的某个子集，A里面所有情况都发生的概率为A里面的每个情况发生的概率的积
    - 事件域的独立性
        - $若A,B相互独立则$
            - $A与\bar{B},\bar{A}与B相互独立$
            - $\Tau_{A} = \{A,\bar{A},\Phi,\Omega\}与\Tau_{B} = \{B,\bar{B},\Phi,\Omega\}$

- 定理1.1.3 A与B的（概率独立性2推广到事件域的）
- 定理1.1.4 $设A，B，C \in \Tau相互独立,则$下面的都相互独立（两个推广到三个）
    1. A 与 BC
    2. A 与 $B \bigcup C$
    3. A 与 $B - C$
    4. A所生存的事件域与B、C所生成的事件域

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
