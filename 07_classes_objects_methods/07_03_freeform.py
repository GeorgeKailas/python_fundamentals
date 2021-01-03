'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class sports_teams:
    def __init__(self, city, name, titles = 0):
        self.city = city
        self.name = name
        self.titles = titles
    def __str__(self):
        return f"The {self.name} are from {self.city} and have won {self.titles} titles"
    def championship(self):
        print(f"The {self.name} have won the championship!!")
        self.titles += 1
t1 = sports_teams('LA', 'Rams', 3)
print(t1)
t1.championship()
print(t1)

# class zoo:
#     def __init__(self, animals, status, zookeepers = 1):
#         self.animals = list(animals)
#         self.status - status
#         self.zookeepers = zookeepers + len(self.animals) / 2
# z1 = zoo(['lion', 'tiger','bear'], 'open',2)
# print(z1)

class zoo:
    def __init__(self, animals, status, zookeepers = 1):
        self.animals = list(animals)
        self.status = status
        self.zookeepers = zookeepers + len(self.animals) / 2
    def __str__(self):
        if self.status.lower() == 'open':
            return f"The {self.animals} can be seen at the {self.status} zoo with {self.zookeepers} zookeepers"
        elif self.status.lower() == 'closed':
            return f"The {self.animals} cannot be seen at the {self.status} zoo with {self.zookeepers} zookeepers"
        else:
            return f"Maybe you can see the {self.animals} at the zoo with {self.zookeepers} zookeepers"
    def __add__(self, other):
        new_animals = self.animals.copy()
        new_animals.append(other)
        return zoo(new_animals,self.status,self.zookeepers)

z1 = zoo(['lion', 'tiger','bear'], 'OPEN',2)
print(z1)
z2 = zoo(['lion', 'tiger','bear', 'snake'], 'clOsed',5)
print(z2)
z3 = zoo(['goat'], 'goat')
print(z3)
z3.zookeepers = 7
print(z3)
z1 = z1 + 'yeti'
print(z1)