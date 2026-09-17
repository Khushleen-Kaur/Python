
import room as Room
import person as Person
import booking as Book

def main():
    while(True):
        print("\n======= Hotel Manager ========")
        print("1. View Rooms")
        print("2. Add Guest")
        print("3. Book Room")
        print("4. Cancel Booking")
        print("5. View Bookings")
        print("6. Checkout")
        print("7. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please, enter a  valid choice!")
        else:
            if choice == 7:
                break

            match choice:
                case 1:
                    Room.room_details()
                case 2:
                    Person.add_guest()
                case 3:
                    Book.book_room()
                case 4:
                    Book.cancel_booking()
                case 5:
                    Book.display_booking()
                case 6:
                    Book.checkout()
                case _:
                    print("Please, Enter a valid choice.")


if __name__ == "__main__":
    main()