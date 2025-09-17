age = int(input("Please enter your age: "))
if age < 0:
    print("Invalid age. Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are a senior.")
        