'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
# tinput = input("Give me a string:")
# r = []
# for i in tinput:
#    r += tinput.split(i)
# # toutput = tinput.split()
# print(r)


# tinput = input("Give me a string:")
tinput = "hello world"
list_tinput = tinput.split()
for word in list_tinput:
    toutput = ()
    for char in word:
        toutput += tuple(char)
        for i in toutput:
            result = []
            result += i 
        print(result)



# tinput = input("Give me a string:")
# tinput = "hello world"
# list_tinput = list(tinput)
# tl1 = (tuple(list_tinput[0:5]))
# tl2 = (tuple(list_tinput[6:]))
# print(list_tinput)