def unique_letters(n: int, array: list):
    list_arr = {}
    for i, value in enumerate(array):
        sort_val = ''.join(map(str, sorted(value)))
        if sort_val in list_arr:
            list_arr[sort_val].append(i)
            continue
        list_arr[sort_val] = [i]
    result = [map(str, v) for k, v in list_arr.items()]
    return result


if __name__ == '__main__':
    count = int(input())
    lst = input().split()
    res = unique_letters(count, lst)
    for i in res:
        print(' '.join(i))
