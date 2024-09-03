"""Linked list implementation."""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


if __name__ == '__main__':
    head = cur = Node('dummy')
    for a in range(10):
        cur.next = Node(a)
        cur = cur.next
    cur = head
    while cur.next:
        print(cur.next.val)
        cur = cur.next
