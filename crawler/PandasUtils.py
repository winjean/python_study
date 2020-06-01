import pandas as pd
import numpy as np

a = np.arange(12).reshape(3, 4)
print(f"a:{a}\n")
c = ["a", "b", "c", "d"]
test = pd.DataFrame(columns=c, data=a)

print(f"len:{len(test)}\n")
print(f"sum:{test.sum()}\n")
print(f"head 2:{test.head(2)}\n")
print(f"describe:{test.describe()}\n")

# test.to_csv("d:/winjean.csv")
test.to_excel("d:/winjean.xls",sheet_name="winjean")


