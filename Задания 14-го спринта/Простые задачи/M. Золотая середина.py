def golden_mean(array, n):
    if n % 2 == 0:
        return (array[n//2] + array[(n//2-1)]) / 2
    return array[n//2]


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    full_array = list(map(int, input().split())) + list(map(int, input().split()))
    print(full_array)
    print(golden_mean(sorted(full_array), n+m))
