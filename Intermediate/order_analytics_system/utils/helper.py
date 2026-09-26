import json

order_data = {}
products = {}
cate = {}

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
            total += item["price"]*item['quantity']
            count += item['quantity']
        order_data[person["order_id"]] = {
            "total_amount" : total,
            "total_items" : count
        }
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
    
def total_products():
    data = read_data()
    total = 0
    for person in data:
        for item in person['items']:
            total += item['quantity']
            if item['category'] in products:
                if item['product'] in products[item['category']]:
                    products[item['category']][item['product']] += item['quantity']
                else:
                    products[item['category']][item['product']] = item['quantity']
            else:
                products[item['category']] = {}
                products[item['category']][item['product']] = item['quantity']

    return products, total

def frequent_product():
    max_val = 0
    max_product = ""
    for category in products:
        for product, count in products[category].items():
            if count > max_val:
                max_val = count
                max_product = product
    return max_product, max_val

def least_product():
    min_val = float('inf')
    min_product = ""
    for category in products:
        for product, count in products[category].items():
            if count < min_val:
                min_val = count
                min_product = product
    return min_product, min_val

def by_category():
    for person in read_data():
        for item in person['items']:
            if item['category'] in cate:
                cate[item['category']]['total'] += item['price']*item['quantity']
                cate[item['category']]['quantity'] += item['quantity']
            else:
                cate[item['category']] = {
                    'total' : item['price']*item['quantity'],
                    'quantity' : item['quantity']
                }
    return cate

def minmax_category():
    for x in products:
        min = float('inf')
        max = 0
        print(products)
        for heading, value  in products[x].items():
            print(heading, value)
    print("done")
        


class Choice:
    def __enter__(self):
        choice = int(input("Enter choice: "))
        return choice
    def __exit__(self, exc_type, exc, tb):
        pass

get_total()
total_products()
by_category()
if __name__ == "__main__":
    # frequent_product()
    # print(by_category())
    minmax_category()