class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def add_last(self, val):
        node = Node(val)

        if self.head is None:
            self.head = node

        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def get(self, index: int) -> int:
        traverse_pointer = self.head
        while index > 0:
            if traverse_pointer is None:
                return -1

            traverse_pointer = traverse_pointer.next

            index -= 1
        if traverse_pointer:
            return traverse_pointer.val
        else:
            return -1
    def print_list(self):
        if self.head:
            traverse_pointer = self.head
            while traverse_pointer is not None:
                print(traverse_pointer.val, end=",")
                traverse_pointer = traverse_pointer.next
        else:
            print(self.head)

    def add_at_index(self, index: int, val: int) -> None:
        traverse_pointer = self.head
        while index > 0:
            if traverse_pointer is None:
                return None

            traverse_pointer = traverse_pointer.next

            index -= 1
        if traverse_pointer:
            node = Node(val)
            node.prev = traverse_pointer.prev
            node.next = traverse_pointer
            traverse_pointer.prev = node
            # node.next = traverse_pointer.next
            # node.prev = traverse_pointer
            # traverse_pointer.next = node

        else:
            self.add_last(val)

    def print_reverse(self):
        if self.tail:
            traverse_pointer = self.tail
            while traverse_pointer is not None:
                print(traverse_pointer.val, end=",")
                traverse_pointer = traverse_pointer.prev
        else:
            print(self.tail)


new_list = DoublyLinkedList()
new_list.print_list()
new_list.add_first(5)
# new_list.print_list()
new_list.add_first(10)
# new_list.print_list()
new_list.add_first(15)
new_list.add_last(20)
print(new_list.get(3))
new_list.add_at_index(1,100)
new_list.print_list()
# new_list.print_reverse()
