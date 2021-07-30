def fib_mod(n, m):
    if n <= 1:
        return n
    previous = 0
    last = 1
    divide = [0, 1]
    d = 2
    while d <= n:
        last, previous = previous + last, last
        division = last % m
        divide.append(division)
        if division == 1 and previous % m == 0:
            index = n % (d-1)
            return divide[index]
        d += 1
    return divide[-1]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
