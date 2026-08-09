#   3. ATM Simulation 


class User:
    # static :
    count = 0
    accNum = "GK15070000"

    def __init__(self):
        User.count += 1
        self.name = input("Enter Account Holder Name: ")
        self.balance = 1000
        self.accNumber = User.accNum + str(User.count)
        print("Account Created Successfully!")
        self.checkBalance()
        self.transactionHistory = []
        self.menu()

    def checkBalance(self):
        print(f"Current Balance: {self.balance}")

    def showTransactionHistory(self):
        print("\n ==== Transaction History ==== ")
        if(len(self.transactionHistory) == 0):
            print("    No transactions yet!    ")
        else:
            for i in range(len(self.transactionHistory)):
                print(f"{i+1}. {self.transactionHistory[i]}")

    def showDetails(self):
        print("\n ==== Account Details ==== ")
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.accNumber}")
        print(f"Current Balance: {self.balance}")
        self.showTransactionHistory()

    def deposit(self):
        try:
            amt = float(input("Enter amout to deposit: "))
            if(amt > 0):
                self.balance += amt
                print("Amount deposited Successfully.")
                self.transactionHistory.insert(0, f" Deposit - {amt} ")
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Please, Enter a Valid Amount to Deposit")

    def withdraw(self):
        print("NOTE: ")
        print("Account must have atleast 1000 balance.")
        print("20 rupee - withdrawal fee for withdrawal of amount more then 5,000.")

        try:
            amt = float(input("Enter amout to Withdraw: "))
            if(amt > 0):
                if(amt >= 5000):
                    amt += 20
                if(self.balance - amt > 1000):
                    self.balance -= (amt)
                    print("Amount withdrawal Successful.")
                    print("Please, Collect the cash.")
                    self.transactionHistory.insert(0, f" Withdraw - {amt} ")
                else:
                    print("Insufficient Balance.")
            else:
                print("Please, Enter a valid Amount!")
        except ValueError:
                print("Please, Enter a valid Amount for Withdrawal!")


    def menu(self):
        choice = 7
        while(choice != 6):
            print("\n ===== ATM ===== ")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Account Details")
            print("6. Exit")
            choice = int(input("Enter choice: "))

            match(choice):
                case 1:
                    self.checkBalance()
                                
                case 2:
                    self.deposit()

                case 3:
                    self.withdraw()

                case 4:
                    self.showTransactionHistory()

                case 5:
                    self.showDetails()

                case 6:
                    print("Thank you for visiting!")
                    pass

                case _:
                    print("Please, Enter a valid choice.")

def main():
    i = 1
    users = {}

    print("\n ==== Welcome to Khushleen's Bank ==== ")
    while(True):
        print("\n1. Create a New Account")
        print("2. Already Have a Account")
        print("3. Exit")

        choice = int(input("Enter choice: "))
        match(choice):
            case 1:
                users[f"GK15070000{i}"] = User()
                i += 1
            case 2:
                accNo = input("Enter Account Number: ")
                if accNo in users:
                    users[accNo].menu()
                else:
                    print("Account not found!")

            case 3:
                break
            case _ :
                print("Please, Enter a valid choice")

main()