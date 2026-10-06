import helper as hel

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
    print("------ Customer Order details ------")
    print(f"{"Name":<10} - {"Items":<5} - {"Orders":<6} - {"Total (₹)"}")
    for i in customer_order_detail:
        print(f"{i[0]:<10} -   {i[1]:<3} -   {i[2]:<4} - ₹{i[3]}")


def top_customers():
    top_customer_list = customer_order_detail.copy()
    top_customer_list.sort(key=lambda person: person[3], reverse=True)
    print("------ Top 3 Customer Order details ------")
    print(f"{"Name":<10} - {"Items":<5} - {"Orders":<6} - {"Total (₹)"}")
    for i in range(3):
        print(f"{top_customer_list[i][0]:<10} -   {top_customer_list[i][1]:<3} -   {top_customer_list[i][2]:<4} - ₹{top_customer_list[i][3]}")


analysis()
if __name__ == "__main__":
    # top_customers()
    # print(data)
    pass