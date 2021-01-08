'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
words = []

for line in reversed(list(open("words.txt"))):
    words.append(line)
    
with open("words_reverse.txt", "w") as fout:
    fout.write("\n".join(words))    