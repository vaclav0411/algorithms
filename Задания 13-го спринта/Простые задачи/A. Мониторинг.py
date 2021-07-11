if __name__ == "__main__":
    r = int(input())
    c = int(input())
    matrix = ['' for i in range(c)]
    for i in range(r):
        m = input().split()
        for j in range(len(m)):
            matrix[j] += ' ' + m[j]
    p = [i.strip() for i in matrix]
    print('\n'.join(p))
