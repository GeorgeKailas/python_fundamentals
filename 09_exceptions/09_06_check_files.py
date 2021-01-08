'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

file_name = 'integers.txt'

'''

numlist = []

with open("integers.txt", 'r') as fin:
    for num in fin.readlines():
        num = num.rstrip()
        numlist.append(num)
try:
    print(int(numlist[0])/4)
except IOError:
    print("IOE bad")
except ValueError: 
    print("Value Error bad")


