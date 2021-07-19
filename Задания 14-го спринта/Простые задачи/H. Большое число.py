def less(number, number_1):
    array_number = list(map(int, number))
    array_number_1 = list(map(int, number_1))
    number = array_number + array_number_1
    number_1 = array_number_1 + array_number
    return number < number_1


def biggest_number(array: list, n):
    for i in range(1, n):
        number = array[i]
        j = i
        while j > 0 and less(number, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = number
    array = array[::-1]
    return ''.join(array)


if __name__ == '__main__':
    count = int(input())
    array = input().split()
    print(biggest_number(array, count))
