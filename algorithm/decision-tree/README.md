## 决策树

#### 随机变量的不确定性

随机变量<img src="http://latex.codecogs.com/svg.latex?\inline&space;X" /></a>，取值集合为<img src="http://latex.codecogs.com/svg.latex?\inline&space;D(X)=\left\{x_{1},x_{2},...,x_{n}\right\}" /></a>，概率分布为<img src="http://latex.codecogs.com/svg.latex?\inline&space;P(X)=\left\{p(x_{1}),p(x_{2}),...,p(x_{n})\right\}" /></a>

随机变量<img src="http://latex.codecogs.com/svg.latex?\inline&space;X" /></a>可能取集合<img src="http://latex.codecogs.com/svg.latex?\inline&space;D(X)" /></a>中不同值，取值具有不确定性，概率分布<img src="http://latex.codecogs.com/svg.latex?\inline&space;P(X)" /></a>可以用来衡量随机变量不确定性的程度

<img src="http://latex.codecogs.com/svg.latex?\inline&space;P(X)" /></a>分布越均匀，<img src="http://latex.codecogs.com/svg.latex?\inline&space;X" /></a>取不同值(不确定值)的概率越大，不确定性越大；反之，<img src="http://latex.codecogs.com/svg.latex?\inline&space;P(X)" /></a>分布越不均匀，<img src="http://latex.codecogs.com/svg.latex?\inline&space;X" /></a>取确定值<img src="http://latex.codecogs.com/svg.latex?\left\{arg\&space;\underset{x_{k}}{top}\&space;p(x_{k})\right\}" /></a>的概率越大，不确定性越小

#### 信息熵(Entropy)

> 随机变量的不确定性，不确定性越大，熵越大

<div align="center"><img src="http://latex.codecogs.com/svg.latex?H(X)=-\sum_{i=1}^{n}p(x_{i})log_{2}p(x_{i})" /></a></div>

假设随机变量<img src="http://latex.codecogs.com/svg.latex?\inline&space;X\in\left\{x_{1},x_{2},...,x_{n}\right\}" /></a>

* <img src="http://latex.codecogs.com/svg.latex?\inline&space;max\&space;p(x_{i})" /></a>越接近1，随机变量的不确定性越小，熵越接近最小值0
* <img src="http://latex.codecogs.com/svg.latex?\inline&space;p(x_{1})=p(x_{2})=...=p(x_{n})=\frac{1}{n}" /></a>时，随机变量的不确定性最大，熵取最大值<img src="http://latex.codecogs.com/svg.latex?\inline&space;log_{2}n" /></a>

#### 条件熵

> 在一个条件下，随机变量的不确定性

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\inline&space;H(Y|X)=\sum_{i=1}^{n}p(x_{i})H(Y|X=x_{i})" /></a></div>

#### 信息增益(Information Gain)

> 在一个条件下，信息不确定性减少的程度，信息增益 = 信息熵 - 条件熵

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\inline&space;G(Y|X)=H(Y)-H(Y|X)" /></a></div>

#### 信息增益极大化

> <img src="http://latex.codecogs.com/svg.latex?\inline&space;H(Y)" /></a>固定，<img src="http://latex.codecogs.com/svg.latex?\inline&space;G(Y|X)" /></a>极大化 → <img src="http://latex.codecogs.com/svg.latex?\inline&space;H(Y|X)" /></a>极小化 → <img src="http://latex.codecogs.com/svg.latex?\inline&space;H(Y|X=x_{i})" /></a>极小化 → <img src="http://latex.codecogs.com/svg.latex?\inline&space;X=x_{i}" /></a>条件下<img src="http://latex.codecogs.com/svg.latex?\inline&space;Y" /></a>的不确定性小 → <img src="http://latex.codecogs.com/svg.latex?\inline&space;X=x_{i}" /></a>条件下<img src="http://latex.codecogs.com/svg.latex?\inline&space;Y" /></a>分布不均匀

最好的情况，<img src="http://latex.codecogs.com/svg.latex?\inline&space;Y\in\left\{c_{j}\right\},p(Y=c_{j}|X=x_{i})=1,H(Y|X=x_{i})=0" /></a>

最坏的情况，<img src="http://latex.codecogs.com/svg.latex?\inline&space;Y\in\left\{c_{1},c_{2},...,c_{n}\right\},p(Y=c_{j}|X=x_{i})=\frac{1}{n},H(Y|X=x_{i})=log_{2}n" /></a>

#### 决策树

1. 计算各个特征下Y的信息增益，取信息增益最大的特征来划分子集

2. 针对子集继续上述过程，直到子集为空或属于同一分类

#### 偏差(Bias)和方差(Variance)

#### 特征数

> 特征数越多，过拟合的可能性越大

#### 复杂度

> 特征数越多，复杂度越大
