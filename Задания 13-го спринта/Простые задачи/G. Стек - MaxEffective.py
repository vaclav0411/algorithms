class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_numbers = []

    def push(self, x):
        if self.max_numbers:
            if x > self.max_numbers[-1]:
                self.max_numbers.append(x)
            else:
                self.max_numbers.append(x)
                self.max_numbers = sorted(self.max_numbers)
        else:
            self.max_numbers.append(x)
        self.items.append(x)

    def pop(self):
        if self.items:
            if self.max_numbers:
                if self.items[-1] == self.max_numbers[-1]:
                    self.max_numbers.pop()
                    return self.items.pop()
                else:
                    self.max_numbers.remove(self.items[-1])
                    return self.items.pop()
            else:
                return self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(self.max_numbers[-1])
        else:
            print('None')


if __name__ == "__main__":
    c = int(input())
    s = StackMaxEffective()
    for i in range(c):
        k = input().split()
        if k[0] == 'get_max':
            s.get_max()
        elif k[0] == 'pop':
            s.pop()
        elif k[0] == 'push':
            s.push(int(k[1]))
