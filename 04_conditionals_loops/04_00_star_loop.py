'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

inp = input("give me a number:")
n = int(inp)
nr = range(1,n+1)
nl = list(nr)

for i in nl:
    print(i*"*")

