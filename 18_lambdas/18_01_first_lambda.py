'''
Write a lambda function that takes in 3 numbers and returns the sum of the numbers.

'''
# from functools import reduce

# l1 = [1,2,3]

# sum = reduce((lambda x,y,z: x+y+z), l1)

# print(sum)

l1 = [1,2,3]

sum = lambda x: x[0]+x[1]+x[2]
print(sum(l1))