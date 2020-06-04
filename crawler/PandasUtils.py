#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# a = np.arange(12).reshape(3, 4)
# print(f"a:{a}\n")
# c = ["a", "b", "c", "d"]
# test = pd.DataFrame(columns=c, data=a)
#
# print(f"len:{len(test)}\n")
# print(f"sum:{test.sum()}\n")
# print(f"head 2:{test.head(2)}\n")
# print(f"describe:{test.describe()}\n")

# test.to_csv("d:/winjean.csv")
# test.to_excel("d:/winjean.xls", sheet_name="winjean")

# ************* pandas date  **************************

# print(pd.date_range('2020/06/03', periods=5))
# # bdate_range不包括周六和周日
# print(pd.bdate_range('2020/06/03', periods=5))
# print(pd.date_range('2020/06/03', periods=5, freq='M'))
#
#
# print(pd.Timedelta(6, unit='h'))
# print(pd.Timedelta(days=2))

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])

aaa = pd.DataFrame(dict(A=s, B=td))
# print(aaa.values)

aa = pd.Series(['a', 'b', 'c', 'd', 'e'])
aa = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[11, 22, 33, 66, 99])
aa = pd.Series({22: 'a', 66: 'b', 77: 'c', 11: 'd', 99: 'e'}, index=[11, 22, 33, 66, 99])
# aa = pd.Series(9, index=[11, 22, 33, 66, 99])
print(aa)
print(aa[11])
print(aa[-2:])
print(len(aa))

