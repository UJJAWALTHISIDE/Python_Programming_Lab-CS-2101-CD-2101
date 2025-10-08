#student name -Ujjawal Mishra
#Roll No-2024UG3021
#Course: CS-2101/CD-2101 -Python Programming Lab
#Experiment No-3 - Task 1: Define a function rectangle_area_perimeter that takes the length and width as input parameters.
#  Return both the area and perimeter of the rectangle from the function.
def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Example calls
print(rectangle_area_perimeter(5, 10))
print(rectangle_area_perimeter(3, 7))   