n = int (input ("Enter a positive number:"))
a, b = 0, 1  
flag = 0
while(a<=n):
 print(a, end=" ")  
#  a, b = b, a + b
 temp=a+b
 a=b
 b=temp
 if (n==a):
    flag=1
    break
if (flag):
    print("its a fib series") 
else:
        print("its not")
  

