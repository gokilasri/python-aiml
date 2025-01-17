#functions are a block of code which can be used any number of times to perform a certain operation or calculation( code reuseablity)
#def name_of_function(x,y,z):
#function body
#return [value(s)]
def print_greeting(user):
    print(f"hello,{user}!")
    return
user = input("enter ur name")
print(print_greeting(user))
#the term "scope of a variable" refer to the region of the program code which provide acess to the variable
def loacl_var():
    num = 50
    print(num)
    return
num=70
loacl_var()
print(f"the var is{num}") # the num cant be accessed out side the block
#default function arguments
def name_of_fun(a=5,b=5):
    return a+b

print(name_of_fun(6,7))

#here 5 and 5 are the default values of a and b
#the constarints with default aruguments is that all the arguments present to the right side of your default arguments  must be default arguments
#def name2(a=5,b):---> invaild definition

def name2(a,b=5):
    return a+b
def name3 (a,b,c=5):
    return a+b+c
def name4 (a,b,c=5,d=6):
    return a+b+c+d

print(name2(4))
print(name3(2,3,4))
print(name4(6,1))

#*args, #**kwargs
#args -> arguments,
#kwargs -> Key-worded argumrnts.
#type.....tuple
def sum_of_n_terms(*args):
    print(sum(args))
sum_of_n_terms(1,2,3,4,9,55,6,6,4)  

#kwargs(type.....dic)
def sum_of_keywords(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
sum_of_keywords(name="python",length_of_name =6,analogies =["c","c++","java"])

def generic_function(a,b,*args,**kwargs):
    print(a,b,args,kwargs)
generic_function(4,5,6,7,8,9,country="hii",value=7)


#sorted function in python
#sorted(iterable,key=None,Reverse =False) is an inbuilt used to sort iterable based on the vaules of the key parametr provided
my_list =["s","b","n","a"]
x= sorted (my_list,reverse=True)
print(x)
print(my_list)

my_list2=["leopard","polar bear","Lion","panter"]
x=sorted(my_list2,key=len)
print(x)
x=sorted(my_list2,key=len,reverse=True)
print(x)

#ASCII VALUE SORTING  UPPER CASE LOWER CASE
import math
my_list3 =[1,2,3,47,2,3]
print(sorted(my_list3,key=math.sin))