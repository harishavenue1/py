### Assignment Part-1
# Q1. Why do we call Python as a general purpose and high-level programming language?
#       Python is very versatile and its best chosen for wide variety of solutions.
#       It's written in closer to human-readable language, which then interpreter runs through code line by line,
#       translating to machine-readable.
#
# Q2. Why is Python called a dynamically typed language?
#       Due to power to assign the type of the variable used during runtime, instead of specifying while writing the code.
#
# Q3. List some pros and cons of Python programming language?
#       Pros: Easy to learn, faster to code, free & open source, best chosen for wide variety of solution.
#       Cons: Line by Line execution making it slower, runtime errors, not chosen for mobile computing due to poor memory handling.
#
# Q4. In what all domains can we use Python?
#       Data Science, Artificial Intelligence, Machine Learning, Deep Learning
#
# Q5. What are variable and how can we declare them?
#       Variable in python is memory location on which a data can be stored.
#       Declaration is as follows, count = 0
#
# Q6. How can we take an input from the user in Python?
#       Using input function as follows, s1 = input("Enter any values :")
#
# Q7. What is the default datatype of the value that has been taken as an input using input() function?
#       String
#
# Q8. What is type casting?
#       Converting one type of data into another, ex: String to int, like count = int(input("Enter any values :"))
#
# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
#       Yes, by providing space between inputs.
#       s1 = input("Enter any values :")
#       Ex: 1 2 3
#       print(s1) -> 1 2 3
#
# Q10. What are keywords?
#       Keywords are built-in python for special purpose, ex: for, int, lambda, list, etc,.
#
# Q11. Can we use keywords as a variable? Support your answer with reason.
#       No, it will be treated syntax errors, as they already have special built-in purpose.
#
# Q12. What is indentation? What's the use of indentation in Python?
#       Indentation is the spaces written at the beginning of the code, it increases readability.
#       Python use a indentation to specify a block of code.
#
# Q13. How can we throw some output in Python?
#       Using print method, ex: print(1)
#
# Q14. What are operators in Python?
#       Operators are special symbols that perform computation on the input data.
#
# Q15. What is difference between / and // operators?
#       '/' symbol does division and provides decimal output.
#       '//' symbol also does division but provides integer output.
#
# Q16. Write a code that gives following as an output.
# ```
# iNeuroniNeuroniNeuroniNeuron
# ```
# str = 'iNeuron'
# print(str * 4)
#
# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
# num = int(input('enter a number:'))
# if num % 2 == 0:
#     print('even')
# else:
#     print('odd')
#
# Q18. What are boolean operator?
#       Operators which returns value as True or False are boolean operators, ex: AND, OR, NOT
#
# Q19. What will the output of the following?
# ```
# 1 or 0 -> True
#
# 0 and 0 -> False
#
# True and False and True -> False
#
# 1 or 0 or 0 -> True
# ```
#
# Q20. What are conditional statements in Python?
#       Statements which has If and else makes it Conditional.
#
# Q21. What is use of 'if', 'elif' and 'else' keywords?
#       If 'if' statement is satisfied then perform an action,
#       else if 'elif' statement is satisfied do an action,
#       else if none of the actions are satisfied, do final action using 'else'.
#
# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
# age = int(input('enter the age fo the person: '))
# if age >= 18:
#     print('I can vote')
# else:
#     print("I can't vote")
#
# Q23. Write a code that displays the sum of all the even numbers from the given list.
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# sum = 0
# for num in numbers:
#     if num % 2 == 0:
#         sum += num
# print(sum)
#
# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
#
# n1, n2, n3 = list(map(int, input('enter 3 numbers: ').split(",")))
# if n1 > n2 and n1 > n3:
#     print("max is", n1)
# elif n2 > n1 and n2 > n3:
#     print("max is", n2)
# else:
#     print("max is", n3)
#
# Q25. Write a program to display only those numbers from a list that satisfy the following conditions
#
# - The number must be divisible by five
#
# - If the number is greater than 150, then skip it and move to the next number
#
# - If the number is greater than 500, then stop the loop
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# ```
# numbers = [12, 75, 150, 180, 145, 525, 50]
# print("Sorted list", numbers)
# for num in numbers:
#     if num % 5 == 0 and num <= 150:
#         print(num)
#     elif num > 150:
#         continue
#     elif num > 500:
#         break
#
# Q26. What is a string? How can we declare string in Python?
#       String is keyword and datatype, which can store sequence of characters.
#       Declaration is as follows, name = 'harish'
#
# Q27. How can we access the string using its index?
#       Using [index], ex: name = 'harish', then -> name[0] = h
#
# Q28. Write a code to get the desired output of the following
#
# string = "Big Data iNeuron"
# desired_output = "iNeuron"
# print(string.split(" ")[2])
#
# Q29. Write a code to get the desired output of the following
#
# string = "Big Data iNeuron"
# desired_output = "norueNi"
# print((string.split(" ")[2])[:: -1])
#
# Q30. Reverse the string given in the above question.
# print(string[:: -1])
#
# Q31. How can you delete entire string at once?
#       Deleting or clearing a string value can be done assigning an empty value = '', ex: string = ''
#
# Q32. What is escape sequence?
#       An escape sequence is a sequence of characters, when used inside a character or string, does not count itself,
#       but it will be converted into another character or series of characters.
#       ex: \n, -> print('Harish\n') --> this will print only Harish and \n is treated as to goto next line
#
# Q33. How can you print the below string?
#
# 'iNeuron's Big Data Course'
# str = "iNeuron's Big Data Course"   # making use of double quotes at outer end
# str = 'iNeuron''s Big Data Course'  # making use of single quotes with single-quotes
# str = 'iNeuron\'s Big Data Course'  # making use of \(backslash) with single-quotes
#
# Q34. What is a list in Python?
#       A list is a data type in python, which can store multiple values of same or different datatypes
#       Ex: num = [1, 1.2, 3, 5, 7.8]
#
# Q35. How can you create a list in Python?
#       Using square brackets, num = [1, 1.2, 3, 5, 7.8]
#
# Q36. How can we access the elements in a list?
#       Using index, num = [1, 1.2, 3, 5, 7.8], num[2] -> 3
#
# Q37. Write a code to access the word "iNeuron" from the given list.
#
# lst = [1, 2, 3, "Hi", [45, 54, "iNeuron"], "Big Data"]
# print(lst[4][2])
#
# Q38. Take a list as an input from the user and find the length of the list.
# lst = [1, 2, 3, "Hi", [45, 54, "iNeuron"], "Big Data"]
# print(len(lst)) # output is 6
#
# Q39. Add the word "Big" in the 3rd index of the given list.
#
# lst = ["Welcome", "to", "Data", "course"]
# lst[2] = "Big" + lst[2]
# print(lst[2]) # ans -> BigData
#
# Q40. What is a tuple? How is it different from list?
#       Tuple is another dataType same as list available in python, only change from list is, it cannot be altered.
#       ex: t1 = (1, 2, 3)
#
# Q41. How can you create a tuple in Python?
#       Using normal brackets, t1 = (1, 2, 3)
#
# Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
# t1 = ()
# t1 = t1.__add__('harish')  # TypeError: can only concatenate tuple (not "str") to tuple
# print(t1)
# Tuple cant be altered with any string or other values, except for adding new tuple values
# t1 = ()
# t1 = t1.__add__(('harish', 'bangalore'))
# print(t1)  # ('harish', 'bangalore')
# t1 = t1.__add__(('PC', 'NYK'))
# print(t1) # ('harish', 'bangalore', 'PC', 'NYK')
#
# Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
# Yes
# t1 = ('harish', 'bangalore')
# t2 = t1 + ('PC', 'NYK')
# print(t2)
#
# Q44. Take a tuple as an input and print the count of elements in it.
# t1 = ('harish', 'bangalore', 'PC', 'NYK')
# print(len(t1))  # 4
#
# Q45. What are sets in Python?
#       Set is dataType is python, which stores a unique list of values only
#
# Q46. How can you create a set?
# set1 = set() # by creating an object of set()
# set1.add(1)
# print(set1) # {1}
#
# Q47. Create a set and add "iNeuron" in your set.
# set1 = set()
# set1.add("iNeuron")
# print(set1)  # {'iNeuron'}
#
# Q48. Try to add multiple values using add() function.
# set1 = set()
# set1.add(1)
# set1.add(1)
# set1.add(2)
# set1.add(3)
# set1.add(4)
# set1.add(6)
# print(set1)  # {1, 2, 3, 4, 6}
#
# Q49. How is update() different from add()?
# set1 = set()
# set1.add("iNeuron")  # will add new values
# set2 = set({'Ab', 'Cd'})
# set1.update(set2)  # will add new values from another set to itself
# print(set1)
#
# Q50. What is clear() in sets?
# set1 = set()
# print(set1)
# set1.add("iNeuron")  # will add new values
# set2 = set({'Ab', 'Cd'})
# set1.update(set2)  # will add new values from another set to itself
# print(set1)
# set1.clear()  # will remove all values from set
# print(set1)
#
# Q51. What is frozen set?
#
# Q52. How is frozen set different from set?
#
# Q53. What is union() in sets? Explain via code.
#
# Q54. What is intersection() in sets? Explain via code.
#
# Q55. What is dictionary ibn Python?
#
# Q56. How is dictionary different from all other data structures.
#
# Q57. How can we delare a dictionary in Python?
#
# Q58. What will the output of the following?
#
# var = {}
# print(type(var))
# Q59. How can we add an element in a dictionary?
#
# Q60. Create a dictionary and access all the values in that dictionary.
#
# Q61. Create a nested dictionary and access all the element in the inner dictionary.
#
# Q62. What is the use of get() function?
#
# Q63. What is the use of items() function?
#
# Q64. What is the use of pop() function?
#
# Q65. What is the use of popitems() function?
#
# Q66. What is the use of keys() function?
#
# Q67. What is the use of values() function?
#
# Q68. What are loops in Python?
#
# Q69. How many type of loop are there in Python?
#
# Q70. What is the difference between for and while loops?
#
# Q71. What is the use of continue statement?
#
# Q72. What is the use of break statement?
#
# Q73. What is the use of pass statement?
#
# Q74. What is the use of range() function?
#
# Q75. How can you loop over a dictionary?
#
# Coding problems
# Q76. Write a Python program to find the factorial of a given number.
#
# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100
#
# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
#
# Q79. Write a Python program to check if a number is prime or not.
#
# Q80. Write a Python program to check Armstrong Number.
#
# Q81. Write a Python program to find the n-th Fibonacci Number.
#
# Q82. Write a Python program to interchange the first and last element in a list.
#
# Q83. Write a Python program to swap two elements in a list.
#
# Q84. Write a Python program to find N largest element from a list.
#
# Q85. Write a Python program to find cumulative sum of a list.
#
# Q86. Write a Python program to check if a string is palindrome or not.
#
# Q87. Write a Python program to remove i'th element from a string.
#
# Q88. Write a Python program to check if a substring is present in a given string.
#
# Q89. Write a Python program to find words which are greater than given length k.
#
# Q90. Write a Python program to extract unquire dictionary values.
#
# Q91. Write a Python program to merge two dictionary.
#
# Q92. Write a Python program to convert a list of tuples into dictionary.
#
# Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
#
# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]
# Q94. Write a Python program to get all combinations of 2 tuples.
#
# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
# Q95. Write a Python program to sort a list of tuples by second item.
#
# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)]
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
# Q96. Write a python program to print below pattern.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# Q97. Write a python program to print below pattern.
#
#     *
#    **
#   ***
#  ****
# *****
# Q98. Write a python program to print below pattern.
#
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# Q99. Write a python program to print below pattern.
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Q100. Write a python program to print below pattern.
#
# A
# B B
# C C C
# D D D D
# E E E E E
