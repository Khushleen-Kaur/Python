import helper as hel

def main():
    print("===== PASSWORD ANALYZER =====")
    password = input("Enter password: ")
    print()
    suggestion = []
    total_score = 0
    suggest, score = hel.analyze_length(password)
    suggestion.append(suggest)
    total_score += score
    suggest, score = hel.upper_letters(password)
    suggestion.append(suggest)
    total_score += score
    suggest, score = hel.lower_letters(password)
    suggestion.append(suggest)
    total_score += score

    print("\nFinal Analysis: ")
    print(f"{"Score":<20}: {total_score}")


if __name__ == "__main__":
    main()