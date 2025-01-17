#dictionaries are anothe datatype in python they used to store data in the form of key:value pairs.dictionaries( there is no indexed but ordered)
sample_dict = {"A":1,"B":2,"C":3}
print(sample_dict["A"])
#empty dic
sample = {}
print(type(sample))
#for the key, you can only use an immutable data type
sample_dict = {"A":'a',"B":'b',"C":[1,2,3,4]}
print(sample_dict)
#for loop in dic
#we generally use for loop to traverse to a dic
for i in sample_dict:
 print(i)
print(f"{i}:{sample_dict[i]}")
print(sample_dict.keys())#dict_keys


for i in sample_dict.items():
 print(i)#tuples output
sample_dict.clear()
sample_dict = {"A":'a',"B":'b',"C":[1,2,3,4]}
sample_dict.pop('A')
print(sample_dict)

#get
print(sample_dict.get("C"))

#condition
a= sample_dict.get('key')
if a:
 print("present")
else:
 print ("not")