def neighbours(x, y, array, m, n):
    result = []
    if not x - 1 < 0:
        result.append(array[x-1][y])
    if not y + 1 > n:
        result.append(array[x][y+1])
    if not x + 1 > m:
        result.append(array[x+1][y])
    if not y - 1 < 0:
        result.append(array[x][y-1])
    return sorted(result)


if __name__ == "__main__":
    m = int(input()) - 1
    n = int(input()) - 1
    array = [list(map(int, input().split())) for i in range(m+1)]
    x = int(input())
    y = int(input())
    pre_result = list(map(str, neighbours(x, y, array, m, n)))
    result = ' '.join(list(map(str, pre_result)))
    print(result)
