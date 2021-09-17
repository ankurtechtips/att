list=[1, 5, 4, 0, 7, 8]
print("Orignal list", list)
a=7
print("Find index of", a)
for i in range (0, len(list)):
  if list[i]==a:
    print(i)
