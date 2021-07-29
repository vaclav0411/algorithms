def extreme_points(n: int, array: list):
    sort_arr = sorted(array, key=lambda x: x[1])
    result = [sort_arr[0]]
    d = 1
    while d < len(sort_arr):
        if sort_arr[d][0] > result[-1][1]:
            result.append(sort_arr[d])
        d += 1
    return result


if __name__ == '__main__':
    count = int(input())
    lst = [list(map(int, input().split())) for _ in range(count)]
    pre_result = extreme_points(count, lst)
    result = [str(i[1]) for i in pre_result]
    print(len(result))
    print(' '.join(result))
