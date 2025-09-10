#student name -Ujjawal Mishra
#Roll No-2024UG3021
#Course: CS-2101/CD-2101 -Python Programming Lab
#Experiment No-1 - Task 4: Input two complex numbers and display their sum, difference, and product.

#Code to perform arithmetic operations on two complex numbers

a1=int(input("Enter the real part of first complex number: "))
b1=int(input("Enter the imaginary part of first complex number: "))
a2=int(input("Enter the real part of second complex number: "))
b2=int(input("Enter the imaginary part of second complex number: "))
c1=a1+a2
c2=b1+b2
print(f"Sum: {c1}+{c2}j")
print(f"Difference: {a1-a2}+{b1-b2}j")
print(f"Product: {a1*a2-b1*b2}+{a1*b2+b1*a2}j")