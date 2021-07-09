class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.tail = 0
        self.head = 0
        self.size_list = 0

    def push(self, x):
        if self.size_list < self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size_list += 1
        else:
            print('error')

    def pop(self):
        if self.size_list == 0:
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_list -= 1
        return x

    def peek(self):
        if self.size == 0:
            return 'error'
        first_number = self.queue[self.head]
        return first_number

    def size(self):
        if self.size == 0:
            return 'error'
        return self.size_list


if __name__ == "__main__":
    count = int(input())
    max_size = int(input())
    my_queue = MyQueueSized(max_size)
    for i in range(count):
        command = input().split()
        if command[0] == 'push':
            my_queue.push(command[1])
        elif command[0] == 'pop':
            print(my_queue.pop())
        elif command[0] == 'peek':
            print(my_queue.peek())
        elif command[0] == 'size':
            print(my_queue.size())
