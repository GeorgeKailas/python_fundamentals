'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
in1 = ""

while isinstance(in1, int) is False:
    try: 
        in1 = int(input("give me a number please:"))
    except ValueError:
        print("You didn't enter a number try again")

print("You picked a number, good job") 
    
