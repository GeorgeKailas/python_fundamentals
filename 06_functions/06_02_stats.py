'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(l):
  return max(l), min(l), sum(l)/len(l), sum(l)

# call the function below here
print(stats(example_list))



# def stats(l):
#   # define the function here
#   print(max(l))
#   print(min(l))
#   print(sum(l)/len(l))
#   print(sum(l))

# # call the function below here
# stats(example_list)

