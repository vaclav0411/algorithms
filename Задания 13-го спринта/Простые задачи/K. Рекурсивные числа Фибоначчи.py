def recursion_fibonacci(i: int, array: list, n=2):
    if i in (0, 1):
        return 1
    array[0] = 1
    array[1] = 1
    if n == i:
        return array[n-1] + array[n-2]
    array[n] = array[n-1] + array[n-2]
    return recursion_fibonacci(i, array, n+1)


if __name__ == '__main__':
    i = int(input())
    array = [0] * i
    print(recursion_fibonacci(i, array))