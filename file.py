ls=[["Mo","mm@gg.com","1283"],[],[],["Test","tt@usr.com","9999"],["UserName","email","126487","city","street"],["Test","tt@usr.com","9999","houston","long street","20122"]]

file1=open("sample.txt","w")


#I've made a tuple of first three elements and then used it as a key t define dictionary to avoid duplicacy
#used the condition to ignore empty values
dict1={tuple(i[:3]):i for i in ls if i}


#print(dict1)

for i in dict1.values():
    for j in i:
        file1.write("%s,"%j)
    file1.write("\n")

file1.close()

file2=open("sample.txt","r")
st=list()
for i in file2.readlines():
    st.append(tuple(i.split(',')[:-1]))

final=tuple(st)
print(final)

file2.close()
