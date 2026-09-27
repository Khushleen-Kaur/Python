import helper as hel

def main():
    print("===== PASSWORD ANALYZER =====")
    password = input("Enter password: ")
    print()
    suggestion = []
    suggestion.append(hel.analyze_length(passwiord))
    suggestion.append(hel.upper_letters(password))

if __name__ == "__main__":
    main()