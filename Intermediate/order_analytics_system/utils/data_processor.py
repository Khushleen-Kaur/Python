import helper

def view_orders():
    orders_data = helper.read_data()
    print(f"{'ID':<8}{'CUSTOMER':<15}{'Spending':<10}{'Items':<12}{'DATE':<15}{'STATUS':<12}")
    print("-" * 70)

    for order in orders_data:
        spending, total_items = helper.total_by_order_id(order['order_id'])
        print(
            f"{order['order_id']:<8}",
            f"{order['customer']:<15}",
            f"{spending:<10}"
            f"{total_items:<10}"
            f"{order['order_date']:<15}"
            f"{order['status']:<12}"
        )

view_orders()

