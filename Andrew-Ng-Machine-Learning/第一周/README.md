# 第一周

#### 机器学习定义

> A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.

#### 机器学习算法

* 监督学习(Supervised Learning): 提供输入和输出
* 无监督学习(Unsupervised Learning): 只提供输入
* 强化学习(Reinforcement Learning)
* 推荐系统(Recommender System)

#### 监督学习

* 回归(Regression): 输出连续值
* 分类(Classification): 输出离散值

#### 无监督学习

* 聚类(Clustering)

#### 机器学习术语

* Training Set: 训练集
* Learning Algorithm: 学习算法
* Cost Function: 损失函数
* Learning Rate: 学习率

#### 线性回归(Linear Regression)

* 一元线性回归
* 多元线性回归

#### 平方误差(Square Error)

#### 梯度下降(Gradient Descent)

* Local Minimum: 局部最小值
* Global Minimum: 全局最小值

#### 矩阵(Matrix)

2 x 3 矩阵: 2行3列

<div align="center"><img src="http://latex.codecogs.com/svg.latex?M&space;=&space;\begin{bmatrix}&space;1&space;&&space;2&space;&&space;3&space;\\&space;4&space;&&space;5&space;&&space;6&space;\end{bmatrix}" /></a></div>

#### 向量(Vector)

向量 = n x 1 矩阵

<div align="center"><img src="http://latex.codecogs.com/svg.latex?v&space;=&space;\begin{bmatrix}&space;1&space;\\&space;2&space;\\&space;3&space;\end{bmatrix}" /></a></div>

#### 矩阵加法

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\begin{bmatrix}&space;1&space;&&&space;2\\&space;3&space;&&&space;4&space;\end{bmatrix}&plus;\begin{bmatrix}&space;1&space;&&&space;2\\&space;3&space;&&&space;4&space;\end{bmatrix}=\begin{bmatrix}&space;2&space;&&&space;4\\&space;6&space;&&&space;8&space;\end{bmatrix}" /></a></div>

#### 矩阵和标量乘法

<div align="center"><img src="http://latex.codecogs.com/svg.latex?3&space;\ast&space;\begin{bmatrix}&space;1\\&space;2\\&space;3&space;\end{bmatrix}=\begin{bmatrix}&space;3\\&space;6\\&space;9&space;\end{bmatrix}" /></a></div>

#### 矩阵和向量乘法

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\begin{bmatrix}&space;1&space;&&&space;2\\&space;3&space;&&&space;4&space;\end{bmatrix}\begin{bmatrix}&space;1\\&space;2&space;\end{bmatrix}=\begin{bmatrix}&space;5\\&space;11&space;\end{bmatrix}" /></a></div>

#### 矩阵和矩阵乘法

[m x n][n x k] = [m x k]

矩阵一的第i行 * 矩阵二的第j列 = 结果矩阵的第i行第j列

<div align="center"><img src="http://latex.codecogs.com/svg.latex?\begin{bmatrix}&space;1&space;&&&space;2&space;&&&space;3\\&space;4&space;&&&space;5&space;&&&space;6&space;\end{bmatrix}\begin{bmatrix}&space;1&space;&&&space;2\\&space;3&space;&&&space;4\\&space;5&space;&&&space;6&space;\end{bmatrix}=\begin{bmatrix}&space;22&space;&&&space;28\\&space;49&space;&&&space;64&space;\end{bmatrix}" /></a></div>

```A x B != B x A```
