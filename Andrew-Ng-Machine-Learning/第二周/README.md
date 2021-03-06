# 第二周

#### 安装Octave或MATLAB

#### 多维特征(Multiple Feature)

<div align="center"><img src="http://latex.codecogs.com/svg.latex?f(x)=b&plus;w_{1}x_{1}&plus;w_{2}x_{2}&plus;...&plus;w_{n}x_{n}" /></a></div>

令 <img src="http://latex.codecogs.com/svg.latex?\inline&space;w_{0}=b,x_{0}=1" /></a>

<div align="center"><img src="http://latex.codecogs.com/svg.latex?f(x)=w_{0}x_{0}&plus;w_{1}x_{1}&plus;...&plus;w_{n}x_{n}=\begin{bmatrix}&space;w_{0}&space;&&space;w_{1}&space;&&space;...&space;&&space;w_{n}&space;\end{bmatrix}&space;\begin{bmatrix}&space;x_{0}\\&space;x_{1}\\&space;...\\&space;x_{n}&space;\end{bmatrix}=w^{T}x" /></a></div>

其中

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\inline&space;\large&space;w=\begin{bmatrix}&space;w_{0}\\&space;w_{1}\\&space;...\\&space;w_{n}&space;\end{bmatrix},x=\begin{bmatrix}&space;x_{0}\\&space;x_{1}\\&space;...\\&space;x_{n}&space;\end{bmatrix}" /></a></div>

#### 多元线性回归

#### 多维特征下的梯度下降

#### 特征缩放(Feature Scaling)

> 确保特征在一个相似的数值范围内，提高算法的收敛速度

<div align="center"><img src="http://latex.codecogs.com/svg.latex?x_{i}=\frac{x_{i}}{max(x_{i})-min(x_{i})}" /></a></div>

#### 均值归一化(Mean Normalization)

> 使特征的均值为0，提高算法的收敛速度

<div align="center"><img src="http://latex.codecogs.com/svg.latex?x_{i}=x_{i}-\bar{x_{i}}" /></a></div>

特征缩放 + 均值归一化处理:

<div align="center"><img src="http://latex.codecogs.com/svg.latex?x_{i}=\frac{x_{i}-\bar{x_{i}}}{max(x_{i})-min(x_{i})}" /></a></div>

#### 梯度下降收敛

迭代次数 - 损失函数值 的散点图

> 迭代次数增加，损失函数值减小，否则，学习率偏大
> 迭代次数增加，损失函数值下降缓慢，学习率偏小

学习率: ...、0.001、0.01、0.1、1、...

#### 多项式线性回归(Polynomial Linear Regression)

同 多元线性回归

<div align="center"><img src="http://latex.codecogs.com/svg.latex?y=b&plus;w_{1}x&plus;w_{2}x^{2}&plus;w_{3}x^{3}" /></a></div>

#### 正规方程

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\theta=(XX^{T})^{-1}X^{T}y" /></a></div>
