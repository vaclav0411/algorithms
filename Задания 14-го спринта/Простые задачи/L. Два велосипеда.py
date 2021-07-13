def savings(array, cost, low, days):
    if low >= days:
        return -1
    mid = (low + days) // 2
    if array[mid] > cost:
        return savings(array, cost, low, mid-1)
    elif array[mid] < cost:
        return savings(array, cost, mid+1, days)
    else:
        if array[mid-1] != array[mid]:
            return mid
        return savings(array, cost, low, mid)


if __name__ == "__main__":
    days = int(input()) - 1
    array = list(map(int, input().split()))
    cost = int(input())
    first_day = savings(array, cost, 0, days)
    second_day = savings(array, 2*cost, 0, days)
    print(first_day, second_day)


# def savings(array, cost, low, days):
#     if low >= days:
#         return -1
#     mid = (low + days) // 2
#     if array[mid] > cost:
#         for i in range(low, mid+1):
#             if array[i] >= cost:
#                 return i + 1
#     elif array[mid] < cost:
#         return savings(array, cost, mid+1, days)
#     else:
#         if array[mid-1] != array[mid]:
#             return mid + 1
#         return savings(array, cost, low, mid)
#
#
# if __name__ == "__main__":
#     days = int(input()) - 1
#     array = list(map(int, input().split()))
#     cost = int(input())
#     first_day = savings(array, cost, 0, days)
#     second_day = savings(array, 2*cost, 0, days)
#     print(first_day, second_day)


# def binary(array, cost, low, days):
#     if low >= days:
#         return -1
#     mid = (low + days) // 2
#     if array[mid] > cost:
#         return binary(array, cost, low, mid-1)
#     elif array[mid] < cost:
#         return binary(array, cost, mid+1, days)
#     else:
#         if array[mid-1] != array[mid]:
#             return mid + 1
#         return binary(array, cost, low, mid)
#
#
# def savings(array, cost, low, days):
#     if cost in array:
#         return binary(array, cost, low, days)
#     else:
#         for i in range(low, days+1):
#             if i >= cost:
#                 return i
#         return -1
#
#
# if __name__ == "__main__":
#     days = int(input()) - 1
#     array = list(map(int, input().split()))
#     cost = int(input())
#     first_day = savings(array, cost, 0, days)
#     second_day = savings(array, 2*cost, 0, days)
#     print(first_day, second_day)
