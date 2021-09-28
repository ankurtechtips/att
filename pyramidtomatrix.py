line_ele=[]
base_ele=1
levels=3
step=3
ele_eachLine=[]

print("Output 1: ")

for i in range(levels):
    temp_list=[]
    for j in range(levels-i):
        print(" ",end='')
    for k in range(i+1):
        m= base_ele+k
        print(m," ",end='')
        temp_list.append(m)

    print("\n")
    ele_eachLine.append(temp_list)

    base_ele+=step

print("Output 2: ")
totalsum=0
for i in ele_eachLine:
    totalsum+=sum(i)
    print(sum(i))

print(totalsum)

print("Output 3: ")

max_index = len(ele_eachLine[-1])

matrix_final =[]

for i in ele_eachLine:
    for j in range(len(i), max_index):
        i.append(0)




matrix_final = ele_eachLine[::-1]

for i in matrix_final:
    print(i)


for i in range(len(matrix_final)):
    for j in range(len(matrix_final[i])):
        matrix_final[i][j]=matrix_final[i][j]**2

print("Output 4 :")
for i in matrix_final:
    print(i)
