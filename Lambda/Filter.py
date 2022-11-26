# How to use filter ()

# Create list of only odd elements
seq = [1, 2, 5, 6, 9, 7, 10]

filter_odd = lambda x: x % 2 != 0

result = list(filter(filter_odd, seq))
# print(result)

###########################################################

filter_even = lambda x: x % 2 == 0

result = list(filter(filter_even, seq))
# print(result)

###########################################################
