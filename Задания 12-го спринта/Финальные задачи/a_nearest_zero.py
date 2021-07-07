# A. Ближайший ноль
# ID: 52072908
class GetNearestZero:
    def __init__(self, array):
        self.array = array

    def get_right_zero(self, index):
        for i in range(index+1, len(self.array)):
            if self.array[i] == 0:
                return i
        return float('inf')

    def get_nearest_zero(self):
        right_zero = self.array.index(0)
        left_zero = float('inf')
        result = list()
        for i in range(len(self.array)):
            if i == right_zero:
                left_zero = right_zero
                right_zero = self.get_right_zero(i)
                result.append(0)
            elif right_zero - i <= abs(left_zero - i):
                result.append(right_zero - i)
            elif abs(left_zero - i) < right_zero - i:
                result.append(abs(left_zero - i))
        return result


if __name__ == "__main__":
    count = int(input())
    array = list(map(int, input().split()))
    get_zero = GetNearestZero(array)
    result = get_zero.get_nearest_zero()
    print(' '.join(list(map(str, result))))
