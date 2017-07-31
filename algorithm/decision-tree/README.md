## 决策树

#### 信息熵(Entropy)

> 随机变量的不确定性(复杂度)，不确定性越大，熵越大

<div align="center"><img src="http://latex.codecogs.com/svg.latex?H(x)=-\sum_{i=1}^{n}p(x_{i})log_{2}p(x_{i})" /></a></div>

假设随机变量<img src="http://latex.codecogs.com/svg.latex?\inline&space;x\in\left\{x_{1},x_{2},...,x_{n}\right\}" /></a>

* <img src="http://latex.codecogs.com/svg.latex?\inline&space;max\&space;p(x_{k})" /></a>越接近1，随机变量的不确定性越小，熵取值越接近最小值0
* <img src="http://latex.codecogs.com/svg.latex?\inline&space;p(x_{1})=p(x_{2})=...=p(x_{n})=\frac{1}{n}" /></a>时，随机变量的不确定性最大，熵取最大值<img src="http://latex.codecogs.com/svg.latex?\inline&space;log_{2}n" /></a>

#### 条件熵

> 在一个条件下，随机变量的不确定性

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\inline&space;H(Y|X)=\sum_{i=1}^{n}p(x_{i})H(Y|X=x_{i})" /></a></div>

#### 信息增益(Information Gain)

> 在一个条件下，信息不确定性减少的程度，信息增益 = 信息熵 - 条件熵

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\inline&space;G(Y|X)=H(Y)-H(Y|X)" /></a></div>

#### 信息增益极大化

<img src="http://latex.codecogs.com/svg.latex?\inline&space;H(Y)" /></a>固定，<img src="http://latex.codecogs.com/svg.latex?\inline&space;G(Y|X)" /></a>极大化 → <img src="http://latex.codecogs.com/svg.latex?\inline&space;H(Y|X)" /></a>极小化，进而<img src="http://latex.codecogs.com/svg.latex?\inline&space;H(Y|X=x_{i})" /></a>也要极小化

#### 决策树

1. 计算各个特征下Y的信息增益，取信息增益最大的特征来划分子集

2. 针对子集继续上述过程，直到子集为空或属于同一分类

#### 偏差(Bias)和方差(Variance)

#### 特征数

> 特征数越多，过拟合的可能性越大

#### 复杂度

> 特征数越多，复杂度越大
