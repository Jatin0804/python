# WAp to remove all vowels from a string and add them to a list

str1=input("Enter a string : ")
vowels="aeiouAEIOU"
str2=""
list=[]
for i in str1:
    if i in vowels:
        list.append(i)
    else:
        str2=str2+i
print("String without vowels : ",str2)
print("List of vowels used : ",list)