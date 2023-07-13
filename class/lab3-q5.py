import math
#Print sum of all Prime number below 2 million(1 million=10^6)

'''sum=1
prime=0
for i in range(2,10):
    prime=0
    for j in range(2,i-1):
        if i%j==0:
            prime=1
    if prime==0:
        #print(i)
        sum=sum+i

print("Sum : ",sum)
'''
def primen(n):
    sum=1
    prime=[True for i in range(n+1)]
    p=2

    while(p*p<=n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    c=0

    for p in range(2,n):
        if prime[p]:
            sum+=p

    print(sum)

primen(2000000)