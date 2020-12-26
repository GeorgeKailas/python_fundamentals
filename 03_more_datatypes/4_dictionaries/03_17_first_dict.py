'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

r= range(1,11)
r_s = set(r)
new_dict = {}
for i in r_s:
    new_dict.update({i:i*i})
print(new_dict)