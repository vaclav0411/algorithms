def continuous_backpack(array: list, bag: int):
    sort_arr = sorted(array, key=lambda x: x[0]/x[1], reverse=True)
    cost = 0
    d = 0
    while bag >= 0 and d < len(sort_arr):
        bag -= sort_arr[d][1]
        cost += sort_arr[d][0]
        d += 1
    if bag < 0:
        cost -= abs(bag)/sort_arr[d-1][1] * sort_arr[d-1][0]
    return cost


if __name__ == '__main__':
    count, weight = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(count)]
    print(continuous_backpack(lst, weight))
