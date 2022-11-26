pass_two_nums = lambda x, y: x + y if x > y else x * y

x = 3
y = 12

# print(pass_two_nums(x, y))

###########################################################

# lambda_add_two_nums = lambda x, y: x + y
#
# a = 30
# b = 20
# print(lambda_add_two_nums(a, b))

lambda_max_three_nums = lambda x, y, z: x if (x > y and x > z) else (y if (y > x and y > z) else z)

num1 = 40
num2 = 10
num3 = 30
# print(lambda_max_three_nums(num1, num2, num3))

###########################################################

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubed = map(lambda x: pow(x, 3), list_1)
# print(list(cubed))

###########################################################

lambda_max_three_nums = lambda x, y, z: x if (x > y and x > z) else (y if (y > x and y > z) else z)

num1 = 40
num2 = 10
num3 = 30
# print(lambda_max_three_nums(num1, num2, num3))

###########################################################
