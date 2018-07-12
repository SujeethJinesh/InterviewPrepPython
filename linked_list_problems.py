class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


def _make_singly_linkedlist(values):
    nodes = [Node(value) for value in values]
    head = nodes.pop(0)
    previous = head
    for node in nodes:
        previous.next = node
        previous = node
    tail = previous
    return head, tail


def _print_linkedlist(head: Node):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


def detect_loop_in_linkedlist(head: Node):
    if head is None:
        return "No Loop Detected"

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return "Loop detected"
        slow = slow.next
        fast = fast.next.next

    return "No loop detected"


if __name__ == '__main__':
    head_node, tail_node = _make_singly_linkedlist([1, 2, 3, 4, 5])
    tail_node.next = head_node  # making loop
    print(detect_loop_in_linkedlist(head_node))
