def compare_numbers(number_1, number_2):
    minimum = len(number_1) if len(number_1) < len(number_2) else len(number_2)
    d = 0
    while minimum > d:
        if int(number_2[d]) > int(number_1[d]):
            return True
        elif int(number_2[d]) == int(number_1[d]):
            d += 1
            continue
        else:
            return False


def biggest_number(array: list, n):
    for i in range(1, n):
        number = array[i]
        j = i
        while j > 0 or compare_numbers(number, array[j-1]):  # Заменить компататор на ключи
            array[j] = array[j-1]
            j -= 1
        array[j] = number
    array = array[::-1]
    result = ''.join(array[1:])
    return result + array[0]


if __name__ == '__main__':
    count = int(input())
    array = input().split()
    print(biggest_number(array, count))
