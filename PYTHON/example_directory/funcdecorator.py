def my_decorator(func):
    def wrapper(*args,**kwargs):

        print("function is called with argument",args,kwargs)
        result = func(*args,**kwargs)
        print("function call complete")
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a+b

print(add(5,3))