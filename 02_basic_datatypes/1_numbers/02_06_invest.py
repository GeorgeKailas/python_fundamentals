'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
P = int(input("Amount to invest?"))
r = int(input("Return rate?"))
t = int(input("Years?"))
print(P*(1+r)**t)