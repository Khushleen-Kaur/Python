from rich import print
from utils import helper
import main
from rich.console import Console

# search by customer_name, order_id 
console = Console()

def completed_orders():
    data = helper.read_data()
    print("\n[bold italic #9A9AEB]List of Completed Orders:[/bold italic #9A9AEB]")
    print(f"[bold #CCCCFF]{'ID':<10}{'CUSTOMER':<15}{'Amount':<10}{'DATE':<15}[/bold #CCCCFF]")
    print("[bold #CCCCFF]-[/bold #CCCCFF]" * 50)
    for person in data:
        if person["status"] == "Completed":
            print(
                f"[not bold #E6E6E6]{person['order_id']:<10}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]{person['customer']:<15}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]₹{helper.order_data[person['order_id']]['total_amount']:<10}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]{person['order_date']:<15}[/not bold #E6E6E6]"
            )

    print(f"[#9A9AEB]Total completed orders: {helper.count_order()[0]}[/#9A9AEB]")

def cancelled_orders():
    data = helper.read_data()
    print("\n[bold italic #9A9AEB]List of Cancelled Orders:[/bold italic #9A9AEB]")
    print(f"[bold #CCCCFF]{'ID':<10}{'CUSTOMER':<15}{'Amount':<10}{'DATE':<15}[bold #CCCCFF]")
    print("[bold #CCCCFF]-[/bold #CCCCFF]" * 50)
    for person in data:
        if person["status"] == "Cancelled":
            print(
                f"[not bold #E6E6E6]{person['order_id']:<10}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]{person['customer']:<15}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]₹{helper.order_data[person['order_id']]['total_amount']:<10}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]{person['order_date']:<15}[/not bold #E6E6E6]"
            )
    print(f"[#9A9AEB]Total Cancelled Orders: {helper.count_order()[1]}[/#9A9AEB]")

def pending_orders():
    data = helper.read_data()
    print("\n[bold italic #9A9AEB]List of Pending Orders:[/bold italic #9A9AEB]")
    print(f"[bold #CCCCFF]{'ID':<10}{'CUSTOMER':<15}{'Amount':<10}{'DATE':<15}[/bold #CCCCFF]")
    print("[bold #CCCCFF]-[/bold #CCCCFF]" * 50)
    for person in data:
        if person["status"] == "Pending":
            print(
                f"[not bold #E6E6E6]{person['order_id']:<10}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]{person['customer']:<15}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]₹{helper.order_data[person['order_id']]['total_amount']:<10}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]{person['order_date']:<15}[/not bold #E6E6E6]"
            )
    print(f"[#9A9AEB]Total Cancelled Orders: {helper.count_order()[2]}[/#9A9AEB]")

def orders_by_customers():
    orders_placed = {}
    data = helper.read_data()
    for person in data:
        if person['customer'] in orders_placed:
            orders_placed[person['customer']] += 1
        else:
            orders_placed[person['customer']] = 1
    print("\n[bold italic #9A9AEB]Orders by Customers:[/bold italic #9A9AEB]")
    print(f"[bold #CCCCFF]{'Customer':<20} {'Orders Placed':<20}[/bold #CCCCFF]")
    print('[bold #CCCCFF]-[/bold #CCCCFF]' * 40)
    for i in orders_placed:
        print(
            f"[not bold #E6E6E6]{i:<20}[/not bold #E6E6E6]"
            f"[not bold #E6E6E6]{orders_placed[i]:<20}[/not bold #E6E6E6]"
        )

def orders_by_amount():
    try:
        amount = int(input("\nEnter amount for filter : "))
    except ValueError:
        print("Please, enter valid number.")
    print(f"[bold #CCCCFF]{'ID':<10}{'CUSTOMER':<15}{'Amount':<10}{'DATE':<15}[/bold #CCCCFF]")
    print("[bold #CCCCFF]-[/bold #CCCCFF]" * 50)
    count = 0
    for person in helper.read_data():
        if helper.order_data[person['order_id']]['total_amount'] >= amount:
            count += 1
            print(
                f"[not bold #E6E6E6]{person['order_id']:<10}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]{person['customer']:<15}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]₹{helper.order_data[person['order_id']]['total_amount']:<10}[/not bold #E6E6E6]"
                f"[not bold #E6E6E6]{person['order_date']:<15}[/not bold #E6E6E6]"
            )
    print(f"[#9A9AEB]Total {count} customers above ₹{amount}[/#9A9AEB]")

def search_menu():
    while(True):
        print("\n[bold italic #9A9AEB]========== Search / Filter Orders ==========[/bold italic #9A9AEB]")
        print("[not bold #E6E6E6]1. Completed Orders[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]2. Cancelled Orders[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]3. Pending Orders[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]4. Orders by Customer[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]5. Orders by Amount[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]6. Back[/not bold #E6E6E6]")
        try:
            with helper.Choice() as choice:
                if choice == 6:
                    print("[italic #FF5C5C]Moving to main...[italic #FF5C5C]")
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
                        print("[italic #FF5C5C]Please, Enter a choice between (1 - 6).[/italic #FF5C5C]")
        except ValueError:
            print("[italic #FF5C5C]Please, Enter a valid choice.[/italic #FF5C5C]") 



if __name__ == "__main__":
    search_menu()