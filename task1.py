import string

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers (0-9).")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters (!, @, #, etc.).")

    print("\nPassword Strength:")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")

    if feedback:
        print("\nSuggestions to improve:")
        for item in feedback:
            print("-", item)
    else:
        print("Excellent! Your password meets all basic checks.")


password = input("Enter your password: ")
check_password(password)
