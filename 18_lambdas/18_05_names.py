'''
You're about to have a baby and you don't have a name yet. 😱
You and your partner agree that it should start with an 'M', but that's
about all you've got so far.

To save the day, use the filter() method and a lambda expression
to map all the baby names that begin with a 'M' to an output list.

'''

names = ['Olivia', 'Noah', 'Ava', 'Oliver', 'Isabella', 'mason', 'Sophia', 'Logan', 'Emma', 'Liam', 'Amelia', 'Lucas', 'Mia', 'Elijah', 'Charlotte', 'Ethan', 'Harper', 'James', 'Mila', 'Aiden', 'Aria', 'Carter', 'Ella', 'Jackson', 'Evelyn', 'Alexander', 'Avery', 'Sebastian', 'Abigail', 'Michael', 'Emily', 'Benjamin', 'Luna', 'Jacob', 'Riley', 'William', 'Scarlett', 'Grayson', 'Chloe', 'Jack', 'Sofia', 'Daniel', 'Layla', 'Owen', 'Lily', 'Luke', 'Madison', 'Henry', 'Ellie', 'Wyatt', 'Zoey', 'Jayden', 'Elizabeth', 'Leo', 'Penelope', 'Gabriel', 'Victoria', 'Julian', 'Grace', 'Matthew', 'Nora', 'David', 'Aubrey', 'Jaxon', 'Camila', 'Levi', 'Hannah', 'Mateo', 'Bella', 'Asher', 'Aurora', 'Lincoln', 'Addison', 'John', 'Stella', 'Samuel', 'Skylar', 'Muhammad', 'Paisley', 'Ryan', 'Savannah', 'Adam', 'Maya', 'Isaac', 'Natalie', 'Nathan', 'Elena', 'Josiah', 'Emilia', 'Isaiah', 'Violet', 'Joseph', 'Hazel', 'Caleb', 'Nova', 'Anthony', 'Niamey', 'Hunter', 'Eva', 'Eli']

mnames = list(filter(lambda l: l[0].upper() == 'M', names))
#changed the m in mason to lowercase above to see if I could get it to work but i'm having trouble figuring out how to get it to capitalize the m in the output 
#tried an attempt below
print(mnames)

# cap_mnames = []
# for i in mnames:
#     cap_mnames.append().capitalize(i)
