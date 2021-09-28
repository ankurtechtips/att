#Sort a Set
numbers = {4, 2, 12, 8, 6, 3}
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

#Check 3 strings are anagrams
s1= "learnt"
s2= "antler"
s3= "rental"
if(sorted(s1)== sorted(s2)==sorted(s3)):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")
    
#Check for missing elements in a set
set1= set()
set2= {1,3,5,9,13,15}
n=7;
i=1
for k in range (0,n):
    i=i+2
    set1.add(i)
print("Set1: ",set1)
print("Set2: ",set2)
set3= set1 - set2
print("Missing numbers : ", set3)
