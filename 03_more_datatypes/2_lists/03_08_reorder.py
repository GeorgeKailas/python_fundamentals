'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

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
print(l1[1],l1[3],l1[5],l1[7],l1[9])
print(l1[8],l1[6],l1[4],l1[2],l1[0])