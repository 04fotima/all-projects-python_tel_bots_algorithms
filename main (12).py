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


##4444
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
# for j in range(3, int(n**0.5)+1):
#     while n % j == 0:
#         f.append(j)
#         n = n / j
# if n > 2:
#     f.append(n)
# print(f"Result:{n} = {' * '.join(str(factor) for factor in f)}")




































###222
#####Here's what I wrote; it prints all the odd numbers instead of primes
#####Bu funktsiya kiritish sifatida sonni oladi va agar u tub bo'lsa True, aks holda False qaytaradi