def unique_letters(string: str):
    array = []
    for i, value in enumerate(string):
        if value in array:
            index = array.index(value)
            for j in range(0, index+1):
                array[j] = None
            array.append(value)
            continue
        array.append(value)
    d = 0
    for i in array:
        if i is not None:
            d += 1
    return d


if __name__ == '__main__':
    s = input()
    print(unique_letters(s))
