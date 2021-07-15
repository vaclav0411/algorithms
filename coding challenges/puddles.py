def puddles(array: list) -> int:
    minimum = 0
    result = 0
    for i in range(len(array)):
        if array[i] > minimum:
            minimum = array[i]
        elif minimum > array[i]:
            result += minimum - array[i]
        else:
            continue
    return result


def divide(array: list):
    maximum = max(array)
    index = array.index(maximum)
    return puddles(array[:index]) + puddles(array[:index:-1])


if __name__ == "__main__":
    array = list(map(int, input().split()))
    print(divide(array))
