'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!

'''
import operator
d = {"item1": 5, "item2": 6, "item3": 1}
l = list(d.items()) 
nl = sorted(l, key=operator.itemgetter(1))
print(nl)



# l = {"item1": 5, "item2": 6, "item3": 1}
# l1 = []
# l1.append(l)
# vals = []
# for d in l1:
#     vals.extend(d.values())
# print(tuple(vals))