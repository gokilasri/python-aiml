n = int(input ("Enter a number"))
a, b = 0, 1  
fib =[]
sum =0
count = 0
while(a<=n):
 fib.append(a)
 if (a%2 !=0):
     sum+=a
     count+=1
     print (a,count)
 a, b = b, a + b
if (count>0):
    average = sum//count
    print(f"average is{average} and the index is {fib[count]}") 
else:
        print("no odd numbers")
  

