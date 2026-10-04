import helper as hel
import rules 

def check_password():
    print("\n===== PASSWORD ANALYZER =====")
    password = input("Enter password: ")
    print()
    suggestion = []
    total_score = 0

    suggest, score = hel.common_passwords(password)
    suggestion.append(suggest)
    total_score += score

    if score != 0:
        functions = [hel.analyze_length(password), hel.upper_letters(password), hel.lower_letters(password), hel.digits(password), hel.special_characters(password)]
        
        for fun in functions:
            suggest, score = fun
            suggestion.append(suggest)
            total_score += score

    print("\n--------------------- Final Analysis: ---------------------")
    print(f"{"Password":<20}: {"*"*len(password)}")
    print(f"{"Score":<20}: {total_score}/10")
    hel.display(suggestion)
    print()

def main():
    print("\n========== Password ==========")
    print("1. Rules for strong password")
    print("2. Check Strength")
    try:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                rules.rules()
            case 2:
                check_password()
            case _ :
                print("Please, Enter a valid choice.\n")
                main()

    except ValueError:
        print("Please, Enter a valid number choice.")
        main()


if __name__ == "__main__":
    main()