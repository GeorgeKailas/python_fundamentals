'''
Print out every prime number between 1 and 100.

'''
# listi = []
# for i in range(0,101):
#     if i % 2 == 0:
#         listi.append(i)
# print(listi)

listi = []
for num in range(0,101):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           listi.append(num)
print(listi)