import helper

def view_orders():
    orders_data = helper.read_data()
    print(f"{'ID':<8}{'CUSTOMER':<15}{'Amount':<10}{'Items':<12}{'DATE':<15}{'STATUS':<12}")
    print("-" * 70)

    for order in orders_data:
        print(
            f"{order['order_id']:<8}",
            f"{order['customer']:<15}",
            f"₹{helper.order_data[order['order_id']]['total_amount']:<10}"
            f"{helper.order_data[order['order_id']]['total_items']:<10}"
            f"{order['order_date']:<15}"
            f"{order['status']:<12}"
        )

view_orders()

