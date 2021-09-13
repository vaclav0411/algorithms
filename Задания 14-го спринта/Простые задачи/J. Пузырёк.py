def bubble(array, n):
    result = []
    for i in range(n-1):
        flag = True
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False
            else:
                continue
        if flag:
            if i < 2:
                result.append(' '.join(list(map(str, array))))
                return result
            return result
        result.append(' '.join(list(map(str, array))))
    return result


if __name__ == "__main__":
    count = int(input())
    numbers = list(map(int, input().split()))
    result_to_print = '\n'.join(bubble(numbers, count))
    print(result_to_print)
