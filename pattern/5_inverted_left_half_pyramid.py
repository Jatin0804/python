n=10

for i in range(n):
    for j in range(n):
        if i>j:
            print(end="  ")
        else:
            print("*",end=" ")

    print()