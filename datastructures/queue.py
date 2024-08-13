"""Queue implemented using linked list."""
from linked_list import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        nnode = Node(val)
        if not self.tail:
            self.head = self.tail = nnode
        else:
            self.tail.next = nnode
            self.tail = nnode

    def dequeue(self):
        if not self.head: raise StopIteration
        val, self.head = self.head.val, self.head.next
        return val


if __name__ == '__main__':
    q = Queue()
    lis = "All that glitters is not gold".split(" ")
    for a in lis:
        q.enqueue(a)
    try:
        while True:
            print(q.dequeue())
    except StopIteration:
        pass
