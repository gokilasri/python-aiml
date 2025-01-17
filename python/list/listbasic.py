#append
x=[1,2,3,4,5]
x.append(6)
print(x)
#index
print(x.index(4))
#x.clear() delete
x.clear()
#insert
x=[1,2,3,4]
x.insert(2,"py")
print(x)
#count
print(x.count(4))
#remove
print(x.remove(4))
print(x)
#pop
x=[1,2]
y=x.pop('2')
print(y)
#sort
x=[1,2,6,3,7,9]
x.sort()
print(x)
x.sort(reverse=True)#decending (reverse=True)
print(x)
#into list
x=list("string")
print(x)
#into tuples
x=tuple("string")
print(x)
#tuple in list
x=list(x)
print(x)
#split method
x = "this is a string"
print(x.split(" ")) 
y="this:is:another a bc"
print(y.split(":"))
m="this:isbcanother a bc "
print(m.split("bc"))
#mutable datatype are those data type which can afford changes you can change the values which are being stored in a same address 
# immutable(string,tuple)
x=[1,2,3,4]
y=x#create a deep copy
print(x)
print(y)
print(id(x),id(y))
y.append(7)
print(x)
print(y)#change x then both x and y has same value
#immutable
str="str1"
str1=str
print(str,str1)
str+="hello"
print(str)
print(str1)
print(id(x),id(y),id(str),id(str1))
#copy
sam1=[1,2,3,4]
sam2=sam1.copy()
print(sam1 , sam2)
print (id(sam1),id(sam2))# shallow copy the changes make in sam1 cant affect
#extend method can use multiple concatinate
a=[1,2,3,4]
a.append([1,2,3,4])
print(a)
b=[1,2,3,4]
b.extend([1,2,3,4])
print(b)
b.extend("python")
a.append("python")
print(a)
print(b)

#map functions
num_list = list(map(int,input().split()))
num_list = set(map(int,input().split()))
num_list = tuple(map(int,input().split(':')))
num_list = list(map(len ,["h","ji","hiii","hy"]))#[1,2,4,2]

#in operator
x= "sub"
y = "substring"
if x in y:
    print("yes")
else:
    print("false")

