'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
a = input("give me a word:")
b = input("give me another word:")
c = input("give me yet another word:")
print(a+",", str(len(a))+".",b+",", str(len(b))+".", c+",", str(len(c))+".")