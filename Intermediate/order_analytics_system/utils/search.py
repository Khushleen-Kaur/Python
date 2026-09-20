# from rich import print
import helper
# search by customer_name, order_id 

def completed_orders():
    data = helper.read_data()
    print("\nList of Completed Orders:")
    print(f"{'ID':<10}{'CUSTOMER':<15}{'Amount':<10}{'DATE':<15}")
    print("-" * 50)
    for person in data:
        if person["status"] == "Completed":
            print(
                f"{person['order_id']:<10}"
                f"{person['customer']:<15}"
                f"₹{helper.order_data[person['order_id']]['total_amount']:<10}"
                f"{person['order_date']:<15}"
            )

    print(f"Total completed orders: {helper.count_order()[0]}")

def cancelled_orders():
    data = helper.read_data()
    print("\nList of Cancelled Orders:")
    print(f"{'ID':<10}{'CUSTOMER':<15}{'Amount':<10}{'DATE':<15}")
    print("-" * 50)
    for person in data:
        if person["status"] == "Cancelled":
            print(
                f"{person['order_id']:<10}"
                f"{person['customer']:<15}"
                f"₹{helper.order_data[person['order_id']]['total_amount']:<10}"
                f"{person['order_date']:<15}"
            )
    print(f"Total Cancelled Orders: {helper.count_order()[1]}")

def pending_orders():
    data = helper.read_data()
    print("\nList of Pending Orders:")
    print(f"{'ID':<10}{'CUSTOMER':<15}{'Amount':<10}{'DATE':<15}")
    print("-" * 50)
    for person in data:
        if person["status"] == "Pending":
            print(
                f"{person['order_id']:<10}"
                f"{person['customer']:<15}"
                f"₹{helper.order_data[person['order_id']]['total_amount']:<10}"
                f"{person['order_date']:<15}"
            )
    print(f"Total Cancelled Orders: {helper.count_order()[2]}")

def orders_by_customers():
    orders_placed = {}
    data = helper.read_data()
    for person in data:
        if person['customer'] in orders_placed:
            orders_placed[person['customer']] += 1
        else:
            orders_placed[person['customer']] = 1
    print("\nOrders by Customers:")
    print(f"{'Customer':<20}{'Orders Placed':<20}")
    print('-' * 40)
    for i in orders_placed:
        print(
            f"{i:<20}"
            f"{orders_placed[i]:<20}"
        )

def orders_by_amount():
    try:
        amount = int(input("\nEnter amount for filter : "))
    except ValueError:
        print("Please, enter valid number.")
    print(f"{'ID':<10}{'CUSTOMER':<15}{'Amount':<10}{'DATE':<15}")
    print("-" * 50)
    count = 0
    for person in helper.read_data():
        if helper.order_data[person['order_id']]['total_amount'] >= amount:
            count += 1
            print(
                f"{person['order_id']:<10}"
                f"{person['customer']:<15}"
                f"₹{helper.order_data[person['order_id']]['total_amount']:<10}"
                f"{person['order_date']:<15}"
            )
    print(f"Total {count} customers above ₹{amount}")

def search_menu():
    while(True):
        print("\n========== Search / Filter Orders ==========")
        print("1. Completed Orders")
        print("2. Cancelled Orders")
        print("3. Pending Orders")
        print("4. Orders by Customer")
        print("5. Orders by Amount")
        print("6. Back")
        try:
            with helper.Choice() as choice:
                if choice == 6:
                    break
                match choice:
                    case 1:
                        completed_orders()
                    case 2:
                        cancelled_orders()
                    case 3:
                        pending_orders()
                    case 4:
                        orders_by_customers()
                    case 5:
                        orders_by_amount()
                    case _:
                        print("Please, Enter a choice between (1 - 6).")
        except ValueError:
            print("Please, Enter a valid choice.") 



if __name__ == "__main__":
    search_menu()