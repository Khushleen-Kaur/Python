#   3. ATM Simulation 

accNum = "GK15070000"
class User:
    # static :
    count = 0

    def __init__(self):
        User.count += 1
        self.name = input("\nEnter Name: ")
        self.balance = 1000
        self.accNumber = accNum + str(User.count)
        self.checkBalance()
        print()
        self.menu()

    def checkBalance(self):
        print(f"Current Balance: {self.balance}")

    def showDetails(self):
        print("\n ==== Account Details ==== ")
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.accNumber}")
        print(f"Current Balance: {self.balance}")

    def deposit(self):
        amt = float(input("Enter amout to deposit: "))
        if(amt > 0):
            self.balance += amt
            print("Amount deposited Successfully.")
        else:
            print("Please, Enter a valid Amount!")

    def withdraw(self):
        print("NOTE: Account must have atleast 1000 balance.")
        amt = float(input("Enter amout to Withdraw: "))
        if(amt > 0):
            if(self.balance - amt > 1000):
                self.balance -= amt
                print("Amount withdrawal Successful.")
                print("Please, Collect the cash.")
            else:
                print("Insufficient Balance.")
        else:
            print("Please, Enter a valid Amount!")

    def menu(self):
        choice = 6
        while(choice != 5):
            print("\n ===== ATM ===== ")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Account Details")
            print("5. Exit")
            choice = int(input("Enter choice: "))

            match(choice):
                case 1:
                    self.checkBalance()
                                
                case 2:
                    self.deposit()

                case 3:
                    self.withdraw()

                case 4:
                    self.showDetails()

                case 5:
                    pass

                case _:
                    print("Please, Enter a valid choice.")



User1 = User()