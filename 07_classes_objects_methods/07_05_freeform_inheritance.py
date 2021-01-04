'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

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

class nfl(sports_teams):
    def __init__(self, city, name, titles = 0, ready = 'no', players = 52):
        super().__init__(city, name, titles = 0)
        self.ready = ready
        self.players = players
    def __str__(self):
        if self.ready.lower() == 'yes':
            return f"The {self.name} are from {self.city} and have won {self.titles} titles and {self.players} {self.name} players are ready for some football!!"
        else:
            return f"The {self.name} are from {self.city} and have won {self.titles} titles and are not ready for some football"
    def injury(self, num):
        print(f"{num} are injured, ouch! watch out")
        self.players -= num
n1 = nfl('LA', 'Rams', 7, 'yes', 47)
print(n1)
n1.championship()
n1.injury(8)
print(n1)

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

class petting(zoo):
    def __init__(self, animals, status, zookeepers = 1, dangerous = 'no'):
        super().__init__(animals, status, zookeepers = 1)
        self.dangerous = dangerous
    
    def __str__(self):
        if self.status.lower() == 'open':
            return f"The {self.animals} can be seen at the {self.status} petting zoo with {self.zookeepers} zookeepers"
        elif self.status.lower() == 'closed':
            if self.dangerous.lower() == 'yes':
                return f"The {self.animals} are dangerous!! Stay away"
            else:
                return f"The {self.animals} cannot be seen at the {self.status} petting zoo with {self.zookeepers} zookeepers"
        else:
            return f"Maybe you can see the {self.animals} at the petting zoo with {self.zookeepers} zookeepers"

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

p1 = petting(['sheep', 'cow', 'pig'], 'closed', 3, 'yes')
print(p1)
p2 = petting(['sheep', 'cow'], 'closed', 3, 'no')
print(p2)
p2 = p2 + 'yeti'
print(p2)