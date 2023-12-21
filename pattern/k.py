n=10
for i in range(n):
    for j in range(n):
        if j==0:
            print("|",end="")
        if j==n-i:
            print("/",end=" ")
        else:
            print(end="  ")
    print()

for i in range(n):
    for j in range(n):
        if j==0:
            print("|",end="")
        if i==j:
            print("\\",end=" ")
        else:
            print(end="  ")
    print()