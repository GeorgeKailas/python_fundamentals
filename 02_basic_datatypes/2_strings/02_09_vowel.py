'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

#\iffalse
#a = input("Write a sentence:")
#count = 0
#for i in a:
 #   if i == 'a':
  #      elif i == 'e':
   #         elif i == 'i':
    #            elif i == 'u':
     #               count = count + 1
#print(count)
#\if lowercase? 

t_str = input("Write a sentence:")
counter1 = t_str.count('e')
counter2 = t_str.count('a')
counter3 = t_str.count('i')
counter4 = t_str.count ('o')
counter5 = t_str.count('u')
print(counter1+counter2+counter3+counter4+counter5)