a=input("Enter a number:")
try:
   int(a)
   print("input is integer")
except:
   try:
     float(a)
     print("input is float")
   except:
       try:
        complex(a)
        print("input is complex")
       except :
             print("input is not valid")
