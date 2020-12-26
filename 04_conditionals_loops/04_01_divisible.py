'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

n = int(input("Give me a number:"))
if n%3 == 0:
    print("divisible by 3")
else:
    print("not divisible by 3")