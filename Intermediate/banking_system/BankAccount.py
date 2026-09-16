# Banking system using OOPs
class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, account_holder, account_type, balance):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = balance
    
    def deposit(self):
        try:
            amt = int(input("Enter amount to deposit: "))
            if amt <= 0 : raise ValueError("Deposit amount must be greater than 0.")
        except ValueError as e: 
            print("Error:",e)
        else:
            self.__balance += amt
            print(f"{amt} deposited successfully!")
    
    def withdrawal(self):
        try:
            amt = int(input("Enter amount to withdraw: "))
            if amt < 100 : raise ValueError("Amount must be atleast ₹100.")
            if self.__balance - amt < 1000: raise ValueError("Insufficient Balance.")
        except ValueError as e:
            print("Error:", e)
        else:
            self.__balance -= amt
            print(f"{amt} withdrawal successfully!")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        try:
            if amount < 0: raise ValueError("Balance Cannot be Negative.")
        except ValueError as e:
            print("Error:", e)
        else:
            self.__balance = amount

    def menu(self):
        while(True):
            print("\n======== Bank Account ==========")
            print("1. Deposit")
            print("2. Withdrawal")
            print("3. Balance")
            print("4. Exit")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Please, enter a valid choice.")
            else:
                if choice == 4:
                    print("Exiting...")
                    break
                match choice : 
                    case 1:
                        self.deposit()
                    case 2:
                        self.withdrawal()
                    case 3:
                        self.show_balance()
                    case _:
                        print("Please, Enter a valid choice!")


if __name__ == "__main__":
    c1 = BankAccount("Gopikrishna Mahalingam", "Savings", 500000)
    c1.menu()

