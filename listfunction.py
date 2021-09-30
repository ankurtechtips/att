def add():
    print("OUTPUT 1 : ")
    mylist= list()
    print("How many elements do you want to insert: ",end="")
    n = int(input())
    for i in range (0,n):
        a = int(input("Add an element to list = "))
        mylist.append(a)
    print(mylist)
    print("OUTPUT 2 : ")
    mydict = {n: n for n in mylist}
    print(mydict)
    print("OUTPUT 3 : ")
    f = mydict.values()
    s = sorted(f, reverse=True)
    print(s)
add()
