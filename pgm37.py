def compare(S1, S2, n):
    if S1[:n] == S2[:n]:
        return True
    else:
        return False

S1 = input("Enter the first string: ")
S2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to compare: "))

result = compare(S1, S2, n)
print(result)
