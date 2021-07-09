def is_correct_bracket_seq(n):
    string = n
    for i in n:
        pass


# Слишком долгое решение(написать новое, либо оптимизировать)
"""
def is_correct_bracket_seq(n):
    p = list(n)
    result = 0
    brackets = {
        '[': ']',
        '(': ')',
        '{': '}',
    }
    if not n:
        return True
    for i in range(len(p)):
        if p[i] in brackets:
            for j in range(len(p[i:])):
                if p[i+j] == ')' and brackets.get(p[i]) == ')':
                    p[i+j] = False
                    result += 1
                if p[i+j] == '}' and brackets.get(p[i]) == '}':
                    p[i+j] = False
                    result += 1
                if p[i+j] == ']' and brackets.get(p[i]) == ']':
                    p[i+j] = False
                    result += 1

    return result == len(p)/2


if __name__ == '__main__':
    n = input()
    print(is_correct_bracket_seq(n))
"""

