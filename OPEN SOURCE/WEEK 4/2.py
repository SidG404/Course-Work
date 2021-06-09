import numpy as np
user_input=int(input())
n=user_input
list=[]
while(n!=0):
    m=n%10
    n=n/10
    list.append(m)
list.reverse()
numpy_array=np.array(list)
numpy_array.sort()
numpy_array=numpy_array[::-1]
print(numpy_array)


