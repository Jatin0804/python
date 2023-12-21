n=7
for i in range(n):
    for j in range(n):
        if j>=n-i:
            print("*",end= " ")
        else:
            print(end="  ")
    print()