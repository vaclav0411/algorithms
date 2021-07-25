# ID: 52219782
from collections import namedtuple


User = namedtuple('User', 'problems penalty name')


def distribute_value(name: str, problems: int, penalty: int):
    return User(-int(problems), int(penalty), name)


def quick_sort(users: list, start, finish):
    if finish - start <= 0:
        return
    index, mobile = start, start
    pivot = users[finish]
    while mobile < finish:
        if users[mobile] < pivot:
            users[index], users[mobile] = users[mobile], users[index]
            index += 1
        mobile += 1
    users[index], users[mobile] = users[mobile], users[index]
    quick_sort(users, start, index-1)
    quick_sort(users, index+1, finish)


if __name__ == '__main__':
    n = int(input())
    array = [distribute_value(*input().split()) for _ in range(n)]
    quick_sort(array, 0, len(array)-1)
    print('\n'.join([i.name for i in array]))
