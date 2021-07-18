BUTTONS = {
    '2' : 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def combinations(n, array, storage: list, prefix=''):
    if n == 0:
        storage.append(prefix)
    else:
        for i in range(len(array[n-1])):
            letter = str(array[n-1][i])
            combinations(n-1, array, storage, prefix=prefix+letter)


if __name__ == "__main__":
    buttons = list(input())
    count = len(buttons)
    array = [BUTTONS[i] for i in buttons if i in BUTTONS]
    result = []
    combinations(count, array[::-1], result)
    print(' '.join(result))
