import heapq
from collections import Counter


def huffman(s: str):
    if len(set(s)) == 1:
        count = len(s)
        return [[list(set(s))[0], '0']], '0' * count
    if len(s) < 1:
        return 0
    count = Counter()
    q = []
    amount_str = {i: '' for i in set(s)}
    new_d = {}
    for i in s:
        count.update({i: 1})
    for i in count:
        heapq.heappush(q, (count[i], i))

    for _ in range(len(q), 2 * len(q) - 1):
        n = heapq.heappop(q)
        m = heapq.heappop(q)
        frequency = n[0] + m[0]
        string = str(n[1]) + str(m[1])
        count.update({string: frequency})
        heapq.heappush(q, (frequency, string))
        new_d[n[1]] = '0'
        new_d[m[1]] = '1'

    for i in new_d:
        for j in i:
            amount_str[j] = amount_str[j] + new_d[i]
    result = [(i, amount_str[i][::-1]) for i in amount_str]
    result_str = s
    for i in result:
        result_str = result_str.replace(i[0], i[1])
    return sorted(result), result_str


if __name__ == '__main__':
    res = huffman(input())
    print(len(res[0]), len(res[1]))
    for k in res[0]:
        print(f'{k[0]}: {k[1]}')
    print(res[1])
