# 朴素贝叶斯

#### 贝叶斯公式

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(A\cap&space;B)=P(A)*P(B|A)=P(B)*P(A|B)" /></a></div>

变形公式:

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(B|A)=\frac{P(A|B)*P(B)}{P(A)}" /></a></div>

#### 朴素贝叶斯

1. 目标函数

<div align="center"><img src="http://latex.codecogs.com/svg.latex?y=arg\&space;\underset{c_{k}}{max}\&space;P(y=c_{k}|X)" /></a></div>

2. 应用贝叶斯公式进行概率转换

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(y=c_{k}|X)=\frac{P(X|y=c_{k})*P(y=c_{k})}{P(X)}" /></a></div>

3. 特征条件独立假设

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(y=c_{k}|X)=\frac{\prod_{j=1}^{n}P(x_{j}|y=c_{k})*P(y=c_{k})}{P(X)}" /></a></div>

4. 概率统计

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(x_{j}|y=c_{k})=\frac{I(x_{j},y=c_{k})}{I(y=c_{k})},P(y=c_{k})=\frac{I(y=c_{k})}{I}" /></a></div>

#### 连续特征处理

> 针对连续值的特征，假设连续特征值服从正态分布

使用正态分布的概率密度函数计算:

<div align="center"><img src="http://latex.codecogs.com/svg.latex?f(x)=\frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})" /></a></div>

#### 拉普拉斯平滑

> 针对零概率，加1处理

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(x_{j}|y=c_{k})=\frac{I(x_{j},y=c_{k})}{I(y=c_{k})}\rightarrow&space;P(x_{j}|y=c_{k})=\frac{I(x_{j},y=c_{k})&plus;1}{I(y=c_{k})&plus;k}" /></a></div>

其中，`k`为`y`的类别数

#### 对数似然

> 概率过小，可能导致概率乘积溢出，解决办法为取对数

<div align="center"><img src="http://latex.codecogs.com/svg.latex?logP(y=c_{k}|X)=\sum_{j=1}^{n}logP(x_{j}|y=c_{k})&plus;logP(y=c_{k})-logP(X)" /></a></div>
