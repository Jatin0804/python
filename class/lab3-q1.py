#To compute distance between 2 coordinates (x1,y1) and (x2,y2)
import math

x1=int(input("Enter value of x1 : "))
y1=int(input("Enter value of y1 : "))
x2=int(input("Enter value of x2 : "))
y2=int(input("Enter value of y2 : "))

dist=math.sqrt((((x2-x1)**2)+((y2-y1)**2)))
print(dist)