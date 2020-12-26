'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
s = input("write a sentence:")
char_s = list(s)
count_word_dict = {}
for i in char_s:
    count_word_dict[i] = char_s.count(i)
print(count_word_dict)

# s = input("write a sentence:")
# s_s = s.split()
# count_word_dict = {}
# for i in s_s:
#     count_word_dict[i] = s_s.count(i)
# print(count_word_dict)