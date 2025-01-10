class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return"some generic sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} mews!"
    
dog1 = Dog("Bruno")
print(dog1.speak())

cat1 = Cat("Kitty")
print(cat1.speak())

