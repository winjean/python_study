import numpy as np

a = np.arange(12).reshape(3, 2, 2)
print(f"a = {a}\n")

print(f"a[0] = {a[0]}\n")

# 数组的维度
print(f"shape = {a.shape}\n")

# 数组轴的个数，轴的个数被称作秩 =shape的长度
print(f"ndim = {a.ndim}\n")

# 数组中每个元素的字节大小
print(f"itemsize = {a.itemsize}\n")

# 数组元素的总个数 =shape属性中元组元素的乘积
print(f"size = {a.size}\n")

print(f"min = {a.min()}\n")
print(f"max = {a.max()}\n")


