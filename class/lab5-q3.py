# WAP to check if a string is palindrome (reverse of string is same string)

str1=input("Enter a string : ")
str2=str1
if str1==str2[::-1]:
    print("Palindrome String.")
else:
    print("Not Palindrome String.")