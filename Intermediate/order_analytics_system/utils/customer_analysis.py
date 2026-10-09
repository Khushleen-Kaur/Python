from utils import helper as hel
import main
from rich import print
from rich.console import Console

console = Console()
data = hel.read_data()
customer_order_detail = []

def total_price(id):
    total = 0
    products = 0
    orders = 0
    for person in data:
        if person['order_id'] == id:
            orders += 1
            for x in person['items']:
                total += x['price']*x['quantity']
                products += x['quantity']
            return total, products, orders

def analysis():
    for person in data:
        total, items, orders = total_price(person['order_id'])
        customer_order_detail.append((person['customer'], items, orders, total))

def view_analysis():
    print("\n[bold #9A9AEB]------ Customer Order details ------[/bold #9A9AEB]")
    print(f"[bold #CCCCFF]{"Name":<20} - {"Items":<5} - {"Orders":<6} - {"Total (₹)"}[/bold #CCCCFF]")
    for i in customer_order_detail:
        print(f"[not bold #E6E6E6]{i[0]:<20} -   {i[1]:<3} -   {i[2]:<4} - ₹{i[3]}[/not bold #E6E6E6]")


def top_customers():
    top_customer_list = customer_order_detail.copy()
    top_customer_list.sort(key=lambda person: person[3], reverse=True)
    print("\n[bold #9A9AEB]------ Top 3 Customer Order details ------[/bold #9A9AEB]")
    print(f"[bold #CCCCFF]{"Name":<20} - {"Items":<5} - {"Orders":<6} - {"Total (₹)"}[/bold #CCCCFF]")
    for i in range(3):
        print(f"[not bold #E6E6E6]{top_customer_list[i][0]:<20} -   {top_customer_list[i][1]:<3} -   {top_customer_list[i][2]:<4} - ₹{top_customer_list[i][3]}[/not bold #E6E6E6]")


def top_10_customers():
    top_customer_list = customer_order_detail.copy()
    top_customer_list.sort(key=lambda person: person[3], reverse=True)
    print("\n[bold #9A9AEB]------ Top 10 Customer Order details ------[/bold #9A9AEB]")
    print(f"[bold #CCCCFF]{"Name":<20} - {"Items":<5} - {"Orders":<6} - {"Total (₹)"}[/bold #CCCCFF]")
    for i in range(min(10, len(customer_order_detail))):
        print(f"[not bold #E6E6E6]{top_customer_list[i][0]:<20} -   {top_customer_list[i][1]:<3} -   {top_customer_list[i][2]:<4} - ₹{top_customer_list[i][3]}[/not bold #E6E6E6]")


def customer_menu():
    while(True):
        print("\n[bold #9A9AEB]========== Customer Analysis ==========[/bold #9A9AEB]")
        print("[not bold #E6E6E6]1. View Customers[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]2. Top 3 Customers[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]3. Top 10 Customers[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]4. Back[/not bold #E6E6E6]")
        try:
            with hel.Choice() as choice:
                if choice == 4:
                    print("[italic #FF5C5C]Moving to main...[/italic #FF5C5C]")
                    break
                match choice:
                    case 1:
                        view_analysis()
                    case 2:
                        top_customers()
                    case 3:
                        top_10_customers()
                    case _:
                        print("[italic #FF5C5C]Please, Enter a choice between (1 - 4).[/italic #FF5C5C]")
        except ValueError:
            print("[italic #FF5C5C]Please, Enter a valid choice.[/italic #FF5C5C]") 


analysis()
if __name__ == "__main__":
    customer_menu()
    pass