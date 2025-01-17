# n1=int(input("Enter the start integer"))
# n2=int(input("Enter the end integer"))
# for num in range (n1,n2+1):
#   if num > 1: 
#         flag = True
#         for i in range(2, int(num ) + 1): 
#           if num % i == 0:
#             flag = False
#             break
#         if flag:
#             print(num)
      


n1 = int(input("Enter the start integer: "))
n2 = int(input("Enter the end integer: "))
print(n1)
for num in range(n1, n2 + 1): 
    if num > 1: 
        flag = True
        for i in range(2, int(num ** 0.5) + 1): 
            if num % i == 0:
                flag = False
                break
        if flag:
            print(num)
print(n2)

