from csv_functions import csv_to_list as ctl, write_csv as wc, add_csv as ac
from datetime import datetime

def show_products(id):
    copy_list = ctl("products.csv")
    return copy_list[id]
def products_rating():
    copy_list = ctl("stats.csv")
    products = []
    result = []

    for i in copy_list:
        if i[0] != "Name" and i[1] not in products:
            products.append(i[1])

    for i in products:
        tatol_amount = 0
        for j in copy_list:
            if j[0] == "Name":
                continue
            if i == j[1]:
                total_amount += int(j[3])
        result.append([i, str(total_amount)])
    print(result)
    print("-" * 21)
    print(
        ""
    )

def show_product_csv():
    print("-" * 36)
    print(
        "|", "ID",
        "|", ctl("products.csv")[0][1],
        "|", ctl("products.csv")[0][2],
        "|", ctl("products.csv")[0][3], "|",
    )
    print("-" * 36)
    counter = 1
    for i in ctl("products.csv"):
        if i[0] == "Pr_id":
            continue
        print(
            "|", counter, "",
            "|", i[1], " " * (7 - len(i[1])),
            "|", i[2], " ",
            "|", i[3], " " * (7 - len(i[3])), "|",
        )
        counter += 1
    print("-" * 36)

def show_basket_csv():

    print("-" * 37)
    print(
        "|", ctl("basket.csv")[0][0],
        "|", ctl("basket.csv")[0][1],
        "|", ctl("basket.csv")[0][2],
        "|", ctl("basket.csv")[0][3], "|",
    )
    print("-" * 37)

    for i in ctl("basket.csv"):
        if i[0] == "products":
            continue
        print(
            "|", i[0], " " * (7 - len(i[0])),
            "|", i[1], " ",
            "|", i[2], " " * (5 - len(i[2])),
            "|", i[3], " " * (4 - len(i[3])), "|",
        )
    print("-" * 37)

# def deduct_qty():
#     produuct_csv = ctl("products.csv")
#     for i in "basket.csv":
#         if i[0] == "products":
#             continue
#         index = 0
#         for j in produuct_csv:
#             if j[1] != "Products" and i[0] == j[1]:
#                 produuct_csv[index][3] = float(j[3]) - float(i[2])
#             index += 1
#     wc("products.csv", produuct_csv)

def change_csv(id, name="not provided", price="not provided", qty="not provided"):
    copy_list = ctl("products.csv")
    status = False
    for i in copy_list:
        if i[1] == copy_list[id][1]:
            status = True
            if name != "not provided" and price != "not provided" and qty != "not provided":
                i[1] = name
                i[2] = price
                i[3] = qty
            elif name != "not provided":
                i[1] = name
            elif price != "not provided":
                i[2] = price
            elif qty != "not provided":
                i[3] = qty
    wc("products.csv", copy_list)
    return status

def delete_csv(id):
    product_info = show_products(id)
    copy_list = ctl("products.csv")
    copy_list.remove(product_info)
    wc("products.csv", copy_list)

print("1-Client")
print("2-Admin")
checker = input("choose your status: ")
if checker == "1":
    col_names = ["products", "price", "amount", "total"]
    wc("basket.csv", col_names)
    user_name = input("What is your name: ")
    while True:
        print("1-Show me products")
        print("2-Show me basket")
        print("3-Quit")
        menu = input("choose act: ")
        if menu == "1":
            show_product_csv()
            user = input("Do you want to buy anything(1-yes/2-no)?")
            if user == "1":
                products = []
                user_choice = int(input("Enter product ID? "))
                product = show_products(user_choice)
                products.append(product[1])
                amount = int(input(f"how many kgs of {product[1]} do you want to buy? "))
                if amount > float(product[3]):
                    print(f"we have only {product[3]} kgs of {product[1]}")
                else:
                    price = float(product[2]) * amount
                    prices = show_products(user_choice)[2]
                    products.append(prices)
                    products.append(str(amount))
                    total_sum = float(price) * amount
                    products.append(round(total_sum, 1))
                    ac("basket.csv", products)
                    # print(f"total price of {product[1]} is {price}$.")
                    # print(product)
            else:
                break
        elif menu == "2":
            if ctl("basket.csv")[1:]:
                show_basket_csv()
                buy_or_not = input("Do you want to buy(1-yes/2-no)? ")
                if buy_or_not == "1":
                        total = 0
                        for i in ctl("basket.csv"):
                            if i[0] == "products":
                                continue
                            total += float(i[3])
                        print(f"total price of all products: {total}$")
                        # deduct_qty()
                        current_time = datetime.now()
                        for i in ctl("basket.csv"):
                            if i[0] == "Products":
                                continue
                            stats = [user_name, i[0], i[1], i[2], i[3], current_time]
                            ac("stats.csv", stats)
            else:
                print("your basket is empty.")
        else:
            break

elif checker == "2":
    password = 10
    admin = int(input("Enter your password: "))
    while True:
        if admin == password:
            print("1 - show me products")
            print("2 - change products")
            print("3 - add products")
            print("4 - delete products")
            print("5 - show me statistics")
            print("6 - exit")
            menu = input("choose act: ")
            if menu == "1":
                show_product_csv()
            elif menu == "2":
                id = int(input("Enter ID: "))
                if change_csv(id):
                    print("ID found")
                    print("1-change everything")
                    print("2-change name")
                    print("3-change price")
                    print("4-change qty")
                    user = input("what you gonna change: ")
                    if user == "1":
                        name = input(" Enter new name: ")
                        price = input(" Enter new price: ")
                        qty = input(" Enter new qty: ")
                        change_csv(id, name, price, qty)
                    elif user == "2":
                        name = input(" Enter new name: ")
                        change_csv(id, name)
                    elif user == "3":
                        price = input(" Enter new price: ")
                        change_csv(id, price=price)
                    elif user == "4":
                        qty = input(" Enter new qty: ")
                        change_csv(id, qty=qty)
                else:
                    print("ID not found")
            elif menu == "3":
                id = input("enter id:")
                status = True
                for i in ctl("products.csv"):
                    if i[0] == id:
                        status = False
                if status:
                    name = input(" Enter new name: ")
                    price = input(" Enter new price: ")
                    qty = input(" Enter new qty: ")
                    new_product = [id, name, price, qty]
                    ac("products.csv", new_product)
                else:
                    print("id is already taken.")
            if menu == "4":
                ID = input("enter id:")
                copy_list = ctl("products.csv")
                if copy_list[ID]:
                    delete_csv(id)
                    print("Done")
                else:
                    print("ID not exists.")

            elif menu == "5":
                print("1 - Products rating in the last 7 days")
                print("2 - Customers rating in the last 7 days")
                admin_choice = input("choose act:")
                if admin_choice == "1":
                    print()
                if admin_choice == "2":
                    print()
            elif menu == "6":
                break





