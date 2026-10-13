words=input("Enter words separated by spaces:").split()
largest=max(words,key=len)
print("Longest word:",largest)
print("Length of the longest word : ",len(largest))
