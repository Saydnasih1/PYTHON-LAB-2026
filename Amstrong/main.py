import Armstrong

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

for i in range(lower, upper + 1):
    if Armstrong.check_armstrong(i):
        print(i)
