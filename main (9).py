# def check(str, words):
#     for i in range(len(str)):
#         for j in range(i + 1, len(str)):
#             if str[i:j + 1] in words:
#                 output.append(str[i:j + 1])
# words = ["eat", "look", "pea", "rain", "pkt"]
# boards = []
# output = []
# with open("m.exam") as fhand:
#     for line in fhand:
#         v = line.strip().split()
#         boards.append(v)
# for i in range(len(boards)):
#     st = "".join(boards[i]).strip()
#     check(st, words)
#     check(st[::-1], words)
# for i in range(len(boards[0])):
#     st = "".join(boards[j][i] for j in range(len(boards)))
#     check(st, words)
#     check(st[::-1], words)
# print(output)




























































# def check(str, words):
#     for i in range(len(str)):
#         for j in range(i + 1, len(str)):
#             if str[i:j + 1] in words:
#                 output.append(str[i:j + 1])
# words = ["eat", "look", "pea", "rain", "pkt"]
# boards = []
# with open("extra.output") as last:
#     with open("m.exam") as fhand:
#         for line in fhand:
#             v = line.strip().split()
#             boards.append(v)
# output = []
# # Check horizontally
# for row in boards:
#     check("".join(row), words)
#     check("".join(row)[::-1], words)
# # Check vertically
# for col in range(len(boards[0])):
#     st = "".join(row[col] for row in boards)
#     check(st, words)
#     check(st[::-1], words)
# print(output)



def check(str, words):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i:j + 1] in words:
                output.append(str[i:j + 1])

words = ["111", "222", "444", "333", "666"]
boards = []
with open("extra.output") as last:
    with open("m.exam") as fhand:
        for line in fhand:
            v = line.strip().split()
            boards.append(v)

output = []

# Check horizontally
for row in boards:
    check("".join(row), words)
    check("".join(row)[::-1], words)

# Check vertically
for col in range(len(boards[0])):
    st = "".join(row[col] for row in boards)
    check(st, words)
    check(st[::-1], words)
# Check diagonally (top-left to bottom-right)
for start_col in range(len(boards[0])):
    st = ''
    row = 0
    col = start_col
    while row < len(boards) and col < len(boards[0]):
        st += boards[row][col]
        row += 1
        col += 1
    check(st, words)
    check(st[::-1], words)
# Check diagonally (top-right to bottom-left)
for start_col in reversed(range(len(boards[0]))):
    st = ''
    row = 0
    col = start_col
    while row < len(boards) and col >= 0:
        st += boards[row][col]
        row += 1
        col -= 1
    check(st, words)
    check(st[::-1], words)
print(output)








































# def getDistance(x, y, z):
#     return ((x 2) + (y 2) + (z ** 2)) * 0.5
# def mySort(l):
#  return l['point']
# lst = [{'point': 45.6, 'values': [3, 5, 6]},]
# f = open("Points.txt")
# w = open("Result.txt", "w")
# for i in f:
#  temp = i.split()
#  x, y, z = int(temp[0]), int(temp[1]), int(temp[2])
#  lst.append({'point': getDistance(x, y, z), 'values': [x, y, z]})
# lst.sort(key=mySort)
# for i in range(len(lst)):
#     string = ""
#     for j in lst[i].values():
#         string += str(j)
#         string += "\t\t"
#         string = string.replace("[", "")
#         string = string.replace("]", "")
#         w.write(string)
#         w.write("\n")
