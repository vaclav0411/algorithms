def factor(n):
    d = 2
    result = []
    while d*d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result


if __name__ == "__main__":
    number = int(input())
    print(factor(number))
