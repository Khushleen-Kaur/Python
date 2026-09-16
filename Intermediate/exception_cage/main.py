
def divide():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"{a} / {b} = ", a/b)
    except ValueError:
        print("Please, Enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by Zero.")

def read_file():
    file_name = input("Enter filename: ")
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File Not Found!")

def access_list():
    numbers = [1,2,3,4,5]
    try:
        index = int(input("Enter index: "))
        print(f"Number at index {index} : {numbers[index]}")
    except ValueError:
        print("Please, Enter a valid number.")
    except IndexError:
        print("Please, Enter a valid index.")

def word_meaning():
    dic = {
        "Cat" : "A small, furry animal with four legs that people often keep as a pet.",
        "Run" : "To move on your feet at a speed faster than walking.",
        "Book" : "A set of printed pages held together inside a cover to read.",
        "Joy" : "A feeling of great happiness and pleasure."
    }
    word = input("Enter word: ")
    try:
        print(f"{word} : {dic[word.capitalize()]}")
    except KeyError:
        print("Please, Enter a valid word.")


def main():
    while(True):
        print("\n========== Exception Cage ==========")
        print("1. Divide Number")
        print("2. Read file")
        print("3. Access List")
        print("4. Word Meaning")
        print("5. Exit")

        try:
            choice = int(input("Enter a choice: "))
        except ValueError:
            print("Please enter a valid choice")
        else:
            if( choice == 5 ):
                print("----- Exiting -----")
                break

            match (choice):
                case 1:
                    divide()
                case 2:
                    read_file()
                case 3:
                    access_list()
                case 4:
                    word_meaning()
                case _:
                    print("Please Enter a valid choice")


if __name__ == "__main__":
    main()