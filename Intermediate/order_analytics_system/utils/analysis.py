from utils import data_analysis as da
from utils import helper as hel
from utils import customer_analysis as ca
from utils import search as s
from rich import print
from rich.console import Console

console = Console()
# (Revenue by Category (Category name - price - items sold) + most popular, least popular

def sales_analysis():
    print("\n[bold #9A9AEB]---------- Sales Analysis ----------[/bold #9A9AEB]")
    print(f"{"Total Orders":<20}:[not bold #F5F5FF] {hel.count_order()[3]}[/not bold #F5F5FF]")
    print(f"{"Completed Orders":<20}:[not bold #F5F5FF] {hel.count_order()[0]}[/not bold #F5F5FF]")
    print(f"{"Cancelled Orders":<20}:[not bold #F5F5FF] {hel.count_order()[1]}[/not bold #F5F5FF]")
    print(f"{"Pending Orders":<20}:[not bold #F5F5FF] {hel.count_order()[2]}[/not bold #F5F5FF]")
    print(f"\n{"Total Revenue":<20}:[not bold #F5F5FF] ₹{hel.total_revenue()}[/not bold #F5F5FF]")
    print(f"{"Average Order Value":<20}:[not bold #F5F5FF] ₹{hel.total_revenue()/hel.count_order()[3]}[/not bold #F5F5FF]")
    print(f"{"Highest Order":<20}:[not bold #F5F5FF] {hel.highest_order()}[/not bold #F5F5FF]")
    print(f"{"Lowest Order":<20}:[not bold #F5F5FF] {hel.lowest_order()}[/not bold #F5F5FF]")
    print(f"\n{"Total Products sold":<20}:[not bold #F5F5FF] {hel.total_products()[1]} products[/not bold #F5F5FF]")
    print(f"{"Mostly buyed product":<20}:[not bold #F5F5FF] Frequency - {hel.frequent_product()[1]/2}[/not bold #F5F5FF]")
    print(f"{"Names":<20}:[not bold #F5F5FF] {hel.frequent_product()[0]}[/not bold #F5F5FF]")
    print(f"{"Least buyed product":<20}:[not bold #F5F5FF] Frequency - {hel.least_product()[1]/2}[/not bold #F5F5FF]")
    print(f"{"Names":<20}:[not bold #F5F5FF] {hel.least_product()[0]}[/not bold #F5F5FF]")

    print("\n[#9A9AEB]----- Sales Analysis Complete -----[/#9A9AEB]\n")

def category_analysis():
    print("\n[bold #9A9AEB]-------- Category Analysis --------[/bold #9A9AEB]")
    print(f"Revenue by Category:")
    data = hel.by_category()
    print(f"[bold #CCCCFF]{"Category":<12}  {'Revenue':<7}  {'Quantity'}[/bold #CCCCFF]")
    print("[bold #CCCCFF]-[/bold #CCCCFF]"*35)
    for x in data:
        print(f"[not bold #E6E6E6]{x:<12} - ₹{data[x]['total']:<7} - {data[x]['quantity']}[/not bold #E6E6E6]")
    print(f"\n{"Mostly buyed product":<20}:[not bold #E6E6E6]  Frequency - {hel.frequent_product()[1]}[/not bold #E6E6E6] ")
    print(f"{"Names":<20}:[not bold #E6E6E6]  {hel.frequent_product()[0]}[/not bold #E6E6E6] ")
    print(f"{"Least buyed product":<20}:[not bold #E6E6E6]  Frequency - {hel.least_product()[1]}[/not bold #E6E6E6] ")
    print(f"{"Names":<20}:[not bold #E6E6E6]  {hel.least_product()[0]}[/not bold #E6E6E6] ")

    print("\n[#9A9AEB]----- Category Analysis Complete -----[#9A9AEB]\n")

def customer_analysis():
    ca.customer_menu()

def time_analysis():
    da.data_menu()

def search():
    s.search_menu()

def view_orders():
    orders_data = hel.read_data()
    print("\n[bold #9A9AEB]-------------------------- Order Details ---------------------------[/bold #9A9AEB]")
    print(f"[bold #CCCCFF]{'ID':<8}{'CUSTOMER':<15}{'Amount':<10}{'Items':<12}{'DATE':<15}{'STATUS':<12}[/bold #CCCCFF]")
    print("[bold #CCCCFF]-[/bold #CCCCFF]" * 70)

    for order in orders_data:
        print(
            f"[not bold #E6E6E6]{order['order_id']:<8}[/not bold #E6E6E6]",
            f"[not bold #E6E6E6]{order['customer']:<15}[/not bold #E6E6E6]",
            f"[not bold #E6E6E6]₹{hel.order_data[order['order_id']]['total_amount']:<10}[/not bold #E6E6E6]"
            f"[not bold #E6E6E6]{hel.order_data[order['order_id']]['total_items']:<10}[/not bold #E6E6E6]"
            f"[not bold #E6E6E6]{order['order_date']:<15}[/not bold #E6E6E6]"
            f"[not bold #E6E6E6]{order['status']:<12}[/not bold #E6E6E6]"
        )


if __name__ == "__main__":
    # sales_analysis()
    # category_analysis()
    # customer_analysis()
    pass