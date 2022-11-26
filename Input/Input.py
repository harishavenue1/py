s1 = input("Enter any values :")
print("String input", s1)
print("input type", type(s1))

s1List = s1.split(" ")
print("input after split", s1List)

int1List = []
for str1 in s1List:
    int1List.append(int(str1))

print("input after converting ", int1List)
print("input type after converting ", type(int1List[0]))
