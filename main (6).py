
#1
# a = []
# n = 0
# s = 0
# M = float()
# m = float()
# file = open('ex 1')
# for i in file:
#     v = i.split()
#     for j in v:
#         n += 1
#         int_f = int(j)
#         s += int_f
#         M = max(M, int_f)
#         m = min(m, int_f)
# print(f'value:{n} sum:{s} Max:{M} Min:{m}')


#2
# import string
# row = 0
# char = 0
# num = []
# low = []
# up = []
# space = []
# char_2 = []
# with open("ex2", "r") as file:
#     for i in file:
#         row += 1
#         for j in i:
#             char += 1
#             if j.isdigit():
#                 num.append(j)
#             elif j in string.ascii_lowercase:
#                 low.append(j)
#             elif j in string.ascii_uppercase:
#                 up.append(j)
#             elif j.isspace():
#                 space.append(j)
#             elif j in ('.', ',', ':', ';', '?', '!'):
#                 char_2.append(j)
# print(f"row:{row}\ncharacter:{char}\nNumber:{num}\nsmall: {low}\ncapital: {up}\nspace: {space}\ncharacter: {char_2}")



 #3
# with open('ex3', 'r') as file:
#     line = file.readlines()
# justified_lines = []
# for line in line:
#     word = line.split()
#     total_space = 60 - len(''.join(word))
#     num = len(word) - 1
#     space_between = total_space // num
#     extra_space = total_space % num
#     justified_line = word[0]
#     for i in range(1, len(word)):
#         space = space_between + (1 if i <= extra_space else 0)
#         justified_line += ' ' * space + word[i]
#     justified_lines.append(justified_line.rstrip())
# with open('justified_ex3.txt', 'w') as outfile:
#     outfile.write('\n'.join(justified_lines))
# with open('ex3', 'rt') as fotima:
#     print(fotima.read())
# print()
# with open('justified_ex3.txt', 'rt') as fotima:
#     print(fotima.read())




#4
# dict = {}
# with open('ex4.1', 'r') as s_file, open('ex4.2', 'r') as m_file:
#     for i in s_file:
#         s_info = i.split()
#         dict[s_info[1]] = s_info[0]
#     for j in m_file:
#         m_info = j.split()
#         s_name = m_info[0]
#         m1 = int(m_info[1])
#         m2 = int(m_info[2])
#         avg_mark = (m1 + m2) // 2
#         if m1 < 15 or m2 < 15 or avg_mark < 18:
#             result = 'fail'
#         else:
#             result = str(avg_mark)
#         print(dict.get(s_name), result)



#5_1
# file = open("ex5.1")
# matrix = []
# for row in file:
#     v = []
#     for i in row.strip():
#         v.append(int(i))
#     matrix.append(v)
# row_len = len(matrix)
# col_len = len(matrix[0])
# for j in range(row_len):
#     print("-", end="")
#     for r in range(col_len):
#         print("-" * 6, end="")
#     for c in range(4):
#         print("\n|", end="")
#         for rc in range(col_len):
#             if matrix[j][rc] == 0:
#                 print(" " * 5, end="|")
#             else:
#                 print("*" * 5, end="|")
#     print()
# print("-" * 49)

#5_2
# file = open("ex5.2")
# matrix = []
# for i in file:
#     v = []
#     for r in i.strip():
#         v.append(int(r))
#     matrix.append(v)
# print(matrix)
# row_len = len(matrix)
# col_len = len(matrix[0])
# for i in range(row_len):
#     print("-", end="")
#     for j in range(col_len * 6):
#         print("-", end="")
#     print()
#     for j in range(4):
#         for jj in range(col_len):
#             if matrix[i][jj] == 0:
#                 print("|" + " "*5, end="")
#             else:
#                 print("|" + "*" * 5, end="")
#         print("|")
#     print()
# print("-" * (col_len * 6 + 1))
















