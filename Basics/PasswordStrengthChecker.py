#     2. Password Strength Checker Program 


import re

def checkSmallerLetters(s):
    r = re.search(r"[a-z]", s)
    return r is not None

def checkCapitalLetters(s):
    r = re.search(r"[A-Z]", s)
    return r is not None

def checkDigits(s):
    r = re.search(r"[0-9]", s)
    return r is not None

def checkSpecialCharacter(s):
    r = re.search(r"[^a-zA-Z0-9_]", s)
    return r is not None


def checkStrength(s):

    if len(s) < 8:
        print("Weak Password!")
        print("Password must contain at least 8 characters.")

    elif checkSmallerLetters(s) and checkCapitalLetters(s) and checkDigits(s):

        if checkSpecialCharacter(s):
            print("Strong Password!")
            print("Good Password!")
        else:
            print("Medium Strength Password!")
            print("Password must contain at least one special character.")

    else:
        print("Medium/Weak Password!")
        print("Password must have at least one Uppercase, Lowercase and Digit.")


password = ""
print("---- Password Strength Checker Program ----")

while password != "exit":
    password = input("Enter the password (type exit to quit): ")

    if password != "exit":
        checkStrength(password)

print("---- End of Program ----")