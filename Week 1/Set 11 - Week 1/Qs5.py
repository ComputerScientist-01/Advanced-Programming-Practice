# 5: Write a python program to check the total marks of a student in various examinations. The
# student will get A+ grade if the total marks are in the range 89..100 inclusive, if the
# examination is &quot;Final-exam.&quot; the student will get A+ grade and total marks must be greater
# than or equal to 90. Return true if the student get A+ grade or false otherwise.

marks = int(input("Enter the total marks: "))

if marks>=90 and marks <=100:
    print("Grade is A+")
    print("True")

else:
    print("False")