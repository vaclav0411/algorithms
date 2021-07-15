# ID: 52145901
class Deque:
    def __init__(self, max):
        self.max = max
        self.queue = []
        self.size = 0

    def push_back(self, value):
        if self.size < self.max:
            self.queue.append(value)
            self.size += 1
        else:
            print('error')

    def push_front(self, value):
        if self.size < self.max:
            self.queue = [value] + self.queue
            self.size += 1
        else:
            print('error')

    def pop_back(self):
        if self.queue:
            x = self.queue.pop()
            self.size -= 1
            return x
        else:
            return 'error'

    def pop_front(self):
        if self.queue:
            x = self.queue.pop(0)
            self.size -= 1
            return x
        else:
            return 'error'


if __name__ == "__main__":
    c = int(input())
    m = int(input())
    deq = Deque(m)
    for i in range(c):
        command = input().split()
        if command[0] == 'push_back':
            deq.push_back(command[1])
        elif command[0] == 'push_front':
            deq.push_front(command[1])
        elif command[0] == 'pop_back':
            print(deq.pop_back())
        elif command[0] == 'pop_front':
            print(deq.pop_front())
