#student name -Ujjawal Mishra
#Roll No-2024UG3021
#Course: CS-2101/CD-2101 -Python Programming Lab
#Experiment No-3 - Task 4: Define a function highest_grade that accepts a dictionary with student names as keys and their grades as values. 
# Use the max() function to find the student with the highest grade. Test the function with a sample dictionary. 

def highest_grade(grades):
    if not grades:
        return None, None
    highest_student = max(grades, key=grades.get)
    return highest_student, grades[highest_student]
# Test the function with a sample dictionary
sample_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 88}
print(highest_grade(sample_grades))
print(highest_grade({}))  # Test with an empty dictionary