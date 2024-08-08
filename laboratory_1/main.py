# ###ex1
# x = int(input("Enter value: "))
# y = int(input("Enter value: "))
# s = x + y
# print(s)
# ###ex2
# n = int(input("Enter value: "))
# m = n - 1
# l = n + 1
# print(m)
# print(l)
###ex3
# tf = int(input("enter value: "))
# tc = 5 * (tf - 32) / 9
# TC = (tf / 5 * 9) + 32
# print(tc)
# print(TC)
###ex4


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# # print("The numbers in reverse order are:", num3, num2, num1)
# n = [num1, num2, num3]
# print(list(reversed(n)))
# char = input("enter char: ")
# for i in char[::-1]:
#     print(i)

# for n in range(3):
#     n = int(input("Enter the first number: "))
#     for i in str(n)[::-1]:
#         print(i)
# num = []
# for n in range(3):
#     n = int(input("Enter the first number: "))
#     s = str(n)
#     num.append(s)
# for i in num[::-1]:
#      print(i)




#lab2
#ex1
# n = int(input("enter num:"))
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")

#ex2
# n1 = int(input("enter num1:"))
# n2 = int(input("enter num2:"))
# n3 = int(input("enter num3:"))
# if n1 == n2 and n2 == n3  and n1 == n3:
#     print("All three num is equel")
# elif n1 == n2 or n2 == n3 or n1 == n3:
#     print("two num is equel")
# else:
#     print("all nums are different")

#ex3
# n1 = int(input("enter num1:"))
# n2 = int(input("enter num2:"))
# n3 = int(input("enter num3:"))
# if n1 > n2 and n1 > n3:
#     print("larger one num 1")
# elif n2 > n1 and n2 > n3:
#     print(" num 2 larger one ")
# elif n3 > n1 and n3 > n2:
#     print("num 3 is larger one")

#ex4

# operation = input("Enter the operation (+, -, *, /): ")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     if num2 == 0:
#         result = "Division by zero is not allowed!"
#     else:
#         result = num1 / num2
# else:
#     result = "Invalid operation!"
#
# print("Result:", result)
#ex5
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# c = int(input("enter c: "))
# if a == b and a == c:
#     print("Equilateral triangle")
# elif (a == b and b != c) or (b == c and c != a) or (a == c and c != a):
#     print("Isosceles triangle")
# elif a != b and b != c:
#     print("Scalene triangle")
# elif c * c == a * a + b *b or a * a == b * b + c * c or b * b == a * a + c * c:
#     print("Rectangular triangle")
# elif a < b + c and b < a + c and c < a + b:
#     print("The sides can form a triangle.")

#ex6
# n = (input("enter char: "))
# char = n.lower()
# if char in 'a''e' 'u' 'i' 'o':
#     print("vowel")
# else:
#     print("consonant")
# import NumPy
# import math


#ex7
# n = int(input("Enter year: "))
# if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
#     print(f' {n} is leap year')
# else:
#     print("are not leap year")

import cmath


#ex8
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# c = int(input("enter c: "))
# x1 = (-b + cmath.sqrt((b**2)-4*(a*c))) / (2 * a)
# x2 = (-b - cmath.sqrt((b**2)-4*(a*c))) / (2 * a)
# print(f" {x1} and {x2} are root")

#lab3
#ex1
# s = 0
# n = int(input("enter num:"))
# for i in range(n):
#     num = int(input(f"enter num {i+1}: "))
#     s += num
# r = s / n
# print(r)

#ex2
# n = int(input("enter positive num: "))
# if n < 0:
#     print("you should enter positive number please try again")
# else:
#     b = 0
#     for i in range(1, n+1):
#         b += 1/i
#         print(b)


#ex3
# p = 0
# n = 0
# pap = []
# nap = []
# n = int(input("enter num: "))
# for i in range(n):
#     num = int(input(f"enter num{i+1}: "))
#     if num > 0:
#         p += num
#         pap.append(num)
#     elif num < 0:
#         n += num
#         nap.append(num)
# print(p)
# print(pap)
# print(n)
# print(nap)

#ex4
# n = input("enter char: ")
# if n.isdigit():
#     num = chr(int(n))
#     print(num)
# elif n.isalpha():
#     alpha = ord(n)
#     print(alpha)

#ex5
# x = int(input("enter x: "))
# y = int(input("enter y: "))
# while True:
#     if x > y:
#         d = x%y
#         v = y%d
#         if v != 0:
#             print(v)
#             break
#     else:
#         div = y%x
#         val = x%div
#         if val != 0:
#             print(val)
#             break
# x = int(input("enter x: "))
# y = int(input("enter y: "))
#
# # Ensure x is always greater than or equal to y
# if x < y:
#     x, y = y, x
#
# # Euclid's Algorithm
# while y != 0:
#     r = x % y  # Calculate the remainder
#     x = y       # Update x to the previous value of y
#     y = r       # Update y to the remainder
#
# print(f"The greatest common divisor (GCD) of {x} and {y} is: {x}")

#ex6
# n = int(input("enter num: "))
# for i in range(n):
#     num = int(input(f"enter n{i + 1}: "))
#     if num[0] > num[1]:
#       print("descanding")
#     else:
#         print("ascending")
# n = int(input("Enter the number of values (n): "))
#
# # Read the n values
# values = []
# for i in range(n):
#     values.append(int(input(f"Enter value {i + 1}: ")))

# Check for ascending, descending, or neither
# if n <= 1:
#     print("Neither ascending nor descending sequence")
# else:
#     is_ascending = True
#     is_descending = True
#     for i in range(1, n):
#         if values[i] <= values[i - 1]:
#             is_ascending = False
#         if values[i] >= values[i - 1]:
#             is_descending = False
#
#     if is_ascending:
#         print("Ascending sequence")
#     elif is_descending:
#         print("Descending sequence")
#     else:
#         print("Neither ascending nor descending sequence")

#ex7
# v =[]
# maxi = []
# n = int(input("enter num: "))
# for i in range(n):
#     v.append((int(input(f"enter num {i + 1}: "))))
# m = max(v)
# maxi.append(m)
# v.remove(m)
# m2 = max(v)
# maxi.append(m2)
# print(maxi)


#lab4
# #ex1
# r = int(input("enter n: "))
# c = int(input("enter n: "))
# for i in range(r):
#     for j in range(c):
#         print(f"({i},{j})", end=" ")
#     print()

# r = int(input("enter n: "))
# c = int(input("enter n: "))
# for i in range(r):
#     for j in range(c):
#         print(i * 10 + j, end=" ")
#     print()
#ex2
# r = int(input("enter row: "))
# c = int(input("enter col: "))
# for i in range(r, 0, -1):
#     for j in range(i):
#         print("*",  end="")
#     print()
r = int(input("enter row: "))
c = int(input("enter col: "))
for i in range(r):
    for j in range(c):
        for s in range(i+1, -1, -1):
            print(" ", end="")
            print("*", end="  ")
    print()