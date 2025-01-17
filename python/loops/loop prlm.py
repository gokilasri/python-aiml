# #print a pattern
# n = int(input("Enter a positive integer"))
# for i in range(65,65+n):
#     output= ""
#     for j in range(65, i + 1): 
#         output += chr(j) + " " 
#     print(output)
#     output = ""
#     print("\n")



# # #another version
# n = int(input("Enter a positive integer"))
# start_var = 'a'
# char_list =[]
# for i in range(n):
#    for j in range(i+1):
#        current_var = chr(ord(start_var)+j)
#        char_list.append(current_var)
# print(" ".join(char_list))
# char_list =[]

#replace vowels into strings
# str1 = input("Enter a string: ")
# str2 = ''
# for i in str1:
#     if i.lower() in "aeiou":
#         str2 += '*'
#     else:
#         str2 += i
# print(str2)


#occurance vowel


#refer and do


#space seperator odd even
x=list(map(int,input().split()))
result =["even" if i%2 == 0 else "odd"for i in x]
print(" ".join(result))