# -*- coding: utf-8 -*-

import numpy as np

np.int(1.0)
np.int32(1.0)
np.int64(1.0)

np.float(1)
np.float32(1)
np.float64(1)

np.float32(np.array([1, 2, 3]))

np.dot(3, 4)
# 点积
np.dot([1, 2], [3, 4])
# 矩阵乘积
np.dot(np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3), np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2))
np.dot(np.array([1, 2, 3]).reshape(-1, 1), np.array([1, 2, 3]).reshape(1, -1))
