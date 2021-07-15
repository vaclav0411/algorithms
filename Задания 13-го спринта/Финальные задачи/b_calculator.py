# ID: 52164052
OPERATIONS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            return popped
        return 'error'


def calculator(array):
    stack = Stack()
    for i in array:
        value = i.lstrip('-')
        if value.isdigit():
            number = int(i)
            stack.push(number)
        else:
            for j in OPERATIONS:
                if i == j:
                    number_1 = stack.pop()
                    number_2 = stack.pop()
                    result = OPERATIONS[j](number_2, number_1)
                    stack.push(result)
    return stack


if __name__ == "__main__":
    resolve = calculator(input().split())
    result = resolve.stack[-1]
    print(result)
