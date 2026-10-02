
def analyze_length(password):
    suggestion = ""
    if(len(password) < 8):
        print(f"{"Length":<20}: {len(password)} ✗")
        score = 0
        suggestion = "Weak password: Length must be 12+ for strong password."
    elif(8 <= len(password) <= 11):
        score = 1
        print(f"{"Length":<20}: {len(password)} ✗")
        suggestion = "Moderate password: Length must be 12+ for strong password."
    else:
        score = 2
        print(f"{"Length":<20}: {len(password)} ✓ ")
    return suggestion, score 
def upper_letters(s):
    upper = 0
    suggestion = ""
    for i in s:
        if i.isalpha():
            if i == i.upper():
                upper += 1
    if upper >0:
        score = 2
        print(f"{"Uppercase":<20}: {upper} ✓")
    else:
        score = 0
        print(f"{"Uppercase":<20}: {upper} ✗")
        suggestion = "Password must contain atleast one 'Uppercase' character."
    return suggestion,score

def lower_letters(s):
    lower = 0
    suggestion = ""
    for i in s:
        if i.isalpha():
            if i == i.lower():
                lower += 1
    if lower > 0:
        print(f"{"Lowercase":<20}: {lower} ✓")
    else:
        print(f"{"Lowercase":<20}: {lower} ✗")
        suggestion = "Password must contain atleast one 'Lowercase' character."
    return suggestion, 0

def digits(s):
    count = 0
    suggestion = ""
    for i in s:
        if i.isdigit():
            count += 1
    if count > 0:
        score = 1
        print(f"{"Digit":<20}: {count} ✓")
    else:
        score = 0
        print(f"{"Digit":<20}: {count} ✗")
        suggestion = "Password must contain atleast one 'Digit'."
    return suggestion,score

def specail_characters(s):
    special = 0
    suggestion = ""
    specail_character = r'[!@#$%^&*()_+.,\/]'
    for i in s:
        if i in specail_character:
            special += 1
    if special > 0:
        score = 1
        print(f"{"Special characters":<20}: {special} ✓")
    else:
        score = 0
        print(f"{"Special characters":<20}: {special} ✗")
        suggestion = "Password must contain atleast one 'Special' character."
    return suggestion,score


def display(sug):
    print("\n--------------------- Suggestions ---------------------")
    count = 1
    for i in sug:
        if i != '':
            print(str(count) + ". " + i)
            count += 1
    if count == 1:
        print("Strong Password.")
        print("No suggestions!")