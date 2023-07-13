#create a function to find the factorial of a number

def fact(num):
    # mul=1
    if num==0:
        return 1
    '''while(num>0):
        mul=mul*num
        num=num-1
    return mul'''
    return num*fact(num-1)

n=int(input("Enter a number : "))
print(fact(n))