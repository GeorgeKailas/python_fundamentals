'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
class rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self.length + 2*self.width
    def __str__(self):
        return f"My rectangle has a length of {self.length} and a width of {self.width} which gives it an area of {self.area()}"

class circle:
    def __init__ (self, radius):
        self.radius = radius
    def circumference(self):
        return self.radius * 3.14 * 2


r1 = rectangle(3, 6)
print(r1.area())
print(r1.perimeter())
print(r1)

r2 = rectangle(10, 11)
r2.area()
r2.perimeter()
print(r2)

c1 = circle(5)
print(c1.circumference())