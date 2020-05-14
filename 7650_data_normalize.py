import numpy as np
from sklearn import preprocessing 

# input data
data = [100, 400, 600,800, 3000, 4200]
arr = np.array(data)


print('\n ========= min-max ===========\n')
# default: min = 0, max = 1
min, max = 0, 100
for x in arr:
  x = float(x - np.min(arr))/(np.max(arr)- np.min(arr))
  print(x *(max - min)+ min)

print('\n\n\n ========= Z-score ===========\n')
print('mean:', arr.mean(),'      std:', arr.std())
for x in arr:
  x = float(x - arr.mean())/arr.std()
  print(x)


print('\n\n\n ========= decimal scaling ===========\n')