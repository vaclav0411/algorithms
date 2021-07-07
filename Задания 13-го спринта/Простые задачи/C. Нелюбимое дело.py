def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(head, index):
    if index == 0:
        next_node = head.next_item
        del head
        return next_node
    previous_node = get_node_by_index(head, index-1)
    current_node = get_node_by_index(head, index)
    previous_node.next_item = current_node.next_item
    del current_node
    return head
