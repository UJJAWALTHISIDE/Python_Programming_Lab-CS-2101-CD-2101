# Multiplication Table Generator (1 to 12)
def generate_single_table(num):
    print(f"\nMultiplication Table for {num}:")
    print("-" * 25)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Get user input
number = int(input("Enter a number to generate its multiplication table: "))
generate_single_table(number)



