givnum=int(input("Enter a decimal number: "))
while (givnum>0):
   rem=givnum%16
   if (rem==10):
      print("A",end="")
   elif (rem==11):
      print("B",end="")
   elif (rem==12):
      print("C",end="")
   elif (rem==13):
      print("D",end="")
   elif (rem==14):
      print("E",end="")
   elif (rem==15):
      print("F",end="")
   else:
      print(rem,end="")
   givnum=givnum//16            
print()
