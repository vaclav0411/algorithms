def to_binary(n):
    result = str()
    while n > 0:
        result += str(n % 2)
        n = n // 2
    return result[::-1]


if __name__ == "__main__":
    number = int(input())
    print(to_binary(number))
