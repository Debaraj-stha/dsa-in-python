from hashlib import new


class Node:
    def __init__(self,key):
        self.key=key
        self.prev=None
        self.next=None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def length(self):
        count=0
        current=self.head
        while True:
            current=current.next
            count+=1
            if  current is self.head:
                break
        return count
        
    def insertAtFirst(self,key):
        new_node=Node(key)
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
            
    def insertAtLast(self,key):
        if self.head is None:
            self.insertAtFirst(key)
        else:
            new_node=Node(key)
            new_node.prev=self.tail
            new_node.next=self.head
            self.tail.next=new_node
            self.head.prev=new_node
            self.tail=new_node
            
    def insertAt(self,key,index:int):
        if self.head is None:
            self.insertAtFirst(key)
        elif index < 0 or index > self.length():
            raise IndexError("Index out of range")
        elif index==self.length()+1:
            self.insertAtLast(key)
        else:
            print("else")
            prev=None
            current=self.head
            for i in range(index):
                prev=current
                current=current.next
                if current==prev:
                    raise IndexError("Index out of range")
            new_node=Node(key)
            new_node.next=current
            new_node.prev=prev
            current.prev=new_node
            prev.next=new_node

    def removeAt(self,index):
        if self.head is None:
            raise ValueError("List is empty")
        elif index<0 or  index>=self.length():
            raise IndexError("Index out of range")
        else:
            prev=None
            current=self.head
            for i in range(index): #traversing the list  to index
                prev=current
                current=current.next
                if current==prev:
                    raise IndexError("Index out of range")
            prev.next=current.next #removing the given index from list
    def remove(self,key):
        if self.head is None:
            raise ValueError("List is empty")
        elif self.head.key==key: #checking if key is head node
            self.removeAt(0)
            return
        prev=None
        current=self.head
        while current.key!=key:
            prev=current
            current=current.next
            if current==prev:
                raise ValueError("Key not found in the list")
       
            if current == self.head:  # Removing the head node
                if self.head == self.tail:  # List has only one node
                    self.head = None
                    self.tail = None    
                else:
                    self.head = current.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:  # Removing a node other than the head
                prev.next = current.next
                current.next.prev = prev
                if current == self.tail:  # Removing the tail node
                    self.tail = prev
    def append(self,*args):
        for key in args:
            self.insertAtLast(key)
            
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.key, end=" ")
            current = current.next
            if current == self.head:  # If we've come full circle
                break
        print()
    def findIndexOf(self, key): #return index of given elements
        current=self.head
        index=0
        while current:
            if current.key==key:
                return index
            current=current.next
            index+=1
        return -1
    
    def contains(self, key): #check if list contains given element
        current=self.head
        while current:
            if current.key==key:
                return True
            current=current.next
        return False
    
    def reverse(self):
        if self.head is None:
            return
        
        current = self.head
        prev = None
        
        while True:
            # Swap the next and prev pointers
            next_node = current.next
            current.next = prev
            current.prev = next_node
            
            prev = current
            current = next_node
            
            # If we've looped back to the head, break the loop
            if current == self.head:
                break
        
        # Adjust the head and tail
        self.tail = self.head
        self.head = prev
        
        # Fix the circular reference
        self.head.prev = self.tail
        self.tail.next = self.head
    def sort(self,reverse=False):
        if self.head is None:
            return
        
        # Convert the list to a list
        nodes = []
        current = self.head
        while True:
            nodes.append(current.key)
            current = current.next
            if current == self.head:
                break
        
        # Sort the list
        nodes.sort(reverse=reverse)
        
        # Convert the sorted list back to a circular double linked list
        self.head = None
        self.tail = None
        for key in nodes:
            self.insertAtLast(key)
    
if __name__=="__main__":
    cdl=CircularDoubleLinkedList()
    cdl.insertAtFirst(3)
    cdl.insertAtFirst(4)
    cdl.insertAtLast(10)
    cdl.insertAt(6,2)
    cdl.display()
    cdl.remove(3)
    cdl.append(5,9,10,41)
    i=cdl.findIndexOf(5)
    cdl.display()
    cdl.reverse()
    print(f"Index of 5 is {i}")
    cdl.display()
    cdl.sort()
    cdl.display()