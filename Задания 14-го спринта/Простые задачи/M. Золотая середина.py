from statistics import mean


def golden_mean(array):
    median_1 = mean(array[0])
    median_2 = mean(array[1])
    return (median_1 + median_2) // 2


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    array = [list(map(int, input().split())) for _ in range(2)]
    print(golden_mean(array))
