# B. Ловкость рук
# ID: 52072752
import re


def speed_print(amount, limit):
    signs = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    count = 0
    s = [len(re.findall(i, str(amount))) for i in signs]

    for i in s:
        if 0 < i <= limit:
            count += 1
    return count


if __name__ == "__main__":
    limit = 2 * int(input())
    amount = input() + input(), input(), input()
    result = speed_print(amount, limit)
    print(result)

