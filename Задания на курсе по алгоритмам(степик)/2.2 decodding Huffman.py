def decoding(sequence: str, dct: dict):
    arr = []
    num = ''
    for i in sequence:
        num += i
        if num in dct.values():
            arr.append(num)
            num = ''
            continue
    arr.append(num)
    for i in dct:
        for j in range(len(arr)):
            if dct[i] == arr[j]:
                arr[j] = i[0]
    return arr


if __name__ == '__main__':
    unique, count = map(int, input().split())
    values = {}
    for _ in range(unique):
        k = input().split(': ')
        values[k[0]] = k[1]
    s = input()
    print(''.join(decoding(s, values)))
