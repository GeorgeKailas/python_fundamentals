'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
def longest_word(file):
    with open(file, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word("words.txt"))

def shortest_word(file):
    with open(file, 'r') as infile:
        words = infile.read().split()
    min_len = len(min(words, key=len))
    return [word for word in words if len(word) == min_len]
print(shortest_word("words.txt"))

def count(file):
    with open(file, 'r') as infile:
        words = infile.read().split()
    return len(words)
print(count("words.txt"))

# with open("words.txt", 'r') as fin:
#     for word in fin.readlines():
#         if len(word) == max(len(word)):
#             print(word)
#         if len(word) == min(len(word)):
#             print(word)
        