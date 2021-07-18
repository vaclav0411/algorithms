# ID: 52178567
class EmptyArray(Exception):
    pass


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
            popped = self.array.pop()
            return popped
        except IndexError:
            raise EmptyArray('Пустой стек')


def calculator(array, stack=Stack(), converter=int, operations=OPERATIONS):
    for item in array:
        if item in operations:
            try:
                number_1 = stack.pop()
                number_2 = stack.pop()
                operate = operations[item](number_2, number_1)
                stack.push(operate)
            except ZeroDivisionError:
                raise ZeroDivisionError('Деление на ноль')
            except IndexError:
                raise EmptyArray('Пустой стек')
            except KeyError:
                raise KeyError(f'{item} нет в OPERATIONS')
        else:
            try:
                value = converter(item)
                stack.push(value)
            except Exception as error:
                raise error
    result = stack.array[-1]
    return result


if __name__ == "__main__":
    resolve = calculator(input().split())
    print(resolve)
