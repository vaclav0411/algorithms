class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')


if __name__ == "__main__":
    c = int(input())
    s = StackMax()
    for i in range(c):
        k = input().split()
        if k[0] == 'get_max':
            s.get_max()
        elif k[0] == 'pop':
            s.pop()
        elif k[0] == 'push':
            s.push(int(k[1]))
