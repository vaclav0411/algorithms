def flower_beds(beds: list):
    right_bed = beds[0][1]
    left_bed = beds[0][0]
    for i in range(1, len(beds)):
        if right_bed >= beds[i][0] and right_bed < beds[i][1]:
            right_bed = beds[i][1]
        elif beds[i][0] > right_bed:
            print(f'{left_bed} {right_bed}')
            left_bed = beds[i][0]
            right_bed = beds[i][1]
    print(f'{left_bed} {right_bed}')


if __name__ == '__main__':
    gardeners = int(input())
    array = [list(map(int, input().split())) for i in range(gardeners)]
    sort = sorted(array, key=lambda x: [x[0], -x[1]])
    flower_beds(sort)
