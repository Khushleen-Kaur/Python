import helper as hel

data = hel.read_data()

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
    print("------ Customer Order details ------")
    print(f"{"Name":<10} - {"Items":<5} - {"Orders":<6} - {"Total (₹)"}")
    for person in data:
        total, items, orders = total_price(person['order_id'])
        print(f"{person['customer']:<10} -   {items:<3} -   {orders:<4} - ₹{total}")

if __name__ == "__main__":
    analysis()
# print(data)