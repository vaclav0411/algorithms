count = int(input())
arr = []
for _ in range(count):
    circle = input()
    if circle in arr:
        continue
    arr.append(circle)

print('\n'.join(arr))
