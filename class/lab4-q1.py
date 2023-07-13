#generate a sequence of n values in range(1,100) and find the sum of even valued terms

import random

sum=0
list=[]
n=int(input("Enter a value of n : "))
for i in range(1,n+1):
    x=random.randint(1,100)
    list.append(x)
    if(x%2==0):
        sum=sum+list[i-1]

print("\nSequence : ",list)
print("\nSum : ",sum)