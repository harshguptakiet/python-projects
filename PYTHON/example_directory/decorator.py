
def my_decorator(func):
    def wrapper():

        print("somethin is happening before the function is called.")
        func()
        print("something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()