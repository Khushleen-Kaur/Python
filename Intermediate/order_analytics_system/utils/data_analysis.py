from utils import helper as hel
from datetime import date,datetime
import main
from rich import print

data = hel.read_data()
def todays_order():

    order_id = list(filter(lambda x: datetime.strptime(x["order_date"], "%Y-%m-%d").date() == date.today(), data))
    print("\n[italic bold #9A9AEB]------------ Today's Order Analysis ------------[/italic bold #9A9AEB]")
    print(f"[not bold #E6E6E6]Date: {date.today()}[/not bold #E6E6E6]")
    print(f"[bold #CCCCFF]{"Order ID":<10}   {"Customer Name":<15}   {"Status":<10}[/bold #CCCCFF]")
    print('-'*45)
    if len(order_id) == 0: print("[italic #FF5C5C]No Orders Found![/italic #FF5C5C]")
    for person in order_id:
        print(f"[not bold #E6E6E6]{person['order_id']:<10} - {person['customer']:<15} - {person['status']:<10}[/not bold #E6E6E6]")

def this_months_order():
    this_month = date.today().month
    this_year = date.today().year

    order_id = list(filter(lambda x:
        datetime.strptime(x["order_date"], "%Y-%m-%d").date().month == this_month
        and
        datetime.strptime(x["order_date"], "%Y-%m-%d").date().year == this_year
        , data
    ))
    print("\n[italic bold #9A9AEB]------------ This Month's Order Analysis ------------[/italic bold #9A9AEB]")
    print(f"[not bold #E6E6E6]Month / Year: {this_month} / {this_year} [/not bold #E6E6E6]")
    print(f"[bold #CCCCFF]{"Order ID":<10}   {"Customer Name":<15}      {"Date":<7}   {"Status":<10}[/bold #CCCCFF]")
    print('-'*55)
    if len(order_id) == 0: print("[italic #FF5C5C]No Orders Found![/italic #FF5C5C]")
    for person in order_id:
        print(f"[not bold #E6E6E6]{person['order_id']:<10} - {person['customer']:<15} - {person['order_date']:<10} - {person['status']:<10}[/not bold #E6E6E6]")

def order_between():
    start_date = input("Enter start date: ")
    end_date = input("Enter end date: ")
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    order_id = list(filter(lambda x:
        datetime.strptime(x["order_date"], "%Y-%m-%d").date() >= start_date
        and
        datetime.strptime(x["order_date"], "%Y-%m-%d").date() <= end_date,
        data
    ))
    print("\n[italic bold #9A9AEB]------ Order Bewtween ------[/italic bold #9A9AEB]")
    print(f"[not bold #E6E6E6]Start date: {start_date}[/not bold #E6E6E6]")
    print(f"[not bold #E6E6E6]End date: {end_date}[/not bold #E6E6E6]")
    print(f"[bold #CCCCFF]{"Order ID":<10}   {"Customer Name":<15}     {"Date":<12}   {"Status":<10}[/bold #CCCCFF]")
    print('-'*55)
    if len(order_id) == 0: print("[italic #FF5C5C]No Orders Found![/italic #FF5C5C]")
    for person in order_id:
        print(f"[not bold #E6E6E6]{person['order_id']:<10} - {person['customer']:<15} - {person['order_date']:<12} - {person['status']:<10}[/not bold #E6E6E6]")



def data_menu():
    while(True):
        print("\n[italic bold #9A9AEB]========== Customer Analysis ==========[/italic bold #9A9AEB]")
        print("[not bold #E6E6E6]1. Today's Orders[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]2. This Month's Orders[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]3. Orders Between[/not bold #E6E6E6]")
        print("[not bold #E6E6E6]4. Back[/not bold #E6E6E6]")
        try:
            with hel.Choice() as choice:
                if choice == 4:
                    print("[italic #FF5C5C]Moving to main...[/italic #FF5C5C]")
                    break
                match choice:
                    case 1:
                        todays_order()
                    case 2:
                        this_months_order()
                    case 3:
                        order_between()
                    case _:
                        print("[italic #FF5C5C]Please, Enter a choice between (1 - 4).[/italic #FF5C5C]")
        except ValueError:
            print("[italic #FF5C5C]Please, Enter a valid choice.[/italic #FF5C5C]") 

if __name__ == "__main__":
    data_menu()
    pass