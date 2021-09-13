def crazy_comparing(string_1: str, string_2: str):
    if len(string_1) != len(string_2):
        return 'No'
    new_d = {}
    for i, v in enumerate(string_1):
        if v in new_d:
            if new_d[v] != string_2[i]:
                return 'No'
        elif v not in new_d:
            if [j for j in new_d if new_d.get(j) == string_2[i]]:
                return 'No'
            new_d[v] = string_2[i]
    return 'Yes'


if __name__ == "__main__":
    s_1 = input()
    s_2 = input()
    print(crazy_comparing(s_1, s_2))
