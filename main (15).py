# from csv_lab1 import csv_to_list
# def show_product(Id):
#     list = csv_to_list('p.csv')
#     return list[Id]
#
# while True:
#     print("1---show to all products")
#     print("2--quit")
#     menu = int(input("enter your choice: "))
#     if menu == 2:
#         break
#     if menu == 1:
#         file_name = 'p.csv'
#         data = csv_to_list(file_name)
#         for row in data:
#             print("-" * 39)
#             print(row)
#     else:
#         break
#     while True:
#         buy = int(input("Do you want to buy (1-yes/2-no): "))
#         count_products = 0
#         if buy == 2:
#             break
#         elif buy == 1:
#             buy_product = int(input("enter product ID: "))
#             count_products += 1
#             product = (show_product(buy_product))
#             amount = float(input(f"How much kg {(product)[1]} do you want to buy? "))
#             if amount > float(product[3]):
#                 print(f"Sorry we don't have enough and we have only {product[3]} kg {product[1]}")
#             elif amount <= float(product[3]):
#                 total_price = amount*float(product[2])
#                 print(f"Your {product[1]}'s total price is ${total_price}")
#         stop = int(input("if you want to stop (1-yes/2-no): "))
#         if stop == 1:
#             check = int(input("Do you want to check (1-yes/2-no): "))
#             if check == 2:
#                 break
#             elif check == 1:
#                 print(f" {'-'*40}\n{count_products} products is bougth"
#                         f"\nAll--PRODUCTS\n Name: {product[1]} | Amount:{amount} | Price: ${total_price}\n")


from csv_lab1 import csv_to_list
def show_product(Id):
    products = csv_to_list('p.csv')
    return products[Id]
# import numpy as np

name_p = []
price_p = []
quantity_p = []
price = []
while True:
    print("1 - Show all products")
    print("2 - Quit")
    menu = int(input("Enter your choice: "))
    if menu == 2:
        break
    elif menu == 1:
        file_name = 'p.csv'
        data = csv_to_list(file_name)
        for row in data:
            print("-" * 39)
            print(row)
        print('-'*39)
        buy = int(input("Do you want to buy (1-yes/2-no): "))
        if buy == 2:
            break
        elif buy == 1:
            count_products = 0
            while True:
                buy_product = int(input("Enter product ID (or -1 to finish): "))
                if buy_product == -1:
                    break
                count_products += 1
                product = show_product(buy_product)
                price.append(product[2])
                name_p.append(product[1])
                amount = float(input(f"How much kg of {product[1]} do you want to buy? "))
                quantity_p.append(amount)
                if amount > float(product[3]):
                    print(f"Sorry, we don't have enough. We only have {product[3]} kg of {product[1]}.")
                else:
                    total_price = amount * float(product[2])
                    print(f"Your total price for {amount} kg of {product[1]} is ${total_price}")
                    price_p.append(total_price)
            print(f"You bought {count_products} products in total.")
            check = int(input("Do you want to check out (1-yes/2-no): "))
            if check == 2:
                break
            elif check == 1:
                print('-' * 40)
                all_price = 0
                for a, b, c, d in zip(name_p, price_p, quantity_p, price):
                    print(f"\t\t\tPRODUCT\nPRODUCT NAME: {a} | PRODUCT PRICE: ${d} | QUANTITY: {c}|  PRICE: ${b}")

                    product_total_price = b * c
                    all_price += product_total_price
                print(f"TOTAL PRICE: ${all_price}")
                print('-' * 40)
                break

user = input("Do you want to add a new product? (y/n): ")
if user == "y":
    import csv
    def add_csv(Pr_id, Products, Price, Quantity):
        with open("p.csv", 'a', newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([Pr_id, Products, Price, Quantity])
    Pr_id = input("enter new product ID: ")
    Products = input("Enter new product name: ")
    Price = float(input("Enter price of new product: "))
    Quantity = float(input("Enter quantity of new product: "))
    add_csv(Pr_id, Products, Price, Quantity)
elif user == "n":
    user = input("Do you want to change product? (y/n): ")
    if user == "y":
        def write_csv(data):
            with open('p.csv', 'w', newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(data)
        def change_csv(row_index, col_index):
            data = csv_to_list('p.csv')
            if 0 <= row_index < len(data) and 0 <= col_index < len(data[0]):
                current_value = data[row_index][col_index]
                new_value = input("enter new value: ")
                data[row_index][col_index] = new_value
            write_csv(data)
        r = int(input("enter id number: "))
        c = int(input("enter column number: "))
        change_csv(r, c)
    elif user == 'n':
        user = input("Do you want to remove product? (y/n): ")
        if user == "y":
            def write_csv(data):
                with open('p.csv', 'w', newline="") as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(data)
            def remove_csv(id_product):
                data = csv_to_list('p.csv')
                if 0 <= id_product < len(data):
                    del data[id_product]
                write_csv(data)
            id_product = int(input("enter id number:"))
            remove_csv(id_product)

        elif user == "n":
            breakpoint()






























# from csv_lab1 import csv_to_list as ctl
# def show_products(id):
#     copy_list = ctl("p.csv")
#     return copy_list[id]
# def check_quantity(quantity):
#     copy_list = ctl("p.csv")
#     return copy_list[quantity]
#
# while True:
#     print("1-show me products")
#     print("2 - quit program")
#     menu = input("Enter your choice: ")
#     if menu == "2":
#         break
#     elif menu == '1':
#         print('-'*39)
#         print('|',
#         ctl("p.csv")[0][0], '|',
#         ctl("p.csv")[0][1], '|',
#         ctl("p.csv")[0][2], '|',
#         ctl("p.csv")[0][3], '|')
#         print('-'*39)
#         counter = 1
#         for i in ctl("p.csv"):
#             if i[0] == 'Pr_id':
#                 continue
#             print('|',
#                 counter, "  ", '|',
#                 i[1], " " * (7-len(i[1])), '|',
#                 i[2], "  ", '|',
#                 i[3], " "* (7-len(i[3])), '|')
#             print('-'*39)
#             counter += 1
#             print(ctl("p.csv"))
#         user = input("do you wanna to buy any product?(1-yes/2-no)?")
#         if user == "1":
#             user_choice = int(input("enter product ID? "))
#             product = show_products(user_choice)
#             amount = int(input(f"how much do you want to buy of {product[1]}  do you want to buy? "))
#
#             if amount < check_qty(product[1]):
#                 print(f"total price: {product[1]} is {float(product[2]) * amount}$")
#             else:
#                 print("you don't have enough")
#         elif user == "2":
#             break
#
#     else:
#         break



