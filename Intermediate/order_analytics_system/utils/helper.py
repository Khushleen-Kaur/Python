import json

order_data = []

def read_data(file_name = "data/orders.json"):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data
    except:
        print("Something went wrong!")

def get_total():
    data = read_data()
    for person in data:
        total = 0
        count = 0
        for item in person["items"]:
            total += item["price"]
            count += 1
        order_data.append({
            "order_id" : person["order_id"],
            "total_spending" : total,
            "total_items" : count
        })
get_total()

def total_by_order_id(id):
    for orders in order_data:
        if orders['order_id'] == id:
            return orders['total_spending'], orders['total_items']

# print(order_data)