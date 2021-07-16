# ID: 52170611
class ExcessElements(Exception):
    pass


class EmptyDeque(Exception):
    pass


class Deque:
    def __init__(self, max):
        self.max = max
        self.items = [None] * self.max
        self.tail = 0
        self.head = 0
        self.size = 0

    def push_back(self, value):
        if self.size >= self.max:
            raise ExcessElements('error')
        else:
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.max
            self.size += 1

    def push_front(self, value):
        if self.size >= self.max:
            raise ExcessElements('error')
        else:
            self.head = (self.head - 1) % self.max - self.max
            self.items[self.head] = value
            self.size += 1

    def pop_back(self):
        if not self.items[self.tail-1]:
            raise EmptyDeque('error')
        else:
            self.tail -= 1
            x = self.items[self.tail]
            self.items[self.tail] = None
            self.size -= 1
            return x

    def pop_front(self):
        if not self.items[self.head]:
            raise EmptyDeque('error')
        else:
            x = self.items[self.head]
            self.items[self.head] = None
            self.head += 1
            self.size -= 1
            return x


if __name__ == "__main__":
    COMMANDS = ('push_back', 'push_front', 'pop_front', 'pop_back')
    count = int(input())
    deq = Deque(int(input()))
    for i in range(count):
        cmd, *prms = input().split()
        get_method = getattr(deq, cmd, 'error')(*prms)
        if get_method:
            print(get_method)
