# ID: 52181183
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
        if self.items[self.tail] is None:
            raise EmptyDeque
        item = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
        self.tail -= 1
        return item

    def pop_front(self):
        if self.items[self.head] is None:
            raise EmptyDeque
        item = self.items[self.head]
        self.items[self.head] = None
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
        except (ValueError, SetDequeErrors):
            print('error')
        except AttributeError:
            raise ValueError(f'Вызов не существующего метода {command}')
