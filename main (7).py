import csv
def write_csv(changed_list):
    with open("info_csv", "w", newline="") as csv.file:
        csv_writer = csv.writer(csv.file)
        csv_writer.writerows(changed_list)

def read_csv():
    with open("info_csv", "r", newline="") as csv.file:
        csv_reader = csv.reader(csv.file)
        for x in csv_reader:
            print(x)

def add_csv(name,surname,age):
    with open("info_csv", "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([name,surname,age])

def csv_to_list():
    copy_list = []
    with open("info_csv", "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        for x in csv_reader:
            copy_list.append(x)
    return copy_list
def change_csv():
    copy_list = csv_to_list()
    for x in copy_list:
        if x[2] == '45':
            x[2] = '100'
    write_csv(copy_list)
    change_csv()




# import csv
# def wcvs():
#     with open("info.csv", "w", newline="") as csv_file:
#         w = csv.writer(csv_file)
#         w.writerows(['name','surname','age'])
# wcvs()
# def rcvs():
#     with open('info_cvs','r',newline="") as cvs_file:
#         r = cvs.reader(cvs_file)
#         for i in r:
#             print(i)
# rcvs()
