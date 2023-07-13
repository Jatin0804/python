str="String "
str1="Concatenation"

con=str+str1
print(con)

print(str[0])
print(str[0:5])
print(str1[-1])  #last index
print(str[:4])  # same as str[0:4]
print(str1[-4:-1])  #from -4 to -2 (exclude -1)
print(con[::2])   #skip value of 2

print(len(con))  # length of string
print(con.endswith("ary"))
print(con.endswith("ion"))
print(con.count("on")) #count on occurence

print(con.capitalize()) #capitalize first letter
print(con.find("in")) #gives index
print(con.replace("on","replace"))
print(con)

esc="new line.\n and tab spaces \tare here"
print(esc)