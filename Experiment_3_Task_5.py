#student name -Ujjawal Mishra
#Roll No-2024UG3021
#Course: CS-2101/CD-2101 -Python Programming Lab
#Experiment No-3 - Task 5: Import the random and math modules. Generate a random number between 1 and 100 using random.randint(). Use the math module to check if the number is prime. 
# (A prime number is a number greater than 1 that has no divisors other than 1 and itself.) 
# Print whether the random number is prime or not.

import random
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
random_number = random.randint(1, 100)
if is_prime(random_number):
    print(f"{random_number} is a prime number.")
else:
    print(f"{random_number} is not a prime number.")
# Example calls
print(is_prime(29))  # True
print(is_prime(30))  # False