def wardrobe(array: list, n: int = 3):
    colors = [0] * n
    for value in array:
        colors[value] += 1
    index = 0
    for value in range(n):
        for amount in range(colors[value]):
            array[index] = value
            index += 1
    return array


if __name__ == '__main__':
    count = int(input())
    list_ = list(map(int, input().split()))
    print(' '.join(map(str, wardrobe(list_))))
