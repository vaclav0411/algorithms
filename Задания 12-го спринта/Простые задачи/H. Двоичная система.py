def to_binary(a, b):
    if len(a) < len(b):
        zeros = [0] * (len(b) - len(a))
        a = zeros + a
    elif len(b) < len(a):
        zeros = [0] * (len(a) - len(b))
        b = zeros + b

    result = str()
    remainder = 0
    for i in range(len(a)-1, -1, -1):
        if a[i] + b[i] + remainder <= 1:
            result += str(a[i] + b[i] + remainder)
            remainder = 0
        elif a[i] + b[i] + remainder == 2:
            result += '0'
            remainder = 1
        else:
            result += '1'
            remainder = 1
    if remainder == 1:
        result += '1'
    return result


if __name__ == "__main__":
    a = [int(i) for i in input()]
    b = [int(i) for i in input()]
    print(to_binary(a, b)[::-1])