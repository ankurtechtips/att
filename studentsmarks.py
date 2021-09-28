students=["a","b","c","d"]
subjects =["Maths","Physics","Chemistry"]
scores =[[50,40,70],[70,80,90],[20,90,40],[15,70,90,100]]
max_marks=100
grades = []
student_status = []

for i in range(len(students)):
    sg = []

    for j in range(len(subjects)):

        if(scores[i][j]>=0.8*max_marks):
            sg.append("Distinction")

        elif(scores[i][j]>=0.6*max_marks):
            sg.append("First Division")

        elif (scores[i][j] >= 0.5 * max_marks):
            sg.append("Second Division")

        elif (scores[i][j] < 0.5 * max_marks):
            sg.append("Fail")
    grades.append(sg)

print(grades)

for i in range(len(students)):
    count=0
    for j in grades[i]:
        if(j=="Fail"):
            count=count+1

    if(count>=2):
        student_status.insert(i,"Fail")
    elif(count==1):
        student_status.insert(i,"Re-appear")
    else:
        student_status.insert(i,"Pass")

count =0
for i in student_status:
    if(i=="Pass"):
        count=count+1

class_performance=(count/len(students))*100

print("Passing status of class = ",class_performance)

re_appear=[]
failed=[]


for i in range(len(students)):
    if(student_status=="Re-appear"):
        re_appear.append(students[i])
    elif(student_status=="Fail"):
        failed.append(students[i])


print("Failed students ", failed)
print("Re-appearing students ", re_appear)

print("Results :")

for i in range(len(students)):
    print("Name : ",students[i])

    for j in range(len(subjects)):
        print(subjects[j]," : ",grades[i][j])
