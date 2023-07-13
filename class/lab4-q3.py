# generate a sequence of n values in range(1,100) and separate odd and even values in 2 separate list

import random

list1=[]
list2=[]
n=int(input("Enter a value of n : "))
for i in range(1,n+1):
    x=random.randint(1,100)
    if(x%2==0):
        list1.append(x)
    else:
        list2.append(x)

print("List of even values : ",list1)
print("List of odd values : ",list2)