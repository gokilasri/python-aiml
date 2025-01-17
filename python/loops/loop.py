    #for loop
for i in [1,2,3,4]:
    # 1 2 3 4
     for i in "string":
        print(i)
    # s t r i n g
#range (start, stop, step)
#range(1,11,2)  # [1,3,5,7,9]
#range(start,stop
#range(stop)


#nested loops
#lopp which contain another loop inside their body called nested lopps
#this can be used within for, while,while within while for within while and vice versa
count=0
for i in range(5):
    for j in range(5):
     count+=1
print(count)

#jump statements:The effect of jump statements in nested lopps the jump statements affecr only the loop in which they are present
for i in range(5):
   for j in range(5):
    if j==2:
       break
    print("inside the inner loop")
print("end")


#single line
x=int(input())
result ="even" if x%2 == 0 else "odd"
print("result")

#single line for
print(x**2 for x in range)