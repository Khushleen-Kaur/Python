import json

order_data = {}

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
        order_data[person["order_id"]] = {
            "total_amount" : total,
            "total_items" : count
        }

# def total_by_order_id(id):
#     total = order_data[id]['total_amount']
#     items = order_data[id]['total_items']
#     return total, items

class Choice:
    def __enter__(self):
        choice = int(input("Enter choice: "))
        return choice
    def __exit__(self, exc_type, exc, tb):
        pass

get_total()
