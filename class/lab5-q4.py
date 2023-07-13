# WAP to check if a string is rotation of another string (HELLO, ELLOH)

def isrotate(str1,str2,i,j):
    if i != j:
        return 0
    temp=str1+str1
    
    if (temp.count(str2)>0):
        return 1
    else :
        return 0

str1=input("Enter string 1 : ")
str2=input("Enter String 2 : ")
i=len(str1)
j=len(str2)

# temp=str1+str1
# t=temp.count(str2)

if isrotate(str1,str2,i,j):
    print("Strings are rotation of each other.")
else:
    print("Strings are not rotation of each other.")