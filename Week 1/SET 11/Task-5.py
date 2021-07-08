print("Enter the exam marks:")
marks=[]
print("Enter Marks Obtained in different exams: ")
for i in range(5):
    marks.insert(i, input())
    #print(marks[i])

tot = sum(int(marks[i]) for i in range(5))
avg = tot/5
print("The average is :",avg)
if avg >=90 :
    print("True")

