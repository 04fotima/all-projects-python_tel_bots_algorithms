
# r = []
# c = []
# n = int(input("enter r:"))
# for i in range(n):
#     row = int(input("enter n:"))
#     print([i], end=" ")
# x = int(input("enter c:"))
# for e in range(x):
#     col = int(input("enter n:"))
#     print([e], end=" ")
# print()

# n = int(input("enter n: "))
# m = [[1, 2, 3], [4, 5, 6], [7, 12, 9]]
# for i in range(3):
#     for j in range(3):
#         print(m[i][j], end=" ")
#     print()

# x = int(input("enter x: "))
# for i in range(n):
#     for j in range(n):
#         if m[i][j] == x:
#             x_sum = 0
#             x_sum_col = 0
#             for l in range(n):
#                 x_sum += m[i][j]
#                 x_sum_col += m[j][l]
#             print(f'sum of row: {x_sum}, sum of col: {x_sum_col}')
#lab_4
# m = [[1, 2, 3], [5, 1, 7], [9, 8, 6]]
# n = 3
# for i in range(n):
#     for j in range(n):
#         print(m[i][j], end=' ')
#     print()
# x = int(input('Enter x: '))
# for i in range(n):
#     for j in range(n):
#         if m[i][j] == x:
#             x_sum = 0
#             for l in range(0, i+1):
#                 for k in range(0, j+1):
#                     x_sum += m[l][k]
#             print(f"sum of sub-matrix: {x_sum}")


matrix = [
    [2.6, 4.4, 5.0],
    [4.8, 3.4, 7.2],
    [2.0, 2.6, 3.8]
]
v = 3
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=' ')
    print()




