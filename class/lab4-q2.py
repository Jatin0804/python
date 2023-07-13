# generate a sequence of n values in range(1,10) and find the value with maximum frequency

import numpy
import random

freq=0
count=0
max=0
a = numpy.zeros((10, 2))
list=[]
n=int(input("Enter a value of n : "))
#to create a list of random numbers
for i in range(0,n):
    x=random.randint(1,10)
    list.append(x)

#to initialize array in ascending order
for i in range(1,11):
    a[i-1][0]=i

#to count the frequency of all numbers
for i in range(0,n):
    num=list[i]
    count=a[num-1][1]
    count+=1
    a[num-1][1]=count

#to calculate maximum frequency
for i in range(1,11):
    if(freq < a[i-1][1]):
        freq = int(a[i-1][1])
        max = int(a[i-1][0])

print("Sequence is : ",list)
print("Number and their respective frequencies : \n",a)
print("Maximum frequency : ",freq)
print("Maximum frequency value : ",max)