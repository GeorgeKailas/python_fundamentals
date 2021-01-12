'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
gen = (x for x in range(1,1000000) if x % 1111 == 0 and x % 1111 != x)

for num in gen: 
    print(num // 1111)