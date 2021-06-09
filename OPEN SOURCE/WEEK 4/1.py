import numpy as np
input_user=(input())
list=input_user.split(",")
numpy_list=np.array(list)
all_freq={}
for i in numpy_list:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1

frequency_numpy=np.array(all_freq)
print(frequency_numpy)