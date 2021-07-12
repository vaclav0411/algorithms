def is_correct_brackets(n):
    while '()' in n or '{}' in n or '[]' in n:
        n = n.replace('{}', '')
        n = n.replace('()', '')
        n = n.replace('[]', '')
    return not n


if __name__ == "__main__":
    text = input()
    print(is_correct_brackets(text))
