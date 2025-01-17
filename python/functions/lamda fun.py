#lambda functions
#lambda functions are small, compact functionswhich are ideal for one time use and throeaway task it is ideal for those scenario where functions are passed as an arguments it can take multiple arguments but can only return a single expression

square_func = lambda x,y:x**2+y**2
print(square_func(3,4))

list_of_tuple = [(20,1),(30,-2),(-11,5),(76,100),(12,-25)]
print(sorted(list_of_tuple,key=lambda x:x[0]))
list_of_tuple2 = [("peter",1),("miles",-2),("flash",5)]
print(sorted(list_of_tuple2,key=lambda x:x[1]))

print(list_of_tuple2[0][0])



sample_dict ={"jan":1,"feb":2,"mar":3,"apr":4,"may":-5}
print(sorted(sample_dict,key=lambda x:x[0]))
print(sorted(sample_dict.values()))
print(type(sample_dict))