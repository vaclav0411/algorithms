def del_symbols(s):
    st = str()
    symbols = ('?', '*', ':', ';', '.', ',', '@', '!', ' ')
    for i in s:
        if i not in symbols:
            st += i
    return st


def check_palindrom(s):
    reversed_str = s[::-1]
    return s == reversed_str


if __name__ == "__main__":
    s = input().lower()
    print(check_palindrom(del_symbols(s)))
