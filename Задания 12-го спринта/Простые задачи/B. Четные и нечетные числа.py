def casino(l):
    u = l[0] % 2
    for i in l[1:]:
        if i % 2 != u:
            return 'FAIL'
    return 'WIN'


if __name__ == "__main__":
    list_ = list(map(int, input().split()))
    print(casino(list_))
