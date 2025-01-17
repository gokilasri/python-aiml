#1)float average
n1=float(input())
n2=float(input())
print("the average is :",(n1+n2)/2)
#2)arithmetic operation without zero
n1=int(input())
n2=int(input())
print(n1+n2)
print(n1-n2)
print(n1*n2)
if(n1!=0 and n2!=0):
  print(n1/n2)
else:
  print("Cannot divide by zero")
# 3)students score
n1=int(input())
if (n1<=100):
 if(90<=n1<=100):
    print("A")
 elif(80<=n1<=89):
    print("B")
 elif(70<=n1<=79):
    print("C")
 elif(60<=n1<=69):
    print("D")
 else:
    print("F")
# 4)max of three numbers
n1=int(input())
n2=int(input())
n3=int(input())
if(n1>n2 and n1 >n3):
    print(f"{n1}")
elif(n2>n1 and n2 >n3):
    print(f"{n2}")
else :
    print(f"{n3}")
# 5)swap
n1=int(input())
n2=int(input())
temp=n1
n1=n2
n2=temp
print(n1,n2,temp)
# 6)leap year
n1=int(input())
if(n1>0):
 if (n1 % 400 == 0):
          print(f"{n1} is a leap year")
 elif (n1 % 4 == 0) and (n1 % 100 != 0):
          print(f"{n1} is a leap year")
 else:
          print(f"{n1} is not a leap year")
else:
       print("invaild year")
# 7)array--list
my_list = input("Enter a list: ").split()
my_list.sort(reverse=True)  
print(my_list)  
# 8)prime number
n1 = int(input("Enter a number: "))
if n1 <= 1: 
    print("Not a prime number")
else:
    flag = 0
    for i in range(2, n1): 
        if n1 % i == 0:
            flag = 1
            break
    if flag == 0:
        print("It's a prime number")
    else:
        print("Not a prime number")    
# 9)factoriAL
n=int(input(" enter a positive number"))
fact=1
if(n<0):
    print("not a positive number")
else:
 for i in range (1,n+1) :
    fact=fact*i
print(fact)
    
# 10)conditional rendering days in month

# 11)odd or even
num = int(input())
if (num % 2) == 0:
 print("The number is even")
else:
 print ("The provided number is odd")
#  12 add fact
n=int(input(" enter a positive number"))
fact=0
if(n<0):
    print("not a positive number")
else:
 for i in range (1,n+1) :
    fact=fact+i
print(fact)
# 13)replace in string
sample = input()
word_replaced=input("the word to be replaced:")
word_replaced1 =input("the word to be replaced with:")
print(sample.replace(word_replaced,word_replaced1))
# 14)count vowels/constants
str1=input()
con=0
vo=0
for i in str1:
  if i.lower() in "aeiou":
   vo+=1
  else:
   con+=1
print("constants",con,"vowels",vo)
# 15)100-perfect square
n = int(input("Enter a number: "))
flag = 0
for i in range(0, n//2+2):
 if i * i == n:
        flag=1
        break
if flag:
    print(f"{n} is a perfect square.")
else:
    print(f"{n} is not a perfect square.")

# 16)108)palnidrome

number = int(input("Enter a number: "))
original_number = number 
while number > 0:
    remainder = number % 10
    reversed_number = reversed_number * 10 + remainder
    number //= 10
if original_number == reversed_number:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

# print 17) 81)
n = (input())
print(n)
# 18)80)check its alpha,num,
var = input("Enter a Character :")
if( var.len(var)== 1):
 if (var.isalpha()):
    print("you have entered a alphabet")
 elif(var.isdigit()):
    print("you have enter a digit")
 elif(var.isspace()):
    print ("you have enter a white space")
 else: 
    print("invalid input or special characters")
else: 
    print("invalid input or special characters")
# 19)102 #binary to decimal
binary=input()
decimal=0
for digit in binary:
    decimal = decimal*2 +int(digit)
print(decimal)
# 20)decimal to binary
decimal=int(input())
binary=""
if decimal == 0:
    print(0) 
while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
print( binary)
#single star pattern 
n = int(input())
count,space=0,0
for i in range(1,2*n):
    if i <=n:
        count = i-1
        space = n-i
    else:
        count-=1
        space = i-n
    string_print = " "*space+"* "*count+"*"
    print(string_print)



#half daimond
n = int(input())
count,space=0,0
for i in range(1,n+1):
    if i <=n:
        count = i-1
        space = n-i
    string_print = " "*space+"* "*count+"*"
    print(string_print)


#hallow daimond prlm
n=int(input())
space_count,mid_space=0,0
for i in range(1,2*n):
    space_count = n-i if i<=n else i-n 
    if i == 1 or i==2*n-1:
        string_print = " "*space_count+"*"
    elif i<=n:
        mid_space=2*(i-1) - 1
        string_print=" "*space_count+"*"+" "*mid_space+"*"

    else:
        mid_space-=2
        string_print =" "*space_count+"*"+" "*mid_space+"*"
    print(string_print)
    