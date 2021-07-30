def polynomial_hash(s: str, q: int, r: int, l: int):
    if not s:
        return 0
    result = ord(s[0])
    for i in range(1, l):
        result = (result * q + ord(s[i])) % r
    return result


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    string = input()
    print(polynomial_hash(string, n, m, len(string)))
