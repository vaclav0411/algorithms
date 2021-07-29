def check_index(squares, middle, k_position):
    left = count = 0
    for right in range(len(squares)):
        val_right = squares[right]
        val_left = squares[left]
        while val_right - val_left > middle:
            left += 1
            val_left = squares[left]
        count += right - left
        if count >= k_position:
            return True
    return False


def diff(quantity, squares, k_position):
    squares.sort()
    left, right = 0, squares[-1] - squares[0]
    while left < right:
        middle = (left + right) // 2
        if check_index(squares, middle, k_position):
            right = middle
        else:
            left = middle + 1
    return left


if __name__ == '__main__':
    squares = [1, 2, 3, 4, 5]
    print(diff(len(squares), squares, 10))
