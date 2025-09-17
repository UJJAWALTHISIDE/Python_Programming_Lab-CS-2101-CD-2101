# Password validator - no functions, uses a while loop
specials = set("!@#$%^&*()-_+=[]{}|\\;:'\",.<>/?`~")  # allowed special characters

while True:
    pwd = input("Enter a password: ")
    errors = []
    if len(pwd) < 8:
        errors.append("Minimum 8 characters")
    if not any(c.isupper() for c in pwd):
        errors.append("At least one uppercase letter")
    if not any(c.islower() for c in pwd):
        errors.append("At least one lowercase letter")
    if not any(c.isdigit() for c in pwd):
        errors.append("At least one number")
    if not any(c in specials for c in pwd):
        errors.append("At least one special character (e.g. @, #, !, etc.)")

    if errors:
        print("\nPassword invalid — you missed:")
        for err in errors:
            print("  -", err)
        print("Please try again.\n")
    else:
        print("\nPassword is valid. ✅")
        break