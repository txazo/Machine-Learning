# 决策树

#### 最小分割样本数

#### 信息熵(Entropy)

> 随机变量的不确定性(复杂度)，不确定性越大，熵越大

<div align="center"><img src="http://latex.codecogs.com/svg.latex?H(x)=-\sum_{i=1}^{n}p(x_{i})log_{2}(x_{i})" /></a></div>

* 只有一种类别时，熵的值最小，为0
* 每种类别的概率相同时，熵的值最大，为<img src="http://latex.codecogs.com/svg.latex?log_{2}N" /></a>，N为类别数

#### 条件熵

> 在一个条件下，随机变量的不确定性

#### 信息增益(Information Gain)

> 在一个条件下，信息不确定性减少的程度，信息增益 = 信息熵 - 条件熵

#### 偏差(Bias)和方差(Variance)

#### 特征数

> 特征数越多，过拟合的可能性越大

#### 复杂度

> 特征数越多，复杂度越大
