# r = int(input("Enter the number of rows: "))
# c = int(input("Enter the number of columns: "))
# entries=[]
# matrix = []
# for i in range(r):
#     row = entries[(map(int, input( ).split()))]  
# for i in range(r):
#     for j in range(c):
#         print(matrix[i][j], end=' ')
#     print()
matrix_elements = list(map(str,input().split(',')))
matrix1=list(map(int,matrix_elements[0].split(" ")))
matrix2=list(map(int,matrix_elements[0].split(" ")))
matrix1_formatted,matrix2_formatted,indi_row = [],[],[]
count = 0
for i in matrix1:
   if count == 2:
      indi_row.append(1)
      matrix1_formatted.append(indi_row)
      indi_row=[]
      count =0
   else:
      indi_row.append(1)
      count += 1
for i in matrix2:
    if count==2:
      indi_row.append(1)
      matrix2_formatted.append(indi_row)
      indi_row=[]
      count =0
else:
     indi_row.append(i) 
     count+= 1
print(matrix1_formatted,matrix2_formatted,sep="\n")
# print(matrix)
# for i in range (len(matrix1)):
#     matrix3.append(str(matrix1[i]+ matrix2[i]))
# print(" ".join(matrix3))
