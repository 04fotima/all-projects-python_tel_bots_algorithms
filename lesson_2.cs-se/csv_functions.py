import csv
#reading data from csv file
def read_csv():
    with open("input.csv", "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
         print(i)
# read_csv()

#writing data to csv file
def write_csv(file_name, col_names):
    with open(file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows([col_names])
# write_csv()

# add data to csv file
def add_csv(file_name, products):
    with open(file_name, "a", newline="") as csv_file:
        csv_add = csv.writer(csv_file)
        csv_add.writerow(products)

# change data in csv file
def csv_to_list(file_name):
     copy_list = []
     with open (file_name, "r", newline="") as csv_file:
         csv_reader = csv.reader(csv_file)
         for i in csv_reader:
            copy_list.append(i)
         # print(copy_list)
     return copy_list
# csv_to_list()
def change_csv(id, name="not provided", surname="not provided", age="not provided"):
    copy_list = csv_to_list("products.csv")
    status = False
    for i in copy_list:
        if i[0] == id:
            status = True
            if name != "not provided" and surname != "not provided" and age != "not provided":
                i[1] = name
                i[2] = surname
                i[3] = age
            elif name != "not provided":
                i[1] = name
            elif surname != "not provided":
                i[2] = surname
            elif age != "not provided":
                i[3] = age
    write_csv(copy_list)
    return status
# change_csv()

#Sorting data by age
def sort_age(mode):
    copy_list = csv_to_list()
    header = copy_list[0]
    data = copy_list[1:]
    if mode == "asc":
        sort_data = sorted(data, key=lambda x: int(x[3]))
    elif mode == "desc":
        sort_data = sorted(data, key=lambda x: int(x[3]), reverse=True)

    sort_info = [header] + sort_data
    return sort_info
# sort_age()

# while True:
#     print("1-change csv")
#     print("2-Read csv")
#     print("3-Sort by age")
#     print("4-Quit")
#     menu = input("choose action: ")
#     if menu == "1":
#         id = input("enter ID(or stop): ")
#         if change_csv(id):
#             print("ID exsits.")
#             print("1-change everything")
#             print("2-change name")
#             print("3-change surname")
#             print("4-change age")
#             user = input("what you ganna change? ")
#             if user == "1":
#                 name = input("enter new name: ")
#                 surname = input("enter new surname: ")
#                 age = input("enter new age: ")
#                 change_csv(id, name, surname, age)
#             elif user == "2":
#                 name = input("enter new name: ")
#                 change_csv(id, name=name)
#             elif user == "3":
#                 surname = input("enter new surname: ")
#                 change_csv(id, surname=surname)
#             elif user == "4":
#                 age = input("enter new age: ")
#                 change_csv(id, age=age)
#             else:
#                 break
#         elif id == "stop":
#             break
#         else:
#             print("id not found")
#
#     elif menu == "2":
#         read_csv()
#     elif menu == "3":
#         print("1-Asc mode")
#         print("2-desc mode")
#         mode = input("choose mode: ")
#         if mode == "1":
#             for i in sort_age("asc"):
#                 print(i)
#         elif mode == "2":
#             for i in sort_age("desc"):
#                 print(i)
#         else:
#             break
#     else:
#         break
#
