
class Person:

    def __init__(self):
        self.name = input("Enter person: ")
        try:
            self.age = int(input("Enter age: "))
            if self.age < 1 : raise ValueError()
        except ValueError as e:
            print("Please, enter a valid age!")

    def display_info(self):
        print("----- Person Details -----")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        

class Passenger(Person):
    count = 0
    def __init__(self):
        super().__init__()
        count += 1
        self.passenger_id = count
        try:
            self.phone = input("Enter Phone number:")
            if len(self.phone) == 10 : raise ValueError()
            self.phone = int(self.phone)
        except ValueError:
            print("Please, enter a valid Phone number!")

    def display_info(self):
        super().display_info()
        print(f"Passenger ID : {self.passenger_id}")
        print(f"Contact Number : {self.phone}")
        

class Staff(Person):
    count = 0
    def __init__(self):
        super().__init__()
        count += 1
        self.employee_id = count
        self.role = input("Enter your role:")

    def display_info(self):
        super().display_info()
        print(f"Employee ID : {self.employee_id}")
        print(f"Role : {self.role}")


