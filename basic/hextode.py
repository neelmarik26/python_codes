hexnum=input("Enter a hexadecimal number: ")
numre=[]
ttl=0
for j in range ((len(hexnum)-1),-1,-1):
  # print(j)
   numre.append(hexnum[j])
print(numre)
for i in range (0,len(numre)):
   if (numre[i]=="a" or numre[i]=="A"):
      max=10*(16**i)
      ttl=ttl+max
   elif (numre[i]=="b" or numre[i]=="B"):
      max=11*(16**i)
      ttl=ttl+max
   elif (numre[i]=="c" or numre[i]=="C"):
      max=12*(16**i)
      ttl=ttl+max
   elif (numre[i]=="d" or numre[i]=="D"):
      max=13*(16**i)
      ttl=ttl+max
   elif (numre[i]=="e" or numre[i]=="E"):
      max=14*(16**i)
      ttl=ttl+max
   elif (numre[i]=="f" or numre[i]=="F"):
      max=15*(16**i)
      ttl=ttl+max
   elif (int(numre[i])<=9):
      max=int(numre[i])*(16**i)
      ttl=ttl+max
   else:
      print("Invalid hexadecimal number")
      break
print("The decimal value is: ",ttl)