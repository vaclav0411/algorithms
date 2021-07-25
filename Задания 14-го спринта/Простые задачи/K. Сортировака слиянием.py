def merge(array: list, left: int, mid: int, right: int) -> list:
    local_array = array[left:right]
    if len(local_array) == 1:
        return local_array
    n = len(array[left:right])
    array_1 = merge(array, left, (left+mid)//2, mid)
    array_2 = merge(array[mid:right])
    result = [None] * n
    l, r, k = 0, 0, 0
    while l < len(array_1) and r < len(array_2):
        if array_1[l] >= array_2[r]:
            result[k] = array_1[l]
            l += 1
        if array_1[l] < array_2[r]:
            result[k] = array_2[r]
            r += 1
        k += 1

    while l < len(array_1):
        result[k] = array_1[l]
        l += 1
        k += 1
    while r < len(array_2):
        result[k] = array_2[r]
        r += 1
        k += 1
    return result


def merge_sort(array: list, left: int, right: int):
    local_array = array[left:right]
    if len(local_array) == 1:
        return local_array
    mid = len(local_array) // 2
    left_array = merge_sort(local_array, 0, mid)
    right_array = merge_sort(local_array, mid, len(local_array))
    full_array = left_array + right_array
    print(0, len(left_array), len(full_array))
    return merge(full_array, 0, len(left_array), len(full_array))


if __name__ == '__main__':
    array = list(map(int, input().split()))
    print(merge_sort(array, 0, 4))
