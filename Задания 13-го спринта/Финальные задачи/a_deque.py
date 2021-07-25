# ID: 52184548
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
        self.head = 1
        self.size = 0

    def push_back(self, value):
        if self.size >= self.max:
            raise ExcessElements
        self.size += 1
        self.tail = (self.tail + 1) % self.max
        self.items[self.tail] = value

    def push_front(self, value):
        if self.size >= self.max:
            raise ExcessElements
        self.size += 1
        self.head = (self.head - 1) % self.max
        self.items[self.head] = value

    def pop_back(self):
        if self.size <= 0:
            raise EmptyDeque
        item = self.items[self.tail]
        self.size -= 1
        self.tail = (self.tail - 1) % self.max
        return item

    def pop_front(self):
        if self.size <= 0:
            raise EmptyDeque
        item = self.items[self.head]
        self.size -= 1
        self.head = (self.head + 1) % self.max
        return item


if __name__ == "__main__":
    count = int(input())
    deque = Deque(int(input()))
    for _ in range(count):
        command, *parameters = input().split()
        try:
            get_value = getattr(deque, command)(*parameters)
            if get_value is not None:
                print(get_value)
        except SetDequeErrors:
            print('error')
        except AttributeError:
            raise ValueError(f'Вызов несуществующего метода {command}')
