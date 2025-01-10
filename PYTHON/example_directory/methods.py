class MathOperations:
    #instance method
    def add(self,x,y):
        return x+y
    
    #class method
    @classmethod
    def multiply(cls,x,y):
        return x*y
    
    #static mthod
    @staticmethod
    def subtract(x,y):
        return x-y
    
#creating an instance 
math_op = MathOperations()

#Using instance method
print(math_op.add(5,3))

#using class method
print(MathOperations.multiply(5,3))

#using static method
print(MathOperations.subtract(5,3))