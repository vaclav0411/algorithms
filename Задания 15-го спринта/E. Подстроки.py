def unique_letters(string: str):
    count = {}
    accumulator = []
    list_arr = list(string)
    d = 0
    while d < len(list_arr):
        if list_arr[d] in accumulator:
            index = accumulator.index(list_arr[d])
            count[len(accumulator[:d])] = accumulator[:d]
            del accumulator[:index+1]
        accumulator.append(list_arr[d])
        d += 1
    values = [[k, v] for k, v in count.items()]
    max_count = max(list(map(lambda x: x[0], values))+[0])
    if len(accumulator) > max_count:
        return accumulator
    return count.get(max_count)


if __name__ == "__main__":
    s = input()
    result = unique_letters(s)
    print(result)
