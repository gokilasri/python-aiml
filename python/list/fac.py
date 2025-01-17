n=int(input(" enter a positive number"))
fact=1
if(n<0):
    print("not a positive number")
else:
 for i in range (1,n+1) :
    fact=fact*i
print(fact)
    
# 100,102,103,104,28,23,22,18,63,57(1 loop),24