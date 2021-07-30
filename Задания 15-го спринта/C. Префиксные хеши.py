def polynomial_hash(s: list, q: int, r: int):
    if not s:
        return 0
    result = s[0]
    for i in range(1, len(s)):
        result = (result * q + s[i]) % r
    return result % r


def sliding_window(number: int, s: list, start: int, finish: int, q, r):
    begin = polynomial_hash(s[:start], q, r)
    end = polynomial_hash(s[finish+1:], q, r)
    result = (number - begin) * 1


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    string = list(map(ord, list(input())))
    count = int(input())
    expression = polynomial_hash(string, n, m)
    print(expression)
    for _ in range(count):
        start, finish = map(int, input().split())
