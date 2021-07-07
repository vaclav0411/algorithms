def solution(head, value):
    i = 0
    while head:
        if head.value == value:
            return i
        head = head.next_item
        i += 1
    return -1
