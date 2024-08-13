class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Point to itself, making it circular
            new_node.prev = new_node  # Point to itself, making it circular
        else:
            new_node.prev = self.tail  # Set the new node's previous to the current tail
            new_node.next = self.head  # Set the new node's next to the head
            self.tail.next = new_node  # Set the current tail's next to the new node
            self.head.prev = new_node  # Set the head's previous to the new node
            self.tail = new_node  # Update the tail to be the new node

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:  # If we've come full circle
                break
        print()
        
    def length(self):
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def insertAtfirst(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

    def removeAt(self, index: int):
        if self.head is None:
            raise ValueError("List is empty")
        elif index < 0 or index >= self.length():
            raise ValueError("Index out of range")
        else:
            current = self.head
            if index == 0:  # Removing the head
                if self.head == self.tail:  # Only one element
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif index == self.length() - 1:  # Removing the tail
                current = self.tail
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            else:  # Removing a middle element
                for _ in range(index):
                    current = current.next
                current.prev.next = current.next
                current.next.prev = current.prev

    def remove(self, value):
        if self.head is None:
            raise ValueError("List is empty")
        current = self.head
        index = 0
        while True:
            if current.data == value:
                self.removeAt(index)
                return
            current = current.next
            index += 1
            if current == self.head:  # If we've come full circle
                break
        raise ValueError("Value not found in the list")

# Example usage:
dll = DoubleCircularLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.insertAtfirst(5)

dll.display()  # Output: 5 10 20 30

dll.removeAt(1)
dll.display()  # Output: 5 20 30

dll.remove(20)
dll.display()  # Output: 5 30

dll.remove(5)
dll.display()  # Output: 30
