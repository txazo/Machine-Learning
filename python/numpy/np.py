# -*- coding: utf-8 -*-

import numpy as np

# np.float32
np.float32('1')  # numpy.float32
np.float32(['1', '2', '3'])  # numpy.ndarray

# np.random.rand
np.random.rand(2, 3, 4)  # numpy.ndarray

# np.dot 两个数组的点积
np.dot(3, 4)  # numpy.int64
np.dot([1, 2], [3, 4])  # numpy.int64
np.dot([[1, 2], [3, 4], [5, 6]], [[1, 2, 3], [4, 5, 6]])  # numpy.ndarray
