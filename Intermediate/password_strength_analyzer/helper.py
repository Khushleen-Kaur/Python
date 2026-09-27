
def analyze_length(password):
    suggestion = ""
    if(len(password) < 8):
        print(f"{"Length":<12}: {len(password)} ✗")
        suggestion = "Weak password: Length must be 12+ for strong password."
    elif(8 <= len(password) <= 11):
        print(f"{"Length":<12}: {len(password)} ✗")
        suggestion = "Moderate password: Length must be 12+ for strong password."
    else:
        print(f"{"Length":<12}: {len(password)} ✓ ")
    return suggestion

def upper_letters(s):
    upper = 0
    suggestion = ""
    for i in s:
        if i.isalpha():
            if i == i.upper():
                upper += 1
    if upper >0:
        print(f"{"Uppercase":<12}: {upper} ✓")
    else:
        print(f"{"Uppercase":<12}: {upper} ✗")
        suggestion = "Password must contain atleast one 'Uppercase' character."
    return suggestion
