'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
# 1st try
num = 1
while num < 1001:
    if num % 5 == 0:
        print(num)
        num += 1
        continue
    else:
        num += 1



     