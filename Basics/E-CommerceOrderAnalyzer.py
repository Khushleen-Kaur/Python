  # Mini E-Commerce Order Analyzer

products = {
    "Television": 70000,
    "Laptop": 60000,
    "Phone": 30000,
    "Speaker": 10000,
    "Headphones": 3000,
    "Keyboard": 1500,
    "Tablet": 5500,
    "Smart Watch": 3550,
    "Doc": 500,
    "Mouse": 800
}

orders = [
    ("Vidhya", ["Tablet", "Keyboard"]),
    ("Khush", ["Laptop", "Mouse"]),
    ("Gopi", ["Phone", "Headphones", "Mouse"]),
    ("Krishna", ["Smart Watch", "Mouse", "Phone"]),
    ("Gopi", ["Laptop", "Keyboard"]),
    ("Khush", ["Headphones", "Keyboard"])
]

customer_total = {}


def analyze_orders(products, orders):
    print("\n========== ORDER ANALYSIS ==========\n")
    total(products, orders)
    category(customer_total)
    expensive_product(products, orders)
    unique_products(orders)
    product_frequency(orders)
    find_who(orders,products)
    expensive_products(products)


def total(products, orders):
    for i in orders:
        total = 0
        for p in i[1]:
            total = total + products[p]

        if i[0] in customer_total:
            customer_total[i[0]] += total
        else:
            customer_total[i[0]] = total

    return customer_total

def category(total):
    print("----Customer Spending----")
    for n , p in total.items():
        if p  >= 50000:
            print(f"{n} -> ₹{p} -> Premium Customer")
        elif p  >= 20000:
            print(f"{n} -> ₹{p} -> Regular Customer")
        else:
            print(f"{n} -> ₹{p} -> Budget Customer")


def expensive_product(products, orders):
    max_price = 0
    for i in orders:
        for j in i[1]:
            if max_price < products[j]:
                max_price = products[j]
                max_product = j
    print(f"\nMost expensive product purchased: \n{max_product} -> ₹{max_price}")


def unique_products(orders):
    print("\nUnique Products Purchased:")
    unique = set()
    for i in orders:
        for j in i[1]:
            unique.add(j)
    print(unique)

def product_frequency(orders):
    print("\nProduct Purchase Frequency:")
    frequency = {}
    for i in orders:
        for j in i[1]:
            if j in frequency:
                frequency[j] += 1
            else:
                frequency[j] = 1
    print(frequency)

def find_who(orders, products):
    product_name = input("\nEnter Product name: ")
    customers = set()
    if product_name not in products:
        print("Product not found!")
    else:
        print(f"Product {product_name} is purchased by: ")
        for i in orders:
            for j in i[1]:
                if j == product_name:
                    customers.add(i[0])
        if len(customers) == 0:
            print(f"No one has bought {product_name} yet.")
        else:
            print(customers)

def expensive_products(products):
    print("\nExpensive Products (price more then ₹2000) :")
    pro_dic = {}
    pro_list = []
    # for n,p in products.items():
    #     if p > 2000:
    #         pro_dic[n] = p
    #         pro_list.append(n)

    pro_dic = {n: p for n, p in products.items() if p > 2000}
    pro_list = [n for n, p in products.items() if p > 2000]

    print(pro_dic)
    print(pro_list)

analyze_orders(products, orders)

# tup = (1,2,3)
# print( tup[0] )

# print("\nCredits - Gopikrishna")