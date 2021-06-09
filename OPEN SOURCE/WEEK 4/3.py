import numpy as np
user_input = input()
n=int(input("Enter Index:"))
count=0
for i in user_input:
    if(count==n):
        user_input=user_input[0:n]+user_input[n+1:]
    count=count+1
print(user_input)
