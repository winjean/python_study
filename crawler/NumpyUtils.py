import numpy as np

a = np.arange(12).reshape(3, 2, 2)
print(a)
print(a[0])

# 数组的维度
print(a.shape)

# 数组轴的个数，轴的个数被称作秩 =shape的长度
print(a.ndim)

# 数组中每个元素的字节大小
print(a.itemsize)

# 数组元素的总个数 =shape属性中元组元素的乘积
print(a.size)

