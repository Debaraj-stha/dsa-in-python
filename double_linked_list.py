class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def append(self,data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node=Node(data)
            self.tail.right=new_node
            new_node.left=self.tail
            self.tail=new_node
            
    def delete(self, key):
        if self.head is None:
            print("List is empty.")
            return
        current=self.head
        while current:
            if current.data==key:
                if current.left:
                    current.left.right=current.right
                else:
                    self.head=current.right
                if current.right:
                    current.right.left=current.left
                else:
                    self.tail=current.left
                break
            current=current.right
        else:
            print("Key not found in the list.")
    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.right=self.head
            self.head.left=new_node
            self.head=new_node
            
            
    def displayForward(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.right
        print()
        
    def displayBackward(self):
        temp=self.tail
        while temp:
            print(temp.data,end="<-")
            temp=temp.left
        print()

if __name__ == '__main__':
    dl=DoubleLinkedList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    dl.append(4)
    dl.displayForward()   # Output: 1->2->3->4->
    dl.delete(3)
    dl.displayForward()   # Output: 1->2->4->
    dl.prepend(13)
    dl.displayForward()   # Output: 13->1->2->4->
    dl.displayBackward()  # Output: 4->2->13->1->
    pass