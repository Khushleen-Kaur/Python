
import room as Room
import person_methods as pm
import booking_methods as bm
import hotel_analysis as ha

def menu():
    while(True):
        print("\n======= Hotel Manager ========")
        print("1. View Rooms")
        print("2. View Guests")
        print("3. Add Guest")
        print("4. Book Room")
        print("5. View Bookings")
        print("6. Extend stay")
        print("7. Cancel Booking")
        print("8. Checkout")
        print("9. Add Staff")
        print("10. View Staff")
        print("11. Hotel Analysis")
        print("12. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please, enter a  valid choice!")
        else:
            if choice == 12:
                print("Exiting...")
                break

            match choice:
                case 1:
                    Room.room_details()
                case 2:
                    pm.view_guests()
                case 3:
                    pm.add_guest()
                case 4:
                    bm.book_room()
                case 5:
                    bm.display_booking()
                case 6:
                    bm.extend_booking()
                case 7:
                    bm.cancel_booking()
                case 8:
                    bm.checkout()
                case 9:
                    pm.add_staff()
                case 10:
                    pm.view_staff()
                case 11:
                    ha.show_analysis()
                case _:
                    print("Please, Enter a valid choice.")


if __name__ == "__main__":
    menu()