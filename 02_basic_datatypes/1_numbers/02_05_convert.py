'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
a = 2
print (a*1.1)
b = 2.1
print (int(b)) 

print(b//a)

c = int(input("give me a number:"))
d = int(input("give me another number:"))
print(c*d)