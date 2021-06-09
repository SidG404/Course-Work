a=input()
b=input()

frequencies_a = {} 
frequencies_b = {} 
  
for char in a: 
   if char in frequencies_a: 
      frequencies_a[char] += 1
   else: 
      frequencies_a[char] = 1

  
for char in b: 
   if char in frequencies_b: 
      frequencies_b[char] += 1
   else: 
      frequencies_b[char] = 1

if(frequencies_a==frequencies_b):
    print("Anagram")
else:
    print("Not Anagram")