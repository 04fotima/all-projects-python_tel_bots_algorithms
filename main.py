

#
# import time
#
# def binary_search(numbers, x):
#     low = 0
#     high = len(numbers) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if numbers[mid] == x:
#             return mid
#         elif numbers[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
# def main():
#     # Read numbers from the file
#     filename = input("Enter the filename: ")
#     with open(filename, 'r') as file:
#         numbers = [int(num) for num in file.read().split()]
#
#     # Sort the list for binary search
#     numbers.sort()
#
#     while True:
#         try:
#             x = int(input('Enter the number to search for: '))
#             break
#         except ValueError:
#             print("Please enter a valid integer.")
#
#     # Linear search algorithm
#     print('Linear search algorithm')
#     j = 0
#     p = False
#     t1 = time.time()
#
#     for i in numbers:
#         j += 1
#         if x == i:
#             print(j, 'iterations were performed and the number was found.')
#             p = True
#             break
#
#     if not p:
#         print(j, 'iterations were performed but the number was not found.')
#
#     t2 = time.time()
#     print('Time taken for linear search:', t2 - t1)
#
#     # Binary search algorithm
#     print('Binary search algorithm')
#     k = 0
#     t = False
#     t1 = time.time()
#     index = binary_search(numbers, x)
#
#     if index != -1:
#         print(f"Number found at index {index}.")
#     else:
#         print("Number not found.")
#
#     t2 = time.time()
#     print('Time taken for binary search:', t2 - t1)
#
# if __name__ == "__main__":
#     main()
























import time
import bisect

def main():
    # Read numbers from the file
    filename = input("Enter the filename: ")
    numbers = []

    with open(filename, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))

    # Sort the list for binary search
    numbers.sort()

    while True:
        try:
            x = int(input('Enter the number to search for: '))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Binary search algorithm using bisect module
    print('Binary search algorithm with bisect module')
    t1 = time.time()
    index = bisect.bisect_left(numbers, x)

    if index < len(numbers) and numbers[index] == x:
        print(f"Number found at index {index}.")
    else:
        print("Number not found.")

    t2 = time.time()
    print('Time taken for binary search with bisect module:', t2 - t1)

if __name__ == "__main__":
    main()
































































































































































































































































































































































































































































