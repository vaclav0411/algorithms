def merge_sort(alist: list, start: int, end: int) -> None:
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge(alist, start, mid, end)


def merge(alist: list, start: int, mid: int, end: int):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
    return list(map(str, alist))


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    rg = len(array)
    merge_sort(array, 0, rg)
    print(' '.join(array))










# def merge(arr, lf, mid, rg):
#     left = arr[lf:mid]
#     right = arr[mid:rg]
#     support = arr[:]
#     l, r, d = 0, 0, lf
#     while (l+lf) < mid and (mid+r) < rg:
#         if left[l] <= right[r]:
#             arr[d] = left[l]
#             l += 1
#         elif right[r] < left[l]:
#             arr[d] = right[r]
#             r += 1
#         d += 1
#     if lf + l < mid:
#         while d < rg:
#             arr[d] = left[l]
#             l += 1
#             d += 1
#     else:
#         while d < rg:
#             arr[d] = right[r]
#             r += 1
#             d += 1
#     return arr
#
#
# def merge_sort(arr, lf, rg):
#     if rg - lf < 2:
#         return
#     mid = (lf + rg)//2
#     merge_sort(arr, lf, mid)
#     merge_sort(arr, mid, rg)
#     merge(arr, lf, mid, rg)
#
#
# if __name__ == '__main__':
#     sort = input()
#     n = int(input())
#     array = list(map(int, input().split()))
#     rg = len(array)
#     print(merge_sort(array, 0, rg))
#     print(' '.join(map(str, array)))

# def merge(arr, lf, mid, rg):
#     support = arr[:]
#     l, r, d = lf, mid, lf
#     while l < mid and r < rg:
#         if support[l] < support[r]:
#             arr[d] = support[l]
#             l += 1
#         elif support[r] < support[l]:
#             arr[d] = support[r]
#             r += 1
#         d += 1
#     while l < mid:
#         arr[d] = support[l]
#         d += 1
#         l += 1
#     while r < rg:
#         arr[d] = support[r]
#         r += 1
#         d += 1
#     return arr
#
#
# def merge_sort(arr, lf, rg):
#     if rg - lf < 2:
#         return
#     mid = (lf + rg)//2
#     merge_sort(arr, lf, mid)
#     merge_sort(arr, mid, rg)
#     merge(arr, lf, mid, rg)
#
#
# if __name__ == '__main__':
#     sort = input()
#     n = int(input())
#     array = list(map(int, input().split()))
#     rg = len(array)
#     merge_sort(array, 0, rg)
#     print(' '.join(map(str, array)))
