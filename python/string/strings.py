
#strings length
sample="hello world "
print(len(sample))
#find a character
print(sample.find('o'))
#including positions
print(sample.find('o',6,12))
#replace string
print(sample.replace('o','a'))#u can sepicify by using ('o','a',1)
#capitalize
print(sample.capitalize())
#lower
print(sample.lower())
#upper
print(sample.upper())
#isalpha(),isdigit(),isalnum(),isspace()
sample="123"#no alpha
if sample.isdigit():
 print ("hi")
sample="hiiii"#no num
if sample.isalpha():
 print ("hi")
 sample="1jighf23"
if sample.isalnum():#both alpha digit no @#$
 print ("hi")
sample=" " #5678 bhjii 8nn doesnt work
if sample.isspace(): #only space
 print ("hi")