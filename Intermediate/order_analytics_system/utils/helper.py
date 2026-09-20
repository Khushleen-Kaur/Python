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

def count_order():
    data = read_data()
    completed = 0
    cancelled = 0
    pending = 0
    total = 0
    for person in data:
        total += 1
        if person["status"] == "Completed":
            completed += 1
        elif person["status"] == "Cancelled":
            cancelled += 1
        elif person["status"] == "Pending":
            pending += 1
    return [completed, cancelled, pending, total]

def total_revenue():
    data = read_data()
    total = 0
    for person in data:
        total += order_data[person["order_id"]]['total_amount']
    return total

def highest_order():
    data = read_data()
    max = 0
    max_customer = []
    for person in data:
        amt = order_data[person["order_id"]]['total_amount']
        if amt > max:
            max = amt
            max_customer = [person['order_id'], person['customer'], amt]
    return " - ".join([str(max_customer[0]), max_customer[1], "₹"+str(max_customer[2])]) 
    
def lowest_order():
    data = read_data()
    min = float('inf')
    min_customer = []
    for person in data:
        amt = order_data[person["order_id"]]['total_amount']
        if amt < min:
            min = amt
            min_customer = [person['order_id'], person['customer'], amt]
    return " - ".join([str(min_customer[0]), min_customer[1], "₹"+str(min_customer[2])]) 
    
# def total_products():
#     data = read_data()
#     products = {}
#     total = 0
#     for person in data:
#         for i in person['items']:
#             total += 1
#             if products[i['category']][i['product']] in products:
#                 products[i['category']][i['product']] += 1
#             else:
#                 products[i['category']][i['product']] = 1

#     return products
    
class Choice:
    def __enter__(self):
        choice = int(input("Enter choice: "))
        return choice
    def __exit__(self, exc_type, exc, tb):
        pass

get_total()

if __name__ == "__main__":
    total_products()