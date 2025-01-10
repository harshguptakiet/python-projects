a=int(input("enter the first number:\n"))
b=int(input("enter the second number:\n"))
c=int(input("enter the third number:\n"))
def max(a,b,c):
    if a>b and a>c :
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
def min(a,b,c):
    if a<b and a<c :
        return a
    elif b<a and b<c:
        return b
    elif c<a and c<b:
        return c
print("the minimum value is:\n",min(a,b,c))
print("the maximum value is:\n",max(a,b,c))


  

