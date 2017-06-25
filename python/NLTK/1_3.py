#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
                'Uniformity of Cell Shape', 'Marginal Adhesion',
                'Single Epithelial Cell Size', 'Bare Nuclei',
                'Bland Chromation', 'Normal Nucleoli', 'Mitoses', 'Class']

data = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',
        names=column_names)
data = data.replace(to_replace='? ', value=np.nan)
data = data.dropna(how='any')

from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(data[column_names[1:10]], data[column_names[10]], test_size=0.25,
                                                    random_state=33)
