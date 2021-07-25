# ID: 52184612
OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


class Stack:
    def __init__(self):
        self.array = []

    def push(self, x):
        self.array.append(x)

    def pop(self):
        try:
            return self.array.pop()
        except IndexError:
            raise IndexError('Пустой стек')


def calculator(array, stack=None, converter=int, operations=OPERATIONS):
    stack = Stack() if stack is None else stack
    for item in array:
        if item in operations:
            number_2, number_1 = stack.pop(), stack.pop()
            stack.push(operations[item](number_1, number_2))
            continue
        try:
            stack.push(converter(item))
        except ValueError:
            raise ValueError(f'Нельзя преобразовать {item} в {converter.__name__}')
    return stack.pop()


if __name__ == "__main__":
    print(calculator(input().split()))
