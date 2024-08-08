###1111
# list = []
# vp = []
# vn = []
# r = int(input("enter num:"))
# for num in range(r):
#     s = int(input("enter n:"))
#     list.append(s)
#     if s > 0:
#         vp.append(s)
#     elif s < 0:
#         vn.append(s)
# print("Positive elements:", vp, "Negative elements:", vn)
#####2222222
# list = []
# while True:
#     n = int(input("enter n:"))
#     if n < 0:
#         break
#     list.append(n)
# result = []
# for i in list:
#     if i not in result:
#         result.append(i)
# print(f"numbers:", list)
# print(result)

####33333
c = [2, -3, 1, 2, 3, 1, 4, -6, 7, -5, -1]
for i in range(len(c)):
    num = 0
    for e in range(i+1, len(c)+1):
        num = sum(c[i:e])
        if num == 0:
            print(f"array start from  ({i}), length ({e-i}).")
######444444
# v = []
# n = int(input("enter n: "))
# for e in range(n):
#     c = int(input("enter num: "))
#     v.append(c)
# print("number:", v)
# N = len(v)
# for i in range(N):
#     sum_triplet = sum(v[i:i + 3])
#     print(f"Triplet {i + 1}: {v[i]} + {v[(i + 1) % N]} + {v[(i + 2) % N]} = {sum_triplet}")


#######555555
# v = []
# s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# n = 1
# while n >= 1:
#     n = int(input("Enter num: "))
#     if n >= 1:
#         v.append(n)
# for i in range(len(v)):
#     s[v[i]//10] += 1
# for i in range(max(s)):
#     for j in range(10):
#         if s[j] > 1:
#             print("#", end="")
#             s[j] -= 1
#         else:
#             print(" ", end="")
#     print()












