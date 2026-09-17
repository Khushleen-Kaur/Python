import person as p

STAFF_ROLES = [ "Manager", "Receptionist", "Housekeeper", "Chef", "Security Guard" ]

staff1 = p.Staff("Rahul", 7896547865, "Manager") 
staff2 = p.Staff("Priya", 8897747877, "Receptionist") 
staff3 = p.Staff("Rani", 9578627865, "Housekeeper") 
staff4 = p.Staff("Arnav", 9875684235, "Chef") 

guest1 = p.Guest("Gopikrishna Mahalingam", 7896547865) 
guest2 = p.Guest("Chrono CR7", 8897747877) 

def add_person():
    name = input("Enter person: ")
    try:
        phone = input("Enter Phone number: ")
        if len(phone) != 10 : raise ValueError()
        phone = int(phone)
    except ValueError:
        print("Please, enter a valid Phone number!")
    else:
        return name, phone

def add_guest():
    name , phone = add_person()
    g = p.Guest(name, phone)
    print("Guest Created!")
    print(f"Guest ID: {g.guest_id}")


def add_staff():
    name , phone = add_person()
    print("Select a role from the options below:")
    for x, i in enumerate(STAFF_ROLES):
        print(f"{x+1}. {i}")
    try:
        role = int(input("Enter prefered role: "))
        s = p.Staff(name, phone, STAFF_ROLES[role])
        print(f"Staff - {STAFF_ROLES[role-1]} Enrolled successfully.")
        print(f"Staff ID: {s.staff_id}")
    except ValueError:
        print("Please, enter a valid number.")
    except IndexError:
        print("Please, enter a correct choice.")


def view_guests():
    for guest in p.guests:
        guest.display_info()

def view_staff():
    for s in p.Staff.staff:
        s.display_info()
