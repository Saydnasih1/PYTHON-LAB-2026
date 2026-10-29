def simple_interest(p, t, senior):
    if senior == 'yes':
        rate = 12
    else:
        rate = 10

    si = (p * t * rate) / 100
    return si

p = float(input("Enter the principal amount: "))
t = float(input("Enter the time in years: "))
senior = input("Is the customer a senior citizen? (yes/no): ").lower()

si = simple_interest(p, t, senior)

print("Simple Interest =", si)
