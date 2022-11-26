# How to use reduce ??
import functools

list_x = [1, 2, 3, 4, 5]
add_two_nums = lambda x, y: x + y

result = functools.reduce(add_two_nums, list_x)
# print(result)

###########################################################

multiply_two_nums = lambda x, y: x * y
result = functools.reduce(multiply_two_nums, list_x)
# print(result)

###########################################################

numbers = [2, 1, 3, 4, 7, 11, 18]
product = functools.reduce(lambda x, y: x * y, numbers)
# print(product)
