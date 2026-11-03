def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
n = int(input("Enter the number of terms: "))
sum = 0
for i in range(1, n + 1):
    term = (i ** i) / factorial(i)
    sum = sum + term
print("Sum of the series =", sum)
