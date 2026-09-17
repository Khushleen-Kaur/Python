
class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_info(self):
        print("\n----- Person Details -----")
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
    staff = set()
    staff_IDs = set()
    def __init__(self, name, phone, role):
        super().__init__(name, phone)
        Staff.count += 1
        self.staff_id = f"S00{Staff.count}"
        self.role = role
        Staff.staff.add(self)
        Staff.staff_IDs.add(self.staff_id)

    def display_info(self):
        super().display_info()
        print(f"Staff ID : {self.staff_id}")
        print(f"Role : {self.role}")
