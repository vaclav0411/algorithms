def get_value(sentence):
    k = 0
    for i in range(1, len(sentence)):
        if len(sentence[i]) > len(sentence[k]):
            k = i
    return k


if __name__ == "__main__":
    count = int(input())
    sentence = input().split()
    value = get_value(sentence)
    print(sentence[value])
    print(len(sentence[value]))
