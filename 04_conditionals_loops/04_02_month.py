'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
m = input("give me a month:")
if m == "January":
    print(1)
elif m == "February":
    print(2)
elif m == "March":
    print(3)
elif m == "April":
    print(4)
elif m == "May":
    print(5)
elif m == "June":
    print(6)
elif m == "July":
    print(7)
elif m == "August":
    print(8)
elif m == "September":
    print(9)
elif m == "October":
    print(10)
elif m == "November":
    print(11)
elif m == "December":
    print(12)
else:
    print("Not a month")