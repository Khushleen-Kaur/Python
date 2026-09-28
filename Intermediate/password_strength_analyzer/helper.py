
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
        score = 1
        print(f"{"Uppercase":<20}: {upper} ✓")
    else:
        score = 0
        print(f"{"Uppercase":<20}: {upper} ✗")
        suggestion = "Password must contain atleast one 'Uppercase' character."
    return suggestion,score

