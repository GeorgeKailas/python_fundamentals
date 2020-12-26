'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

# s = input("write a sentence:")
# s_s = s.split()
# higest_count_word = ""
# count_word_dict = {}
# for i in s_s:
#     if s_s.count(i) == max(s_s.count(i)):
#         higest_count_word += i
# print(higest_count_word)

s = input("write a sentence:")
s_s = s.split()
count_word_dict = {}
for i in s_s:
    count_word_dict[i] = s_s.count(i)
v = list(count_word_dict.values())
k = list(count_word_dict.keys())
print(k[v.index(max(v))])


