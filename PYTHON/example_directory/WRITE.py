class Person:
    species = "Homo sapiens"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
person1 = Person("Alice",30)
print(person1.introduce())