# 决策树

#### 最小分割样本数

#### 信息熵(Entropy)

> 随机变量的不确定性(复杂度)，不确定性越大，熵越大

<div align="center"><img src="http://latex.codecogs.com/svg.latex?H(x)=-\sum_{i=1}^{n}p(x_{i})log_{2}p(x_{i})" /></a></div>

假设随机变量<img src="http://latex.codecogs.com/svg.latex?\inline&space;x\in\left\{x_{1},x_{2},...,x_{n}\right\}" /></a>

* 
* <img src="http://latex.codecogs.com/svg.latex?\inline&space;p(x_{k})=\frac{1}{n}" /></a>时，熵的值最大为<img src="http://latex.codecogs.com/svg.latex?\inline&space;log_{2}n" /></a>

#### 条件熵

> 在一个条件下，随机变量的不确定性

#### 信息增益(Information Gain)

> 在一个条件下，信息不确定性减少的程度，信息增益 = 信息熵 - 条件熵

#### 偏差(Bias)和方差(Variance)

#### 特征数

> 特征数越多，过拟合的可能性越大

#### 复杂度

> 特征数越多，复杂度越大
