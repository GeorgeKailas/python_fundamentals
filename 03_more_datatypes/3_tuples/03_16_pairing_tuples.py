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
# Working Start
input = 3,4,88,33,22,1,1000,23444,23,77
sinput = (sorted(input))
counter = 0
list_output = []
list_temp = []
for num in sinput:
    if len(sinput) % 2 ==0:
        if counter % 2 != 0 or counter ==0:
            list_temp.append(num)
            if  counter < len(sinput)-1:
                counter += 1
            else: 
                list_output.append(tuple(list_temp))
        else:
            list_output.append(tuple(list_temp))
            list_temp.append(num)
            del(list_temp[:2])
            if  counter < len(sinput)-1:
                counter += 1
            else: 
                list_output.append(tuple(list_temp))
    else:
        if counter % 2 != 0 or counter ==0:
            list_temp.append(num)
            if  counter < len(sinput)-1:
                counter += 1
            else: 
                list_output.append(tuple(list_temp))
        else:
            list_output.append(tuple(list_temp))
            list_temp.append(num)
            del(list_temp[:2])
            if  counter < len(sinput)-1:
                counter += 1
            else: 
                list_temp.append(0)
                list_output.append(tuple(list_temp))
print(list_output)

# Working Start
# input = 3,4,88,9,11,22,44,99
# sinput = (sorted(input))
# counter = 0
# list_output = []
# list_temp = []
# for num in sinput:
#     if counter % 2 != 0 or counter ==0:
#         list_temp.append(num)
#         counter += 1
#     else:
#         list_output.append(tuple(list_temp))
#         list_temp.append(num)
#         del(list_temp[:2])
#         counter +=1
# list_output.append(tuple(list_temp))
# print(list_output)

# list_output.append(toutput)
# print(list_toutput)
# toutput = ()