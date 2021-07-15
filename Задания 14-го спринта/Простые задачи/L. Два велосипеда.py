import typing


def bicycles(array: typing.List, cost: int, low: int, high: int) -> int:
    if array[-1] == cost and array[-2] != cost:
        return high + 1
    if low >= high:
        if array[high] > cost:
            return high + 1
        return -1
    mid = (low + high) // 2
    guess = array[mid]
    if guess == cost:
        if array[mid-1] == guess:
            return bicycles(array, cost, low, mid)
        return mid + 1
    elif guess > cost:
        return bicycles(array, cost, low, mid)
    elif guess < cost:
        return bicycles(array, cost, mid + 1, high)
    return -1


if __name__ == "__main__":
    days = int(input()) - 1
    list_ = list(map(int, input().split()))
    price = int(input())
    first = bicycles(list_, price, 0, days)
    second = bicycles(list_, 2*price, 0, days)
    print(first, second)
