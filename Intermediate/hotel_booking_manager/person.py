
class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_info(self):
        print("----- Person Details -----")
        print(f"Name : {self.name}")
        print(f"Contact number : {self.phone}")

guests = set()
guest_IDs = set()
class Guest(Person):
    count = 0
    def __init__(self, name, phone):
        super().__init__(name, phone)
        Guest.count += 1
        self.guest_id = f"G00{Guest.count}"
        guests.add(self)
        guest_IDs.add(self.guest_id)

    def display_info(self):
        super().display_info()
        print(f"Guest ID : {self.guest_id}")


class Staff(Person):
    count = 0
    def __init__(self, name, phone, role):
        super().__init__(name, phone)
        Staff.count += 1
        self.staff_id = f"S00{Staff.count}"
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Staff ID : {self.staff_id}")
        print(f"Role : {self.role}")

STAFF_ROLES = [ "Manager", "Receptionist", "Housekeeper", "Chef", "Security Guard" ]
staff1 = Staff("Rahul", 7896547865, "Manager") 
staff2 = Staff("Priya", 8897747877, "Receptionist") 
staff3 = Staff("Rani", 9578627865, "Housekeeper") 
staff4 = Staff("Arnav", 9875684235, "Chef") 
staff = {staff1, staff2, staff3, staff4}

def add_guest():
    name = input("Enter person: ")
    try:
        phone = input("Enter Phone number: ")
        if len(phone) != 10 : raise ValueError()
        phone = int(phone)
    except ValueError:
        print("Please, enter a valid Phone number!")
    else:
        g = Guest(name, phone)
        print("Guest Created!")
        print(f"Guest ID: {g.guest_id}")