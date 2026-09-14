from Python.Intermediate.calculator_project.calculator import arithmetic as bas
from Python.Intermediate.calculator_project.calculator import advance as adv

print("\nYour pocket calculator, powered by Python.")
def main():
    while(True):
        print("\n==== Calculator ====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Root")
        print("8. Factorial")
        print("9. Exit")
        try:
            choice = int(input("Enter choice: "))
            
            if(choice == 9):
                print("Exiting....")
                break

            match ( choice ):
                case 1:
                    a = int(input("Enter 1st number: "))
                    b = int(input("Enter 2nd number: "))
                    print(f"{a} + {b} = {bas.add(a,b)}")
                case 2:
                    a = int(input("Enter 1st number: "))
                    b = int(input("Enter 2nd number: "))
                    print(f"{a} - {b} = {bas.sub(a,b)}")
                case 3:
                    a = int(input("Enter 1st number: "))
                    b = int(input("Enter 2nd number: "))
                    print(f"{a} x {b} = {bas.mul(a,b)}")
                case 4:
                    a = int(input("Enter 1st number: "))
                    b = int(input("Enter 2nd number: "))
                    try:
                        print(f"{a} / {b} = {bas.div(a,b)}")
                    except ZeroDivisionError:
                        print("Cannot divide by zero.")
                case 5:
                    a = int(input("Enter 1st number: "))
                    b = int(input("Enter 2nd number: "))
                    print(f"{a} % {b} = {bas.mod(a,b)}")
                case 6:
                    a = int(input("Enter base number: "))
                    b = int(input("Enter index number: "))
                    print(f"{a} ^ {b} = {adv.power(a,b)}")
                case 7:
                    a = int(input("Enter number: "))
                    print(f"√{a} = {adv.root(a)}")
                case 8:
                    a = int(input("Enter number: "))
                    print(f"Factorial of {a} = {adv.fact(a)}")

                case _ :
                    print('Please, Enter a valid choice!')

        except ValueError:
            print("Please enter a valid number")

                

if __name__ == "__main__":      
    main()