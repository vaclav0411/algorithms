# ID: 52177735
class SetDequeErrors(Exception):
    pass


class ExcessElements(SetDequeErrors):
    pass


class EmptyDeque(SetDequeErrors):
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
            raise ExcessElements
        self.size += 1
        if not self.items[self.tail]:
            self.items[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.max
            self.items[self.tail] = value

    def push_front(self, value):
        if self.size >= self.max:
            raise ExcessElements
        self.size += 1
        if not self.items[self.head]:
            self.items[self.head] = value
        else:
            self.head = (self.head - 1) % self.max - self.max
            self.items[self.head] = value

    def pop_back(self):
        if not self.items[self.tail] and self.size <= 0:
            raise EmptyDeque
        item = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
        if self.size >= 1:
            self.tail -= 1
            return item
        return item

    def pop_front(self):
        if not self.items[self.head]:
            raise EmptyDeque
        item = self.items[self.head]
        self.items[self.head] = None
        self.size -= 1
        if self.size >= 1:
            self.head += 1
            return item
        return item


if __name__ == "__main__":
    count = int(input())
    deq = Deque(int(input()))
    for _ in range(count):
        command, *parameters = input().split()
        try:
            get_method = getattr(deq, command)(*parameters)
            if get_method:
                print(get_method)
        except (TypeError, SetDequeErrors):
            print('error')
