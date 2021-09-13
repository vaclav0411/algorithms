def quick_search(lst: list, find: list):
    result = []
    for i in find:
        high = len(lst) - 1
        low = 0
        found = 0
        while low <= high and found == 0:
            middle = (high + low) // 2
            guess = lst[middle]
            if guess == i:
                result.append(str(middle+1))
                found = 1
            elif guess < i:
                low = middle + 1
            else:
                high = middle - 1
        if not found:
            result.append('-1')
    return result


if __name__ == '__main__':
    n, *A = map(int, input().split())
    n0, *A0 = map(int, input().split())
    print(quick_search(A, A0))
