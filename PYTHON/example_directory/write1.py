class Car:
    type = "vehicle"

    def __inti__(self,brand,model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota","Camry","1")
car2 = Car("Honda","Civic","2")

print(car1.type)
print(car1.brand)
print(car2.type)
print(car2.brand)
