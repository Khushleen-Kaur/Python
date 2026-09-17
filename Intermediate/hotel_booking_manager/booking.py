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
                if not r.is_available:
                    print("Room is not available!")
                    return
                
        try:
            self.days = int(input("Enter number of days: "))
        except ValueError:
            print("Please, enter a valid number!")

        Booking.count += 1
        self.booking_id = f"B00{Booking.count}"
        room.book_room(self.room_no, False)
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

def display_booking():
    print("------ Booking Details ------")
    if len(Booking.bookings) == 0:
        print("No Bookings yet.")
    else:
        for book in Booking.bookings:
            print(book.booking_id)
            print(f"Guest ID: {book.guest}")
            print(f"Room number: {book.room_no}")
            print(f"Days: {book.days}")
            print(f"Total amount: {book.calculate_bill()}\n")

def checkout():
    id = input("Enter Booking ID : ")
    if id not in Booking.bookings_id:
        print("Booking not Found!")
        return 
    booking_to_remove = None
    for r in Booking.bookings:
        if id == r.booking_id:
            print("------ Final Bill ------")
            print(r.booking_id)
            print(f"Guest ID: {r.guest}")
            print(f"Room number: {r.room_no}")
            print(f"Days: {r.days}")
            print("Checkout successful!")
            room.book_room(r.room_no, True)
            print(f"Room {r.room_no} is available.")
            booking_to_remove = r
            break
    if booking_to_remove:
        Booking.bookings.remove(booking_to_remove)



def cancel_booking():
    id = input("Enter Booking ID : ")
    if id not in Booking.bookings_id:
        print("Booking not Found!")
        return 
    booking_to_remove = None
    for r in Booking.bookings:
        if id == r.booking_id:
            print("------ Canceling Booking ------")
            print(r.booking_id)
            print(f"Guest ID: {r.guest}")
            print(f"Room number: {r.room_no}")
            print(f"Days: {r.days}")
            print("Booking Cancelled!")
            room.book_room(r.room_no, True)
            print(f"Room {r.room_no} is available.")
            booking_to_remove = r
            break
    if booking_to_remove:
        Booking.bookings.remove(booking_to_remove)



def book_room():
    r = Booking()