num = 5
list_a = [1, 2, 3, 4, 7, 90, 20]
dict_a = {'shashank': 20, 'rahul': 30}
try:
    print("Divide number by 0 ")
    # result = num/0
    result = num / 5
    print(result)
    print("Step 1 Done ")

    print("Access 11'th element from List ")
    # print(list_a[11])
    print(list_a[5])
    print("Step 2 Done ")

    print("Access value of amit from dictionary ")
    # print(dict_a['amit'])
    print(dict_a['shashank'])
    print("Step 3 Done ")
except ZeroDivisionError:
    print("This Error Was Occurred Because Division by 0 Happened !!")
except IndexError:
    print("Error Occurred because out of bound index is getting accessed !!")
except KeyError:
    print("Search Key Doesn't Exists !!")
except Exception as err:
    print("Error Occurred and Message : ", err)

# Use of Else Block
a = 5
try:
    # result = a / 0
    result = a / 2
except ZeroDivisionError:
    print("Error Occurred because of Division by 0 !!")
else:
    print("Calculation completed !!")
    print(result)

# Use Of Finally Keyword
a = 5
try:
    result = a / 2
    # result = a / 2
except ZeroDivisionError:
    print("Error Occurred because of Division by 0 !!")
else:
    print("Calculation completed !!")
    print(result)
finally:
    print("Doesn't matter try-except but I will print myself !!")
