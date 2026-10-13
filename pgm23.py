n=int(input("Enter number of elements:"))
d={}
for i in range(n):
  key=input("enter key")
  value=int(input("enter value"))
  d[key]=value
print("original dictionary",d)
print("Ascending order:",dict(sorted(d.items())))
print("Descending order:",dict(sorted(d.items(),reverse=True)))
