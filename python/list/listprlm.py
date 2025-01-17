# arithmetic operations ---> 45+ 56..45-56....4*8
x = input("enter a string")
n=x.split(" ")
g=list(n)
a1=(g.pop())
a2=(g.pop())
a3=(g.pop())
if (a2 == "+"):
 print( int(a1)+ int(a3))
elif (a2 == "-"):
 print( int(a1)- int(a3))
elif (a2 == "%"):
 print( int(a1)% int(a3))
elif (a2 == "//"):
 print( int(a1)// int(a3))
#another method
expr = input("Enter an expression (e.g., 5 + 3): ").split()
expr[0], expr[2] = int(expr[0]), int(expr[2])
operator = expr[1]

if operator == '+':
    print(expr[0] + expr[2])
elif operator == '-':
    print(expr[0] - expr[2])
elif operator == '%':
    print(expr[0] % expr[2])
elif operator == '//':
    print(expr[0] // expr[2])
else:
    print("Invalid operator")
