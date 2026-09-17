import person
import room 

class Booking:
    count = 0
    bookings = set()
    bookings_id = set()

    def __init__(self):
        self.guest = input("Enter guest ID : ")
        if self.guest not in person.guest_IDs:
            print("Guest not Found!")
            return 
        
        self.room_no = input("Enter Room Number : ")
        if self.room_no not in room.room_nos:
            print("Room not Found!")
            return 
        
        for r in room.rooms:
            if self.room_no == r.room_number:
                if r.is_available ==  "Booked":
                    print("Room is not available!")
                    return
                
        try:
            self.days = int(input("Enter number of days: "))
        except ValueError:
            print("Please, enter a valid number!")

        Booking.count += 1
        self.booking_id = f"B00{Booking.count}"
        room.book_room(self.room_no, "Booked")
        print("Booking successful.")
        print(f"Booking ID: {self.booking_id}")

        Booking.bookings.add(self)
        Booking.bookings_id.add(self.booking_id)

    def calculate_bill(self):
        price = 0
        for r in room.rooms:
            if r.room_number == self.room_no:
                price = r.calculate_price()
        price *= self.days
        return price
