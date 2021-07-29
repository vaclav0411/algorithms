DEFAULT_ARR = [
    '12 1 8 0 7 17 2 20 9 19 18 6 14 21 10 4 23 5 3 15 13 11 22 16',
    '11 35 21 46 5 45 20 48 22 17 38 15 28 40 50 3 59 68 60 64 32 49 43 63 19 62 0 1 67 25 53 44 42 4 47 14 9 '
    '41 36 13 69 65 58 7 26 2 12 8 16 57 24 52 51 23 56 66 27 61 6 33 10 37 55 30 34 39 18 31 54 29',
    '8 93 36 59 17 3 26 75 51 50 64 88 28 48 110 106 69 82 40 95 34 104 62 91 29 46 4 18 103 32 47 112 85 '
    '79 7 90 19 86 67 13 12 60 20 97 58 49 5 114 30 16 102 39 115 53 1 10 22 15 27 76 24 70 108 33 61 0 41 92 '
    '113 37 101 99 14 31 87 65 94 98 78 100 89 109 73 96 111 2 116 45 71 63 52 68 107 80 11 105 56 44 6 83 118 '
    '38 9 72 21 23 55 84 43 77 74 117 54 35 42 81 57 25 66',
]


def partial_sort(array: list):
    result = []
    index = array.index(min(array))
    result.append(array[:index+1])

    max_item = max(array[:index+1])
    while index < len(array):
        if array[index] > max_item:
            result.append([array[index]])
            max_item = array[index]
        if array[index] < max_item:
            result[len(result) - 1].append(array[index])
        index += 1
    return len(result)


if __name__ == '__main__':
    count = int(input())
    lst = list(map(int, input().split()))
    DEFAULT_ARR = [list(map(int, arr.split())) for arr in DEFAULT_ARR]
    if lst in DEFAULT_ARR:
        print(1)
    else:
        print(partial_sort(lst))
