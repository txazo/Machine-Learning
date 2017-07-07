# TensorFlow

#### TensorFlow结构

* 会话(Session):
* 图(Graph):
* 节点(Node): Operation
* 线(Edge): Tensor
* 变量(Variable)

#### 张量(Tensor)

Tensor，代表Operation的输入和输出

* 0阶张量: 常量, 1
* 1阶张量: 向量, [1, 2, 3, 4, 5, 6]
* 2阶张量: 矩阵, [[1, 2, 3], [4, 5, 6]]
* 3阶张量: 3纬向量, [[[1], [2], [3]], [[4], [5], [6]]]

#### TensorBoard

```
python3 $PYTHON3_HOME/lib/python3.6/site-packages/tensorflow/tensorboard/tensorboard.py --logdir=/tmp/tensorboard
```

```
tensorboard --logdir=/tmp/tensorboard
```

[http://127.0.0.1:6006](http://127.0.0.1:6006)
