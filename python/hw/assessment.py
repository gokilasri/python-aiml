#happy number
num=int(input())
sum_of_squares = list()
flag = True
while 1:
    str_num = str(num)
    sq_sum = 0
    for i in str_num:
        sq_sum += int(i) **2
    if sq_sum==1:
        print("True")
        break
    elif sq_sum in sum_of_squares:
        print("false")
        break
    else:
        sum_of_squares.append(sq_sum)
    num=sq_sum
#repeating character return -1
str1= input()
d={}
res = []
for c in str1:
    d[c] = d.get(c, 0) + 1
for c, cnt in d.items():
    if cnt > 1:    
        res.append(c)
if res:
    print(-1)
else:
    print(len(str1))

#another version change in lower
string_input = input()
string_input = string_input.lower()
non_re_dict,rep_list ={},[]
for i in range (len(string_input)):
    if string_input[i] in rep_list:
        continue
    elif string_input[i] in non_re_dict:
        rep_list.append(string_input[i])
        del non_re_dict[string_input[i]]
    else:
        non_re_dict[string_input[i]]=i
if not non_re_dict:
    print("non repeating character -1")
else:
    list_of_dict =list(non_re_dict.items())
    list_of_dict= sorted(list_of_dict,key = lambda x:x[1])
    print(f"in string{list_of_dict[0][0]} and found in{list_of_dict[0][1]} ")


#another version
inp = str(input())
count=0
for i  in range (len(inp)):
      count = inp.count(inp[i])
      if(count==1):
            print(i)
            break
      if(count>1):
            count=0
if(count==0):
      print(-1)
#decimal->binary
decimal=int(input())
binary=""
if decimal == 0:
    print(0) 
while decimal > 0:
        remainder = decimal%2
        binary = str(remainder)+binary
        decimal //= 2
print(binary)


#substring
#sample.... "abcabcaccbb" output:3,[abc,bca,cab]    "bbbb" 1,[b]

