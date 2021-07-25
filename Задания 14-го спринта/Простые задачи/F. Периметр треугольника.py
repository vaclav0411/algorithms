def perimeter_triangle(array: list):
    sorted_lengths = sorted(array, reverse=True)
    d = 0
    while d < len(sorted_lengths)-2:
        if sorted_lengths[d] < sorted_lengths[d+1] + sorted_lengths[d+2]:
            return sorted_lengths[d] + sorted_lengths[d+1] + sorted_lengths[d+2]
        d += 1
    return


if __name__ == '__main__':
    count = int(input())
    array = list(map(int, input().split()))
    print(perimeter_triangle(array))
