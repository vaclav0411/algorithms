# ID: 52146303
class Calculator:
    def __init__(self, input_):
        self.stack = []
        self.array = input_.split()

    def resolve(self):
        for i in self.array:
            if i.isdigit():
                self.stack.append(i)
            elif i == '+':
                n_1 = self.stack.pop()
                n_2 = self.stack.pop()
                plus = int(n_2) + int(n_1)
                self.stack.append(plus)
            elif i == '-':
                n_1 = self.stack.pop()
                n_2 = self.stack.pop()
                minus = int(n_2) - int(n_1)
                self.stack.append(minus)
            elif i == '*':
                n_1 = self.stack.pop()
                n_2 = self.stack.pop()
                multiply = int(n_2) * int(n_1)
                self.stack.append(multiply)
            elif i == '/':
                n_1 = self.stack.pop()
                n_2 = self.stack.pop()
                share = int(n_2) // int(n_1)
                self.stack.append(share)
            else:
                self.stack.append(i)
        return self.stack


if __name__ == "__main__":
    i = input()
    calc = Calculator(i)
    result = calc.resolve()
    print(result[-1])
