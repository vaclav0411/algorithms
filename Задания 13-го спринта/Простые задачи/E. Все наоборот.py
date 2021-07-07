def get_last_node(node):
    while node:
        if node.next is None:
            return node
        node = node.next


def solution(node):
    i = get_last_node(node)
    last_node = get_last_node(node)
    while last_node:
        if last_node.prev is None:
            return i
        last_node.next = last_node.prev
        last_node = last_node.prev
