
###111
# def pal_check(p):
#     return p == p[::-1]
# p = input("enter string:")
# p = p.lower()
# if pal_check(p):
#     print("it is palindrome")
# else:
#     print("it is not palindrom")
###222
# def char_r(s1, s2):
#     s3 = ""
#     for char in s1:
#         if char not in s2:
#             s3 += char
#     return s3
# s1 = input("enter n1:")
# s2 = input("enter n2:")
# s3 = char_r(s1, s2)
# print("result n3:", s3)


###3333
# c = input("enter ch: ")
# w = []
# while True:
#     n = input("enter word: ")
#     if n == "finish":
#         break
#     w.append(n)
#
#
# ce = w.count(c)
# most = max(ce)
# print(f"The word is {most}")



###444
# import re
# line = input("enter line: ")
# word = re.findall(r'\b\w+\b', line)
# result = ' '.join(word[0].upper() + word[1:] for word in word)
# print("Output line: " + result)


###555
# n1 = input("enter n1: ")
# n2 = input("enter n2: ")
# n3 = input("enter n3: ")
# result = n1.replace(n2, n3)
# print("Result string: " + result)
######
# n1 = input("enter n1: ")
# n2 = input("enter n2: ")
# n3 = input("enter n3: ")
#
# result = ""
# i = 0
# while i < len(n1):
#     if n1[i:i+len(n2)] == n2:
#         result += n3
#         i += len(n2)
#     else:
#         result += n1[i]
#         i += 1
#
# print("Result string: " + result)



###666
# def binary(a, b):
#     a = int(a, 2)
#     b = int(b, 2)
#     c = a + b
#     return bin(c)[2:]
# a = input("enter n: ")
# b = input("enter n: ")

#
# s = binary(a, b)
# print("Result S: ", s)















# n = []
# row = int(input('How many rows in matrix?: '))
# col = int(input('How many cols in matrix?: '))
# for i in range(row):
#     lst = []
#     for j in range(col):
#         nums = int(input('input nums: '))
#         lst.append(nums)
#     n.append(lst)
# for k in n:
#     print(k)
# result = [[n[i][j] + n[i][j + 1] + n[i + 1][j] + n[i + 1][j + 1] if j < col-1 and i < row-1 else 0 for j in range(col-1)] for i in range(row-1)]
# for r in result:
#     print(r)


#1
# n = input("enter word:")
# p = n.lower()
# num = p[::-1]
# if p == num:
#     print("it is palindrome")
# else:
#     print("not palindrome")

#2
# n1 = input("enter n:")
# n2 = input("enter n:")
# n3 = ""
# for i in n1:
#     if i not in n2:
#         n3+=i
# print(f"result:", n3)

#3
# a = []
# n = input("enter ch:")
# while True:
#     num = input("enter word:")
#     if num == "finish":
#         break
#     a.append(num)
# count = {}
# for i in a:
#     count[i] =i.lower().count(n.lower())
# m = max(count, key= count.get)
# print(f"The word is {m}.")


#4
# n = input("enter: ").title()
# print(f"output:", n)


#5
# n1 = input("enter n1: ")
# n2 = input("enter n2: ")
# n3 = input("enter n3: ")
# result = ""
# i = 0
# while i < len(n1):
#     if n1[i:i+len(n2)] == n2:
#         result += n3
#         i += len(n2)
#     else:
#         result += n1[i]
#         i += 1
#
# print("Result string: " + result)


#6
# def binary(a, b):
#     a = int(a,2)
#     b = int(b,2)
#     c = a + b
#     return bin(c)[2:]
# a = input("enter n: ")
# b = input("enter n: ")
# s = binary(a, b)
# print("Result S: ", s)


