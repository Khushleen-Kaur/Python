import helper as hel

data = hel.read_data()

def total_price(id):
    total = 0
    for person in data:
        if person['order_id'] == id:
            for x in person['items']:
                total += x['price']*x['quantity']
            return total

def analysis():
    for person in data:
        print(f"{person['customer']} - {total_price(person['order_id'])}")

if __name__ == "__main__":
    analysis()
# print(data)