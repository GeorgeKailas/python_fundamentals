'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
class Car:
    def __init__(self, model, year, max_speed = 0, state = 'working'):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.state = state
    
    def accelerate(self):
        self.max_speed += 5
    
    def __str__(self):
        return f"{self.model} is from {self.year} and has goes as fast as {self.max_speed} and it is {self.state}"
    
    def crashed(self):
        print(f"you crashed your {self.model}")
        self.state = "broken"

    def fixed(self):
        print(f"you fixed up your {self.model}")
        self.state = "repaired"

c1 = Car('Toyota Rav 4', 2010, 50, 'working')
print(c1)
c1.crashed()
print(c1)
c1.fixed()
print(c1)
c2 = Car('Clunker', 1980, 3, "broken")
print(c2)

