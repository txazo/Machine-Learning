# 感知机(Perceptron)

输入: <img src="http://latex.codecogs.com/svg.latex?\inline&space;\dpi{120}&space;\bg_white&space;\large&space;x&space;=&space;[x_{1},x_{2},...,x_{n}]" />

<div align=center><img src="http://latex.codecogs.com/svg.latex?\dpi{120}&space;\bg_white&space;\large&space;f(x)=sign(w\cdot&space;x&plus;b)" /></div>

<div align=center><img src="http://latex.codecogs.com/svg.latex?\dpi{120}&space;\bg_white&space;\large&space;sign(x)=\left\{\begin{matrix}1&x>=0\\-1&x<0\end{matrix}" /></div>

M为误分类的集合:

<div align=center><img src="http://latex.codecogs.com/svg.latex?\dpi{120}&space;\large&space;L(w,b)=-\sum_{x_{i}\in&space;M}y_{i}(w\cdot&space;x_{i}&plus;b))" /></div>
