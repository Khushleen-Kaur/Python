import helper as hel

def main():
    print("===== PASSWORD ANALYZER =====")
    password = input("Enter password: ")
    print()
    suggestion = []
    total_score = 0
    functions = [hel.analyze_length(password), hel.upper_letters(password), hel.lower_letters(password), hel.digits(password)]
    
    for fun in functions:
        suggest, score = fun
        suggestion.append(suggest)
        total_score += score

    print("\n--------------------- Final Analysis: ---------------------")
    print(f"{"Password":<20}: {password}")
    print(f"{"Score":<20}: {total_score}/10")
    hel.display(suggestion)
    print()


if __name__ == "__main__":
    main()