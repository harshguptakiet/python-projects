import math
a=float(input("ENTER THE LENGTH OF FIRST SIDE:\n"))
b=float(input("ENTER THE LENGTH OF SECOND SIDE:\n"))
c=float(input("ENTER THE LENGTH OF THIRD SIDE:\n"))
s=((a+b+c)/2)
area = (math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("the area of triangle is :",float(area))