# На вход подаётся целое число в диапазоне от 1 до 10000.
def check_degree_of_four(n):
    degree_list = [4**i for i in range(6)]
    return n in degree_list


if __name__ == "__main__":
    number = int(input())
    print(check_degree_of_four(number))
