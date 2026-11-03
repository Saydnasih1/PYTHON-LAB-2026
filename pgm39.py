def add(*args):
    total = 0
    for i in args:
        total = total + i
    return total
n = int(input("Enter the number of arguments: "))
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
result = add(*numbers)
print("Sum of numbers:", result)
print("\nDocstring:")
print(add.__doc__)
