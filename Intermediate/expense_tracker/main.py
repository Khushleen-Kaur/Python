# ========== EXPENSE TRACKER ==========

def is_empty():
    with open("expense.txt", "r") as file:
        data = file.read()
        if data == "":
            print("No Expenses!")
            return True
        return False
    
def add_expense():
    ex_name = input("Enter expense name: ")
    ex_amount = int(input("Enter amount: "))

    with open("expense.txt", "a") as file:
        file.write(f"\n{ex_name},{ex_amount}")
        print(f"New expense: {ex_name} - {ex_amount}")
        print("Expense Added Successfully!")

def view_expense():
    if not is_empty():
        print("\n---------- Expenses ----------")
        with open ("expense.txt", "r") as file:
            for line in file:
                name, amt = line.strip().split(",")
                print(f"{name} - {amt}")

def calculate_total():
    if not is_empty():
        with open("expense.txt", "r") as file:
            total = 0
            for line in file:
                total += int(line.strip().split(",")[1])

        return total

def min_expense():
    min_amt = float('inf')  
    with open("expense.txt", "r") as file:
        for line in file:
            name, amt = line.strip().split(",")
            amt = int(amt)
            if amt <= min_amt:
                min_amt = amt
                n = name
    return n, min_amt

def max_expense():
    max_amt = 0
    with open("expense.txt", "r") as file:
        for line in file:
            name, amt = line.strip().split(",")
            amt = int(amt)
            if amt > max_amt:
                max_amt = amt
                n = name
    return n, max_amt

def total():
    if not is_empty():
        with open("expense.txt", "r") as file:
            total = 0
            for line in file:
                total += 1
        return total

def expense_analyzer():
    if not is_empty():
        view_expense()
        print("\n------- Expenses Analyses -------")
        print("Number of Expenses:", total())
        print("Total Expense:", calculate_total())
        a, b = max_expense()
        print(f"Maximum Expenses: {a} - {b}")
        a, b = min_expense()
        print(f"Minimum Expenses: {a} - {b}")

def clear():
    with open("expense.txt", "w") as file:
        file.write("")
        print("File Clear.")


def main():
    while(True):
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Calculate total amount")
        print("4. Clear Expense")
        print("5. Highest Expense")
        print("6. Lowest Expense")
        print("7. Number of Expenses")
        print("8. Expense Analysis")
        print("9. Exit")
        try:
            choice = int(input("Enter choice: "))

            if( choice == 9):
                break

            match (choice) :
                case 1:
                    add_expense()
                case 2:
                    view_expense()
                case 3:
                    print("Total Expenses :" , calculate_total())
                case 4:
                    clear()
                case 5:
                    if not is_empty():
                        a, b = max_expense()
                        print(f"Maximum Expenses: {a} - {b}")
                case 6:
                    if not is_empty():
                        a, b = min_expense()
                        print(f"Minimum Expenses: {a} - {b}")
                case 7:
                    print("Number of Expenses:", total())
                case 8:
                    expense_analyzer()

        except ValueError:
            print("Please, Enter a valid data.")


main()
