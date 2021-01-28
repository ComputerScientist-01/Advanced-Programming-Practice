print("Enter the exam marks:")
marks=[]
tot = 0
print("Enter Marks Obtained in different exams: ")
for i in range(5):
    marks.insert(i, input())
    #print(marks[i])

for i in range(5):
    tot = tot + int(marks[i])
avg = tot/5
print("The average is :",avg)
if avg >=90 :
    print("True")

