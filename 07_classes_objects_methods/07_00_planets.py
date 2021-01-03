'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self, name, size, system):
        self.name = name
        self.size = size 
        self.system = system
    def __str__ (self):
        return f"Planet {self.name} is {self.size} and is located in {self.system}"
E = Planet('Earth', 5000, 'Milky Way')
print(E)
print(E.size)