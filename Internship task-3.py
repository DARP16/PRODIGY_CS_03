import re
import time

def check_password_strength(password):
    score = 0
    suggestions = []

    print("\nOkay, let's take a moment to review your password...")
    time.sleep(1)

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Your password is a bit short. Try making it at least 8 characters long.")

    # Upper and lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Using both uppercase and lowercase letters makes your password more secure.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Adding a number or two can really help strengthen your password.")

    # Special character check
    if re.search(r'[\W_]', password):
        score += 1
    else:
        suggestions.append("Consider using special characters like !, @, #, or * for added protection.")

    # Strength assessment
    print("\nHere’s our assessment of your password:")
    if score == 4:
        print("Your password is strong. Well done.")
    elif score == 3:
        print("Your password is decent, but it could be stronger with a few small changes.")
    else:
        print("This password is quite weak. It’s a good idea to improve it before using it.")

    if suggestions:
        print("\nSuggestions to make it stronger:")
        for tip in suggestions:
            print("-", tip)

    print("\nThanks for checking. Keep your accounts secure.")

# Run the checker
print("Welcome! Let's check how strong your password is.")
user_input = input("Enter a password to test: ")
check_password_strength(user_input)
