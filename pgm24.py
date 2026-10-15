n = int(input("Enter number of elements in dictionary 1: "))
dict1 = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

m = int(input("Enter number of elements in dictionary 2: "))
dict2 = {}

for i in range(m):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict2[key] = value

dict1.update(dict2)

print("Merged dictionary:", dict1)
