
import booking
import room
import person

def available_room():
    count = 0
    for r in room.rooms:
        if r.is_available == "Available":
            count += 1
    return count

def booked_room():
    count = 0
    for r in room.rooms:
        if r.is_available == "Booked":
            count += 1
    return count

def show_analysis():
    print("-------- Hotel Analysis ---------")
    print(f"Rooms Available: {available_room()}")
    print(f"Rooms Booked: {booked_room()}")
    print(f"Total number of Guests: {person.Guest.count}")
    print(f"Total Staff members: {person.Staff.count}")

if __name__ == "__main__":
    show_analysis()