'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''
nl = [1,2,6,7,8,9,11]

gen1 = (x for x in tuple(nl))

print(sum(gen1))