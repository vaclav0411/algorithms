class Fibonacci:
    def __init__(self, i, k):
        self.last_1 = 0
        self.last_2 = 0
        self.i = i
        self.k = k

    def fibonacci_mod(self):
        self.last_1 = self.last_2 = 1
        k = 10 ** self.k
        for d in range(1, i):
            number = self.last_2 + self.last_1
            self.last_1, self.last_2 = self.last_2, number % k
        return self.last_2


if __name__ == "__main__":
    list_input = list(map(int, input().split()))
    i = list_input[0]
    k = list_input[1]
    array = [None] * i
    fi = Fibonacci(i, k)
    print(fi.fibonacci_mod())
