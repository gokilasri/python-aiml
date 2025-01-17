n = int (input ("Enter a number"))
a, b = 0, 1  
count =0
if(n>0):
 while(count<n):
  print(a, end=" ")  
  temp =a + b,a=b,b=temp
  count+=1

