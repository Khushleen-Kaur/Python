import booking as b
import room 

def display_booking():
    print("------ Booking Details ------")
    if len(b.Booking.bookings) == 0:
        print("No Bookings yet.")
    else:
        for book in b.Booking.bookings:
            print(book.booking_id)
            print(f"Guest ID: {book.guest}")
            print(f"Room number: {book.room_no}")
            print(f"Stay duration (days): {book.days}")
            print(f"Total amount: {book.calculate_bill()}\n")

def checkout():
    id = input("Enter Booking ID : ")
    if id not in b.Booking.bookings_id:
        print("Booking not Found!")
        return 
    booking_to_remove = None
    for r in b.Booking.bookings:
        if id == r.booking_id:
            print("------ Final Bill ------")
            print(r.booking_id)
            print(f"Guest ID: {r.guest}")
            print(f"Room number: {r.room_no}")
            print(f"Stay duration (days): {r.days}")
            print("Checkout successfully!")
            room.book_room(r.room_no, "Available")
            print(f"Room {r.room_no} is available.")
            booking_to_remove = r
            break
    if booking_to_remove:
        b.Booking.bookings.remove(booking_to_remove)
        b.Booking.bookings_id.remove(booking_to_remove.booking_id)

def cancel_booking():
    id = input("Enter Booking ID : ")
    if id not in b.Booking.bookings_id:
        print("Booking not Found!")
        return 
    booking_to_remove = None
    for r in b.Booking.bookings:
        if id == r.booking_id:
            print("------ Canceling Booking ------")
            print(r.booking_id)
            print(f"Guest ID: {r.guest}")
            print(f"Room number: {r.room_no}")
            print(f"Stay duration (days): {r.days}")
            print("Booking Cancelled!")
            room.book_room(r.room_no, "Available")
            print(f"Room {r.room_no} is available.")
            booking_to_remove = r
            break
    if booking_to_remove:
        b.Booking.bookings.remove(booking_to_remove)
        b.Booking.bookings_id.remove(booking_to_remove.booking_id)

def extend_booking():
    id = input("Enter Booking ID : ")
    if id not in b.Booking.bookings_id:
        print("Booking not Found!")
        return 
    try:
        extend_days = int(input("Enter number of days to extend: "))
    except ValueError:
        print("Please, enter valid number of days.")

    for r in b.Booking.bookings:
        if id == r.booking_id:
            print("------ Extending Booking ------")
            print(r.booking_id)
            print(f"Guest ID: {r.guest}")
            print(f"Room number: {r.room_no}")
            r.days += extend_days
            print(f"New stay duration (days): {r.days}")
            print("Booking extended successfully!")

def book_room():
    r = b.Booking()