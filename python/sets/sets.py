#sets aare nothing but a collecton of variables ellements,where each unique element is stored only once.it does not allow duplicate entries
#[1,2,,3,4,4,2,4]
sample = {1,2,5,3,4,4,2,4}
print(type(sample))
print(sample)
#sets are ordered and sorted it cant accessed by index value

#set methods
#set add
sample.add(20)
print(sample)
#set are muttable
sample2 = sample
sample2.add(19)
print(sample)
#clear
# sample.clear()
# print(sample,sample2)
#length of set
print(len(sample))
#remove element
sample.discard(9)
print(sample)
sample.remove(20)#remove and discard diff...discard dont show error when there is no element
print(sample)
## set opeartion
#set intersection
sample = {1,2,5,3,4,4,2,4}
sample = {1,2,5,3,4,4,2,4,8,9,6,8}

print(sample&sample2)#.................(.intersection())
#set union
print(sample|sample2)#.................(.union())
#set difference
print(sample-sample2)#.................(.union())

