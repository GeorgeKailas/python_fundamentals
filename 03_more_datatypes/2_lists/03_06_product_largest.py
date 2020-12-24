'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
n1 = int(input("Give me number:"))
n2 = int(input("Give me number:"))
n3 = int(input("Give me number:"))
n4 = int(input("Give me number:"))
n5 = int(input("Give me number:"))
n6 = int(input("Give me number:"))
n7 = int(input("Give me number:"))
n8 = int(input("Give me number:"))
n9 = int(input("Give me number:"))
n10 = int(input("Give me number:"))
l1 = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
m = max(l1)
print(m)