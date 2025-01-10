def example_function(*args, **kwargs):
    print("Arguments (args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword Arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(1, 2, 3, name="Alice", age=30, city="New York")
