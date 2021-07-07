def unique_letter(s, t):
    k = t[:]
    for i in range(len(s)):
        if s[i] in t:
            k.pop(k.index(s[i]))
    return k


if __name__ == "__main__":
    s = list(input())
    t = list(input())
    unique = str()
    print(unique_letter(s, t)[0])
