'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
gen = (x for x in range(1,1000000) if x % 1111 == 0 and x % 1111 != x)

for num in gen: 
    print(sorted(num))