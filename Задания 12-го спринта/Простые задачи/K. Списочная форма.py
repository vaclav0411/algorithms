from functools import reduce


count = int(input())

first_number = int(reduce(lambda x, y: x+y, input().split()))
second_number = int(reduce(lambda x, y: x+y, input().split()))
summing = first_number + second_number
print(' '.join(list(str(summing))))
