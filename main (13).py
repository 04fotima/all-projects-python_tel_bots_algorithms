

####11111
# c = [[4, 3, 1, 2], [1, 7, 2, 2], [3, 3, 5, 0]]
# for sublist in c:
#     print(sublist)
# x = int(input("enter x: "))
# for i, sublist in enumerate(c):
#     for j, element in enumerate(sublist):
#         if element == x:
#             r_sum = sum(c[i])
#             c_sum = sum(column[j] for column in c)
#             print(f"Sum  Row: {r_sum}, Sum  Col: {c_sum}")



####222222
# a = [[2.6, 4.4, 5.0], [4.8, 3.4, 7.2], [2.0, 2.6, 3.8]]
# a_r = []
# first = True
# v = [0, 0, 0]
# for i in range(len(a)):
#     if not first:
#         for j in range(len(a)):
#             v[j] = (a[i-1] [j] + a[i][j])/2
#         a_r.append(v.copy())
#         a_r.append(a[i])
#     else:
#         a_r.append(a[i])
#     first = False
# for s in a_r:
#     print(s)


#####333333
# n_1 = [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]
# n_2 = [[9, 8, 7],
#       [6, 5, 4],
#       [3, 2, 1]]
# r_1, c_1 = len(n_1), len(n_1[0])
# r_2, c_2 = len(n_2), len(n_2[0])
# n_3 = [[0] * c_2 for x in range(r_1)]
# for i in range(r_1):
#     for r in range(c_2):
#         for e in range(c_1):
#             n_3[i][r] += n_1[i][e] * n_2[e][r]
# for k in range(r_1):
#     for v in range(c_2):
#         print(n_3[k][v], end=" ")
#     print()


####44444
# matrix = [[1, -2, 0, 3],
#          [3, 1, 5, 4],
#          [7, 2, 3, 1],
#          [4, 6, -1, 5]]
# print(matrix)
# n = int(input("enter num: "))
# for i in range(4):
#     for j in range(4):
#         if matrix[i][j] == n:
#             sum_x = 0
#             for i in range(0, 1+i):
#                 for j in range(0, j+1):
#                     sum_x += matrix[i][j]
#                 print(f'Sum of matrix: {sum_x}')

####555555
# i = 0
# j = 0
# n = 5
# print(f"({i}, {j})")
# while i != n-1 or j != n-1:
#     if j+1 != n:
#         j -= 1
#     else:
#         i += 1
#     print(f"({i}, {j})")
#     while j != 0 and i != n-1:
#         i += 1
#         j -= 1
#         print(f"({i}, {j})")
#     if  i + 1 != n:
#         i += 1
#     else:
#         j += 1
#     print(f"({i}, {j})")
#     while i != 0 and j != n-1:
#         i -= 1
#         j += 1
#         print(f"({i}, {j})")



##1111111
# n = int(input("enter num: "))
# d = int(input("enter den: "))
# for i in range(1, min(n, d) + 1):
#     if n % i == 0 and d % i == 0:
#         num = i
# s_n = n // num
# s_d = d // num
# print(f"Result: {n}/{d} = {s_n}/{s_d}")

###222222
# m = int(input("enter m: "))
# print(f"num <= {m}, are: ", end= " ")
# for num in range(2, m + 1):
#     p = 1
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             p = 0
#             break
#     if p:
#         print(num, end=" ")
# print()

#####3333333
# y = int(input("enter y: "))
# n = 0
# while n**n < y:
#     n += 1
# n -= 1
# print(f"Max n = {n}")

###4444
# n = int(input("enter num: "))
# s = int(input("enter num: "))
# for _ in range(n):
#     print("+" + "---+" * n)
#     for _ in range(s):
#         print("|" + "   |" * n)
# print("+" + "---+" * n)

####555555
# n = int(input("enter n: "))
# f = []
# while n % 2 == 0:
#     f.append(2)
#     n = n / 2
# for j in range(3, int(n**0.5)+ 1):
#     while n % j == 0:
#         f.append(j)
#         n = n / j
# if n > 2:
#     f.append(n)
# print(f"Result:{n} = {' * '.join(str(factor) for factor in f)}")


n = 13
print(f"prime:")
for i in range(2,(n**1)+1):
    if i % n == 0:
        print(i)















