def factor_cookies(greedy: list, sizes: list):
    sort_children = sorted(greedy)
    sort_cookies = sorted(sizes)
    contentment = 0
    d = 0
    for i in sort_children:
        while d < len(sort_cookies):
            if i <= sort_cookies[d]:
                contentment += 1
                d += 1
                break
            d += 1
    return contentment


if __name__ == '__main__':
    n = int(input())
    greedy = list(map(int, input().split()))
    count = int(input())
    sizes = list(map(int, input().split()))
    print(factor_cookies(greedy, sizes))
