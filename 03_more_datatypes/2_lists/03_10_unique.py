'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
list_unique = []
for i in list_:
    if list_.count(i) < 2:
        list_unique.append(i)
print(list_unique)
