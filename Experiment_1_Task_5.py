#student name -Ujjawal Mishra
#Roll No-2024UG3021
#Course: CS-2101/CD-2101 -Python Programming Lab
#Experiment No-1 - Task 5:Convert temperature from Celsius to Fahrenheit and vice versa.

#Code to convert temperature from Celsius to Fahrenheit and vice versa

# Get temperature inputs from user
celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))

# Convert Celsius to Fahrenheit
celsius_to_fahrenheit = (celsius_temp * 9/5) + 32

# Convert Fahrenheit to Celsius
fahrenheit_to_celsius = (fahrenheit_temp - 32) * 5/9

# Display results
print(f"{celsius_temp}°C = {celsius_to_fahrenheit}°F")
print(f"{fahrenheit_temp}°F = {fahrenheit_to_celsius}°C")