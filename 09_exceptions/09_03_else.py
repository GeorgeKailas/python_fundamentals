'''
Write a script that demonstrates a try/except/else.

'''

try:
    dividend = int(input("Please enter the number to be divided: "))
    divisor = int(input("Please enter the divisor: "))
    result = dividend / divisor
    print(f"The result of {dividend} divided by {divisor} is {result}")
except ZeroDivisionError as zde:
    print("There was an error with the message: ", zde)
else:
    print("You did it!")
