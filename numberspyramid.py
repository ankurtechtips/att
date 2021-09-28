line_ele=[]
base_ele=1
levels=3
step=2
for i in range(levels):
    for j in range(levels-i):
        print(" ",end='')
    for k in range(i+1):
        print(base_ele," ",end='')
    print("\n")
    line_ele.append(base_ele)
    base_ele+=step

for i in range(len(line_ele)):
    print("Row ",i+1," : ",line_ele[i],"s = ",line_ele[i]," * ",i+1," = ",line_ele[i]*(i+1))
