class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        current = self.head
        while current:  # Ensure to count the last node
            count += 1
            current = current.next
        return count

    def print(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print()

    def _insertAtFirst(self, value):
        new_node = Node(value)
        new_node.next = self.head  # Properly link the new node
        self.head = new_node

    def _insertAtLast(self, value):
        if self.head is None:
            self._insertAtFirst(value)
        else:
            new_node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, value, index: int = None):
        if index is None:  # Correctly check if index is None
            self._insertAtLast(value)
        else:
            length = self.length()
            if index > length or index < 0:
                raise IndexError("Index out of range")
            new_node = Node(value)
            if index == 0:
                self._insertAtFirst(value)
            elif index == length:
                self._insertAtLast(value)
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def delete(self, value):
        if self.head is not None:
            if self.head.data == value:
                self.head = self.head.next
                return
            current = self.head
            while current.next and current.next.data != value:
                current = current.next
            if current.next:
                current.next = current.next.next
            else:
                raise ValueError("Value not found in the list")
        else:
            raise ValueError("List is empty")

    def deleteAt(self, index: int):
        if index < 0 or index > self.length():
            raise IndexError("Index out of range")
        if self.head is None:
            raise ValueError("List is empty")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        if current.next:
            current.next = current.next.next
            return
        else:
            raise ValueError("Index out of range")

    def sort(self, reverse=False):
        current = self.head
        if current is None:
            return
        keys = []
        while current:
            keys.append(current.data)
            current = current.next
        keys.sort(reverse=reverse)
        self.head = None
        for k in keys:
            self._insertAtLast(k)

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.print()  # Output: 1->2->3->
    ll.insert(4, 1)  # Inserting 4 at index 1
    ll.print()  # Output: 1->4->2->3->
    # ll.delete(3)
    ll.print()  # Output: 1->4->2->
    # ll.deleteAt(1)
    ll.print()  # Output: 1->2->
    # ll.sort(True)
    ll.print()  # Output: 1->2->4->
    ll.reverse()
    ll.print()  # Output: 4->2->1->
