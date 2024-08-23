class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
        
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
            if temp == self.head:
                break
        print()
        
    def length(self):
        count=0
        current=self.head
        while True:
            current=current.next
            count+=1
            if current == self.head:
                break
        return count
    
    
    def insertAtFirst(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

        

    def insertAtLast(self, data):
        new_node=Node(data)
        if self.head is None:
            self.insertAtFirst(data)
        else:
            current=self.head
            while current.next !=self.head:
                current=current.next
            current.next=new_node
            new_node.next=self.head
            
    def insertAt(self,index,key):
        if index<0 or index>self.length():
            raise IndexError("Index out of range")
        new_node=Node(key)
        if index==0:
            self.insertAtFirst(key)
        elif index==self.length():
            self.insertAtLast(key)
        else:
            current=self.head
            for _ in range(index-1):
                current=current.next
            new_node.next=current.next
            current.next=new_node
            
    def deleteAt(self,index:int):
        if index < 0 or index > self.length()-1:
            raise IndexError("Index out of range")
        if self.head is None:
            raise ValueError("List is empty")
        if index==0:
            temp=self.head
            if temp==self.head.next:
                self.head=None
            else:
                current=self.head
                while current.next!=self.head:
                    current=current.next
                current.next=self.head.next
                self.head=self.head.next
        else:
            current=self.head
            for i in range(index-1):
                current=current.next
            current.next=current.next.next
            
            
    def indexOf(self,value):
        index=0
        current=self.head
        while current.next!=self.head:
            if current.data==value:
                return index
            current=current.next
            index+=1
    def delete(self, value):
        if self.head is None:
            raise ValueError("List is empty")
        index=self.indexOf(value)
        if index is None:
            raise ValueError("element not found")

        self.deleteAt(index)
    
    def reverse(self):
        if self.head is None:
            return
        current = self.head
        prev = None
        next_node = None
        while True:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
            if current == self.head:
                break
        self.head.next=prev
        self.head=prev
        
    def sort(self,reverse=True):
       if self.head is None:
           return
       current=self.head
       key=[]
       while True:
            current=current.next
            key.append(current.data)
            if current == self.head:
                break
       key.sort(reverse=reverse)
       self.head=None
       for k in key:
           self.insertAtFirst(k)
           
    def append(self,**args):
        for key in args:
            self.insertAtLast(key)
         
    

if __name__ == "__main__":
    circular_list = CircularLinkedList()
    circular_list.insertAtFirst(6)
    circular_list.insertAtFirst(5)
    circular_list.insertAtFirst(4)
    circular_list.insertAtFirst(3)
    circular_list.insertAtLast(93)
    circular_list.insertAt(2, 7)
    circular_list.printList()
    print()
    circular_list.delete(3)
    circular_list.reverse()
    print()
    circular_list.printList()
    circular_list.deleteAt(0)
    circular_list.printList()
    circular_list.sort()
    print()
    circular_list.printList()