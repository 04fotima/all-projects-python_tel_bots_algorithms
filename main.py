# #lab4
# 4_1_1
# n = int(input("enter n: "))
# num = int(input("enter num: "))
# for row in range(n):
#     for col in range(num):
#         print((row, col), end=" ")
#     print()
#
#4_1_2
# number = int(input("enter n: "))
# for row in range(number):
#     for col in range(number):
#         print(row*10+col, end=" ")
#     print()
#
# #lab4_2_1
# num = int(input("enter n: "))
# for row in range(num):
#     for col in range(num):
#         if col == row:
#             print("*", end="")
#         elif col > row:
#             print("*", end="")
#     print()
# #lab4_2_2
# n = int(input("enter n: "))
# for row in range(n):
#     for space in range(row):
#         print(" ", end="")
#     for col in range(n):
#            print("*", end="")
#     print()
#
#
# #lab4_2_3
# n = int(input("enter n: "))
# for row in range(n):
#     for col in range(n):
#         if col == 0 or col == n-1 or row == 0 or row == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#
# #lab4_2-4
# n = int(input("enter n: "))
# for col in range(n):
#     for row in range(n):
#         if row == col:
#             print("*", end="")
#         elif row < col:
#             print("-", end="")
#         else:
#             print("+", end="")
#     print()
#
#
#
# #lab4_2_5
# n = int(input("enter n: "))
# for row in range(n):
#     for col in range(n):
#        if row == col or row == n-1-col:
#            print("*", end="")
#        else:
#            print(" ", end="")
#     print()
#
# #lab4_3_1
# while True:
#     n = int(input("Input n: "))
#     if n > 0:
#         print("*" * n)
#     else:
#         print("Execution terminated.")
#         break
#
# #lab4_4_1
# n = int(input("enter num: "))
# count = 1
# for row in range(n):
#     for col in range(n):
#         if col <= row:
#             print(count, end=" ")
#             count += 1
#     print()
#
# #lab4_4_2
# n = int(input("enter num: "))
# v = 1
# for row in range(n):
#     for col in range(n):
#         if row >= col and n-v+1:
#             print(v, end=" ")
#     else:
#         print("*" end="")
#
#             v += 1
#     print()


#
# # opposite
# n = int(input("enter n: "))
# for row in range(n):
#     for col in range(n):
#         if col >= n-1-row:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = int(input("enter n:"))
# if n%2 == 0:
#     print("*")
# elif n%2 == 1:
#     print("odd")
