'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''
# from collections import Counter

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict_c = {}

for key in dict_1:
    dict_c[key] = dict_1[key]
for key in dict_2:
    print(key)
    if key not in dict_c:
        dict_c[key] = dict_2[key]
    else:
        dict_c[key] += dict_2[key]
    print(dict_c, "this is dict_c")
    # print(key,  "this is key")
    # print(dict_1[key])

# dict_c = dict(Counter(dict_1)+Counter(dict_2))
# print(dict_c)







