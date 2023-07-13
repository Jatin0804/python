#create a function to find the distance between 3 coordinates and print the coordinates with least distance

def min_dist(x,y):
    d12=((x[2]-x[1])**2+(y[2]-y[1])**2)**(1/2)
    d13=((x[3]-x[1])**2+(y[3]-y[1])**2)**(1/2)
    d23=((x[3]-x[2])**2+(y[3]-y[2])**2)**(1/2)
    list=[d12,d23,d13]
    
    dict = {d12: {'C1', 'C2'}, d13: {'C1', 'C3'}, d23: {'C2', 'C3'}}
    for a in dict:
        print(dict[a], " : ",a)
    print("")

    m=min(list)
    print("The least distance between 2 coordinates is : ",m)
    return(dict[m])


x=[0,0,0,0]
y=[0,0,0,0]
print("Enter the values of x and y : ")
for i in range(1,4):
    x[i]=int(input(f'x[{i}] : '))
    y[i]=int(input(f'y[{i}] : '))
print(x)
print(y)

coord = {'C1': {x[1], y[1]}, 'C2': {x[2], y[2]}, 'C3': {x[3], y[3]}}
for a in coord:
    print(a, end=" : ")
    for b in coord[a]:
        print(b, end=' ')
    print("")
print("")

dict = {'d12': {'C1','C2'}, 'd13': {'C1','C3'}, 'd23': {'C2','C3'}}
for a in dict:
    print(a,end=" : ")
    for b in dict[a]:
        print(b,end=' ')
    print("")
print()

min=min_dist(x,y)
print("The least distance is of coordinates : ",min)
res=list(min)
for a in range(2):
    r=res[a]
    print("Point",a+1,":",coord[r])
