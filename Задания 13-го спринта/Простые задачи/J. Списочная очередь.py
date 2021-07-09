class DoubleConnectedNode:
    def __init__(self, head, next_item=None, prev=None):
        self.head = head
        self.next = next_item
        self.prev = prev


class MyQueue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size_list = 0

    def get(self):
        if self.head:
            node = self.head
            del self.head
            self.head = node.next
            self.size_list -= 1
            return node.head
        else:
            return "error"

    def put(self, x):
        if self.size_list == 0:
            self.head = DoubleConnectedNode(x)
            self.tail = self.head
            self.size_list += 1
            return self.head.head
        else:
            node = DoubleConnectedNode(x, prev=self.tail.head)
            self.tail.next = node
            self.tail = node
            self.size_list += 1
            return self.tail.head

    def size(self):
        return self.size_list


if __name__ == "__main__":
    count = int(input())
    my_queue = MyQueue()

    for i in range(count):
        command = input().split()
        if command[0] == 'put':
            my_queue.put(command[1])
        if command[0] == 'get':
            print(my_queue.get())
        if command[0] == 'size':
            print(my_queue.size())
