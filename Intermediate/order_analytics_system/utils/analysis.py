import data_analysis as da
import helper as hel

def sales_analysis():
    print("\n------ Sales Analysis ------")
    print(f"{"Total Orders":<20}: {hel.count_order()[3]}")
    print(f"{"Completed Orders":<20}: {hel.count_order()[0]}")
    print(f"{"Cancelled Orders":<20}: {hel.count_order()[1]}")
    print(f"{"Pending Orders":<20}: {hel.count_order()[2]}")
    print(f"\n{"Total Revenue":<20}: ₹{hel.total_revenue()}")
    print(f"{"Average Order Value":<20}: ₹{hel.total_revenue()/hel.count_order()[3]}")
    print(f"{"Highest Order":<20}: {hel.highest_order()}")
    print(f"{"Lowest Order":<20}: {hel.lowest_order()}")
    print(f"\n{"Total Products sold":<20}: {hel.total_products()[1]} products")
    print(f"{"Mostly buyed product":<20}: {hel.frequent_product()[0]}, Frequency - {hel.frequent_product()[1]}")


def category_analysis():
    print("\n------ Category Analysis ------")
    print(f"Revenue by Category:")

    

def customer_analysis():
    pass

def data_analysis():
    da.data_analysis()

if __name__ == "__main__":
    sales_analysis()
    category_analysis()