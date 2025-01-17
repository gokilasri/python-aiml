n = int(input("enter a num"))
if n<=0:
 print("positive num")
else:
  a,b=0,1
  sum,count=0,0
  while(count<n):
   if(b%2 == 1):
    sum+=b 
    count+=1
    print(b)
   a,b=b,a+b
print(sum//count)
