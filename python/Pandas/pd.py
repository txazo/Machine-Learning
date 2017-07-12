# -*- coding: utf-8 -*-

import pandas as pd

# -------------------- pd.Series --------------------

pd.Series(['Joke', 'Kite', 'Marry'], index=['100', '101', '102'], dtype=np.object)

# -------------------- pd.DataFrame --------------------
df = pd.DataFrame([['Joke', 'male', 18], ['Kite', 'female', 25], ['Marry', 'female', 25]], index=['100', '101', '102'],
                  columns=['Name', 'Sex', 'Age'],
                  dtype=np.object)

# 行切片访问: df[1:2]
# 行名称访问: df.loc['100'] df.loc[['100', '102']]
# 列名称访问: df.Sex df['Name'] df[['Name', 'Sex']]
# 组合访问: df[1:][['Name', 'Sex']] df[['Name', 'Sex']][1:] df.loc['101'][['Name', 'Sex']]
# df.loc[:, ['Name', 'Sex']]
# df.loc[['100', '102'], ['Name', 'Sex']]
# df.loc['100':'102', ['Name', 'Sex']]
# df.loc['100', 'Name']
# df.iloc[0:2, 0:2]

# DataFrame.index       行名称
# DataFrame.columns     列名称
# DataFrame.values      值(numpy.ndarray)
# DataFrame.T           转置

# DataFrame.head(5)     头部
# DataFrame.tail(10)    尾部

# DataFrame.info()      概要信息
# DataFrame.describe()  统计性信息
# count 计数
# mean 平均值
# std 标准偏差
# min 最小值
# max 最大值

# DataFrame.sort_index(axis=1)    按轴排序
# DataFrame.sort_values(by='')   按值排序
