class HeapList:
    def __init__(self):
        self.array = list()
        self.size = 0

    def swap(self, x, y):
        arg = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = arg
        return self

    def insert(self, value: int):
        self.array.append(value)
        current = len(self.array) - 1
        height = current // 2
        if self.array[height] > self.array[current]:
            self.swap(height, current)
        self.size += 1
        return

    def extract(self):
        return self.array.pop()


if __name__ == '__main__':
    n = int(input())
    h = HeapList()
    for i in range(n):
        command, *args = input().split()
        if command == 'Insert':
            h.insert(*args)
        elif command == 'ExtractMax':
            print(h.extract())
