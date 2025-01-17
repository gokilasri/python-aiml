str=input("enter a string")
months={"jan":31,"feb":"28 or 29","mar":31,"april":30,"june":31,"july":30,"Aug":31,"sep":30,"oct":31,"nov":30,"dec":31}
for i in months:
 while i == str:
   print(f"{i}:{months[i]}")
   break
else:
  print("Kindly enter vaild month")


#another version
print(months.get(str,"kindly enter a vaild month"))