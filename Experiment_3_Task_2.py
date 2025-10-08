#student name -Ujjawal Mishra
#Roll No-2024UG3021
#Course: CS-2101/CD-2101 -Python Programming Lab
#Experiment No-3 - Task 2: Define a function list_summary that accepts a list of integers. Return the sum, average, and maximum value of the list as a tuple. 
# Test the function with a sample list.
def list_summary(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    maximum = max(numbers) if numbers else 0
    return total, average, maximum

# Test the function with a sample list
print(list_summary([1, 2, 3, 4, 5]))
print(list_summary([10, 20, 30]))