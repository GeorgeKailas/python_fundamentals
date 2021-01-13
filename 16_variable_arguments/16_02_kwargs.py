'''
Write a script with a function that demonstrates the use of **kwargs.

'''
def exercises(**kwargs):
    for k, v in kwargs.items():
        print(f"I like to {k} because it keeps me fit, I can burn {v} calories in an hour")

exercises(run = 200, jump = 400, playbasketball = 550)
