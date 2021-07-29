def various_terms(n: int):
    result = []
    d = 1
    while n >= 0:
        n -= d
        result.append(str(d))
        d += 1
    if n < 0:
        result.pop(abs(n)-1)
    return result


if __name__ == '__main__':
    n = int(input())
    result = various_terms(n)
    print(len(result))
    print(' '.join(result))
