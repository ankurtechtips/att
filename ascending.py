list=[1, 5, 4, 7, 8]
print("Orignal list: ", list)
temp=0
for i in range (0,len(list)):
    for j in range (1,len(list)):
        if list[i]<list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
for i in range(0,len(list)):
    print(list[i])
