def conference_lovers(array: list, top: int):
    id_universe = dict()
    for i in array:
        if not id_universe.get(i, None):
            id_universe[i] = 1
        else:
            id_universe[i] += 1
    for_sort = [[value, int(key)] for key, value in id_universe.items()]
    sort = sorted(for_sort, key=lambda x: -x[0])[:top]
    result = [i[1] for i in sort]
    return result


if __name__ == '__main__':
    students = int(input())
    id_s = input().split()
    first_top = int(input())
    result = conference_lovers(id_s, first_top)
    print(' '.join(map(str, result)))
