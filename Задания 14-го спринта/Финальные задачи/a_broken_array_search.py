# ID: 52217312
def broken_array(nums: list):
    high = len(nums)
    low = 0
    while low <= high:
        mid = (high + low) // 2
        next_item = (mid + 1) % len(nums)
        prev_item = (mid - 1) % len(nums)
        if nums[mid] > nums[-1]:
            low = mid
        elif nums[mid] < nums[-1]:
            high = mid
        if nums[mid] > nums[next_item]:
            return next_item
        elif nums[mid] < nums[prev_item]:
            return mid
    return -1


def binary_search(nums: list, target: int, start: int, stop: int):
    low = start
    high = stop
    while low <= high:
        mid = (high + low) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        elif guess < target:
            low = mid + 1
    return -1


def broken_search(nums: list, target: int):
    if nums[-1] < nums[0]:
        broken = broken_array(nums)
    else:
        broken = 0
    count = len(nums) - 1
    if target < nums[-1]:
        return binary_search(nums, target, broken, count)
    elif target > nums[-1]:
        return binary_search(nums, target, 0, broken)
    elif target == nums[-1]:
        return count
    return -1
