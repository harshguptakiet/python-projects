def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
       return x/y
    else:
        return "error:division by zero "
    
def calculator():
    print("SELECT OPERATION:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    
    choice = input("ENTER CHOICE(1/2/3/4):")

    if choice in ['1','2','3','4']:
       num1 = float(input("enter first number:"))
       num2 = float(input("enter second number:"))

       if choice == '1':
           print(f"{num1} + {num2} = {add(num1,num2)}")
       elif choice == '2':
           print(f"{num1} - {num2} = {subtract(num1,num2)}")
       elif choice =='3':
           print(f"{num1} * {num2} = {multiply(num1,num2)}")
       elif choice =='4':
           result = divide(num1,num2)
           print(f"{num1} / {num2} = {result}")
    else:
        print("invalid input")

if __name__ == "__main__":
   calculator()













    