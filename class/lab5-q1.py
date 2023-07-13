# WAP to find if 2 strings are anagrams, (have same set of characters)(xyz,yzx)

str1=input("Enter 1st string : ")
str2=input("ENter 2nd string : ")
'''
str3=""
flag=0
count=0
for i in str1:
    for j in str2:
        if i==j:
            count=count+1
'''
if(sorted(str1)==sorted(str2)):
    print("Anagram strings.")
else:
    print("Strings not Anagram.")