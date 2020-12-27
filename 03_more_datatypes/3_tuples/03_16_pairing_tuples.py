'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

input = 3,4,88,9,11,22,44,99
sinput = (sorted(input))
counter = 0
list_toutput = []
for num in sinput:
    toutput = ()
    if counter % 2 != 0:
        toutput += tuple(num)
        counter += 1
    else:
        counter +=1
list_output.append(toutput)
print(list_toutput)
