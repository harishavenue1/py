# How to work with map() , filter(), reduce()

# implement map function
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Result
# result = [1,4,9,16,25,36,49,64,81]

square_num = lambda x: x * 2
# print(square_num(11))
square_list = list(map(square_num, list1))
# print(square_list)

###########################################################

# Add sequential respective elements in two given lists
list_a = [1, 2, 3, 4, 5]
list_b = [5, 4, 3, 2, 1]

# result = [6, 6, 6, 6, 6]
sum_two_elements = lambda x, y: x + y
result = list(map(sum_two_elements, list_a, list_b))
# print(result)
###########################################################
