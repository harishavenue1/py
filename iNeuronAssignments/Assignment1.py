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
