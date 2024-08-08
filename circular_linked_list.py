class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head  # Point to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    
    def delete(self, data):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        previous = None
        while True:
            if current.data == data:
                if previous is None:  # Node to be deleted is the head
                    if current.next == self.head:  # Only one node
                        self.head = None
                    else:
                        previous = self.head
                        while previous.next != self.head:
                            previous = previous.next
                        self.head = current.next
                        previous.next = self.head
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
            if current == self.head:
                break
        print(f"Node with data {data} not found.")
    
    def display(self,key):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        while current:
            print(current.data,end=",")
            current=current.next
            if current == self.head:
                break
    
if __name__ == '__main__':
    circular_list = CircularLinkedList()
    circular_list.insert(10)
    circular_list.insert(20)
    circular_list.insert(30)
    circular_list.insert(40)
    circular_list.display("Circular Linked List")
    print()
    circular_list.delete(20)
    circular_list.display("After Deletion")
