class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

    def insertAtLast(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = node
            node.next = self.head

    def insertAtFirst(self, val):
        node = Node(val)
        if self.head is None:
            self.head = val
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            node.next = self.head
            curr.next = node
            self.head = node

    def append(self, *args):
        for val in args:
            self.insertAtLast(val)

    def _length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count

    def insertAt(self, value, position):
        if position < 0 or position > self._length():
            raise IndexError("Invalid position")
        if position == 0:
            self.insertAtFirst(value)
        if position == self._length():
            self.insertAtLast(value)
        else:
            curr = self.head
            node = Node(value)
            for _ in range(position - 1):
                curr = curr.next
                if curr == self.head:
                    raise IndexError("Invalid position")

            node.next = curr.next
            curr.next = node

    def pop(self):
        if not self.head:
            raise IndexError("List is empty")
        if self.head.next == self.head:
            val = self.head.val
            self.head = None
            return val
        curr = self.head
        prev = None
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr == self.head:
                raise IndexError("Invalid position")
        prev.next = curr.next
        val = curr.val
        return val

    def reverse(self):
        if not self.head:
            return
        current = self.head
        prev = None
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head.next = prev
        self.head = prev

    def index(self, value):
        try:

            index = -1
            current = self.head
            while current.next != self.head:
                index += 1
                if current.val == value:
                    return index
                current = current.next
            return -1

        except Exception as e:
            raise e

    def removeAt(self, index):
        print(f"index {index}")
        if index < 0 or index >= self._length():
            raise IndexError("Invalid position")
        if index == 0:
            self.head = self.head.next
            if self.head.next == self.head:
                self.head = None
            return True
        current = self.head
        prev = None
        for _ in range(index - 1):
            prev = current
            current = current.next

            if current.next == self.head:
                raise IndexError("Invalid position")
        prev.next = current.next
        return True

    def remove(self, value):
        if not self.head:
            return
        index = self.index(value)
        self.removeAt(index)


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(9, 28, 2, 1, 3, 78)
    # cll.print()
    # cll.insertAtFirst(71)
    # cll.print()
    # cll.insertAt(6, 7)
    # cll.print()
    # print(cll.remove(28))
    cll.print()
    print(cll.pop())
    cll.print()
    cll.reverse()
    cll.print()
