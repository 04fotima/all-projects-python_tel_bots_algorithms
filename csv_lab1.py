import csv
# function find
# for i in dir(csv):
#     print(i)

# reading data from csv file
def read_csv():
    with open("info.csv", "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
         print(i)


#writing data to csv file
def write_csv(copy_list):
    with open("info.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(copy_list)


# adding data to csv file
def add_csv(file_name, copy_list):
    with open(file_name, "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(copy_list)


# changing data to csv file
def csv_to_list(file_name):
    copy_list = []
    with open(file_name, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            copy_list.append(i)
    return copy_list


# def change_csv(id, name="not provided", surname="not provided", age="not provided"):
#     copy_list = csv_lo_list()
#     status = False
#     for i in copy_list:
#         if i[0] == id:
#             status = True
#             if name!="not provided"and surname!="not provided"and age!="not provided":
#                 i[1] = name
#                 i[2] = surname
#                 i[3] = age
#             elif name!="not provided":
#                 i[1] = name
#             elif surname!="not provided":
#                 i[2] = surname
#             elif age!="not provided":
#                 i[3] = age
#     write_csv(copy_list)
#     return status
# change_csv(id = "2", name = "asila", surname = "asia", age = 98)

#sorted data by age
# def sort_by_age(mode):
#     copy_list = csv_lo_list()
#     header = copy_list[0]
#     data = copy_list[1:]
#     # if mode == "ASC":
#     sorted_data = sorted(data, key=lambda x: int(x[3]))
    # elif mode == "DESC":
    #     sorted_data = sorted(data, key=lambda x: int(x[3]),reverse=True)
#     sorted_info = [header] + sorted_data
#     r = sorted_info
#     return r
#
# while True:
#     print("1-change csv")
#     print("2-read csv")
#     print("3-sorted by age")
#     print("4-qiut")
#     menu = input("choose act:")
#     if menu == "1":
#         id = input("enter id(or stop): ")
#         if change_csv(id):
#             print("id exist")
#             print("1-change everything")
#             print("2-change name")
#             print("3-change surname")
#             print("4-change age")
#             choice = input("choice one:")
#             if choice == "1":
#                 name = input("enter name")
#                 surname = input("enter surname")
#                 age = input("enter age")
#                 change_csv(id, name, surname, age)
#             elif choice == "2":
#                 name = input("enter name")
#                 change_csv(id, name=name)
#             elif choice == "3":
#                 surname = input("enter surname")
#                 change_csv(id,surname=surname)
#             elif choice == "4":
#                 age = input("enter age")
#                 change_csv(id, age=age)
#             else:
#                 break
#         elif id == "stop":
#             break
#         else:
#             print("id not found")
#     elif menu == "2":
#         read_csv()
#     elif menu == "3":
#         print("1-ASC mode")
#         print("2-DESC mode")
#         mode = input("enter mode:")
#         if mode == "1":
#             for i in sort_by_age("ASC"):
#                 print(i)
#         elif mode == "2":
#             for j in sort_by_age("DESC"):
#                 print(j)
#         else:
#             break
#     else:
#         break


