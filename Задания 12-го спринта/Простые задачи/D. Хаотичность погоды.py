def chaotic_weather(array: list) -> int:
    if len(array) == 1:
        return 1
    result = 0
    for i, arg in enumerate(array):
        if i+1 > len(array)-1:
            if arg > array[i-1]:
                result += 1
            continue
        elif i-1 < 0:
            if arg > array[i+1]:
                result += 1
            continue
        elif arg > array[i+1] and arg > array[i-1]:
            result += 1
    return result


if __name__ == "__main__":
    days = int(input())
    list_ = list(map(int, input().split()))
    print(chaotic_weather(list_))
