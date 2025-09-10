#student name -Ujjawal Mishra
#Roll No-2024UG3021
#Course: CS-2101/CD-2101 -Python Programming Lab
#Experiment No-1 - Task 1: Create a program to compute student marks(average , grade ,classification) . for instance ,marks could be translated into grades as follows:
# 90-100 A 
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

#Code to compute student marks, average, grade, and classification
num_subjects = int(input("Enter the number of subjects: "))
marks = []
for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
total_marks = sum(marks)
average_marks = total_marks / num_subjects
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
elif average_marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade: {grade}")
if average_marks >= 60:
    classification = "Pass"
else:
    classification = "Fail"
print(f"Classification: {classification}")
