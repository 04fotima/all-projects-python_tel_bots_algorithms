
#####11111
# array = []
# even_number = []
# odd_number = []
# n = int(input("enter number:"))
# while True:
#     for i in range(n):
#         v = int(input("enter num:"))
#         if v % 2 == 0:
#             even_number.append(v)
#         elif v % 2 == 1:
#             odd_number.append(v)
#         array.append(v)
#     print(f"v = {array}")
#     break
# print(f"even: {even_number}")
# print(f"odd: {odd_number}")


###222222
# v = []
# n = int(input("Input n: "))
# for i in range(n):
#     a = int(input(f"Input v[{i}]: "))
#     v.append(a)
# print(f"val = {v}")
# repeat = 1
# while repeat == 1:
#     x = int(input("Input x: "))
#     count = v.count(x)
#     print(f"Value {x} appears {count} time(s) in the array.")
#     repeat = int(input("Would you like to continue (1=yes, 0=no)? "))
# print("Program terminated")


#####33333
# array = []
# arr = []
# ma = []
# max_pos = -1
# max_val = 1
# n = int(input("enter number:"))
# for i in range(n):
#     v = int(input("enter n:"))
#     array.append(v)
#     w = int(input("enter num:"))
#     arr.append(w)
#     for i in range(len(array)):
#         if abs(array[i]-arr[i]) > max_val:
#             max_val = abs(array[i]-arr[i])
# print(f"v = {array}")
# print(f"w = {arr}")
# print(f"max of abs val {array[max_pos]} and {arr[max_pos]} on position {max_val} ")



###444444
# array = []
# arr = []
# p = []
# n = int(input("enter number:"))
# for i in range(n):
#     b = int(input("enter base:"))
#     array.append(b)
#     e = int(input("enter exp:"))
#     arr.append(e)
#     x = (b**e)
#     p.append(x)
#
# print(f"base = {array}")
# print(f"exp = {arr}")
# print(f"power = {p}")


##55555555
# list = []
# dim = int(input("enter dim: "))
# for i in range(dim):
#     val = float(input("input val: "))
#     list.append(val)
# print(f"v = {list}")
# def longest_positive_sequence(list):
#     n = len(list)
#     start_index = 0
#     max_length = 0
#     start_indices = [0] * n
#     lengths = [0] * n
#     for i in range(1, n):
#         if list[i] > 0:
#             lengths[i] = lengths[i - 1] + 1
#             start_indices[i] = start_indices[i - 1]
#         else:
#             lengths[i] = 1
#             start_indices[i] = i
#         if lengths[i] > max_length:
#             max_length = lengths[i]
#             start_index = start_indices[i]
#
#
#     return start_index, max_length
# start_index, max_length = longest_positive_sequence(list)
#
# print("The longest positive sequence (" + str(max_length) + " elements) starts from index " + str(start_index) + ".")

