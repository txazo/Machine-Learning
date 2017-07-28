# 朴素贝叶斯

## 贝叶斯公式

贝叶斯公式:

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(A\cap&space;B)=P(A)*P(B|A)=P(B)*P(A|B)" /></a></div>

变形公式:

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(B|A)=\frac{P(A|B)*P(B)}{P(A)}" /></a></div>

* 先验概率:
    * P(A): A的先验概率
    * P(B): B的先验概率
* 后验概率:
    * P(A|B): B条件下A的后验概率
    * P(B|A): A条件下B的后验概率

#### 朴素贝叶斯

1. 目标函数

<div align="center"><img src="http://latex.codecogs.com/svg.latex?C=max(P(y_{i}|x))" /></a></div>

2. 应用贝叶斯公式进行概率转换

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(y_{i}|x)=\frac{P(x|y_{i})*P(y_{i})}{P(x)}" /></a></div>

3. 特征条件独立假设

<div align="center"><img src="http://latex.codecogs.com/svg.latex?P(y_{i}|x)=\frac{\prod_{j=1}^{n}P(x_{j}|y_{i})*P(y_{i})}{P(x)}" /></a></div>

4. 概率统计

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\left\{P(x_{1}|y_{i}),...,P(x_{j}|y_{i}),P(y_{i})\right\}" /></a></div>

#### 连续特征处理

> 假设连续特征值服从正态分布

正态分布的概率密度函数:

<div align="center"><img src="http://latex.codecogs.com/svg.latex?f(x)=\frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})" /></a></div>
