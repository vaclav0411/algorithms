def sequence(array_1, array_2):
    d = 0
    index = 0
    while d < len(array_2) and index < len(array_1):
        if array_1[index] == array_2[d]:
            index += 1
        d += 1
    return index == len(array_1)


if __name__ == "__main__":
    s = list(input())
    t = list(input())
    print(sequence(s, t))
