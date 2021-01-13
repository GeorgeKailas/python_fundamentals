'''
Write a script with a function that demonstrates the use of *args.

'''

def exercises(*args):
    for a in args:
        print(f"I like to {a} because it keeps me fit")

exercises('run', 'jump', 'play basketball')
