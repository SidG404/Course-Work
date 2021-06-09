import numpy as np
arr1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",arr1)
arr2 = [10, 30, 40, 50, 70]
print("Array2:" ,arr2)
for i in arr1:
  print(i," is present")
else:
  print(i, " is not present")
print(np.in1d(arr1, arr2))