'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
def sqr(num):
    return num ** 2
def rmdsq(num):
    return sqr(num) / 3
def rmdsqcu(num):
    return rmdsq(num) ** 3
print(rmdsqcu(3))

