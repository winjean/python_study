import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_excel("d:/winjean.xls", sheet_name=0, header=None)
data = pd.read_excel("d:/winjean.xls", sheet_name=0, header=0, index_col=0)
mm = data.sum()

print(f"data :\n{data}")
print(f"\nmm:\n{mm}")

plt.rc('font', family='SimHei', size=13)
N = 4
# 3个用户 0 1 2
ind = np.arange(N)  # the x locations for the groups
print(f"\nind:\n{ind}")
# 设置宽度
width = 0.35
x = [u'用户A', u'用户B', u'用户C', u'用户D']
# 绘图
plt.bar(ind, mm, width, color='g', label='sum num')
plt.xlabel(u"用户名")
plt.ylabel(u"总耗电量")
plt.title(u'电力窃漏电用户自动识别--总耗电量')
plt.legend()
# 设置底部名称
# 旋转40度
plt.xticks(ind+width/2, x, rotation=40)
plt.show()

