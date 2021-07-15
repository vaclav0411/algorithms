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


def sequence_pressings(n, k, prefix=''):
    amount = len(n)
    if k == 0:
        print(prefix)
    # else:
        # for i in
        # sequence_pressings(n, k-1, prefix+'0')
        # sequence_pressings(n, k-1, prefix+'1')


if __name__ == "__main__":
    n = ['2', '3']
    print(sequence_pressings(n, 2))