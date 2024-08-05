class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertAtFirst(self,data)->int:
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        return 1

        
        
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()
        
        
    def insertAtLast(self,value)->int:
        new_node=Node(value)
        current_node=self.head
        
        if current_node is None:
            self.head=new_node
            return 1
        lst_node=self.head
        while lst_node.next:
            lst_node=lst_node.next
        lst_node.next=new_node
        return 1
        
        
    
    def length(self)->int:
        count=0
        current_node=self.head
        while current_node:
            count+=1
            current_node=current_node.next
        return count
    
    
    def insert(self,value,position)->int:
        current_node=self.head
        if position==0:
          return  self.insertAtFirst(value)
        
        if position>self.length():
            raise IndexError("Index out of bounds")
        elif position==self.length():
           return self.insertAtLast(value)
        
        else:
            new_node=Node(value)
            for i in range(position-1):
                current_node=current_node.next
                if current_node is None:
                    raise ValueError("Array index out of range")
            new_node.next=current_node.next
            current_node.next=new_node
            return 1
               
            
    def removeAt(self,index)->int:
        current_node=self.head
        if  current_node is None:
            raise ValueError("Empty list")
        if index==0:
            self.head=self.head.next
            return 1
        if index>self.length()-1:
            raise IndexError("Index out of bounds")
        
        for i in range(index-1):
            current_node=current_node.next
            if current_node is None:
                raise ValueError("Array index out of range")
                break
        current_node.next=current_node.next.next
        return 1


    def remove(self,value)->int:
        current_node=self.head
        
        if current_node and current_node.data==value:
            print("Removing")
            self.head=current_node.next
            return 1  
        prev=None
        while current_node  and current_node.data!=value:
            prev=current_node
            current_node=current_node.next
           
        if current_node is None:
            raise ValueError("value not found : %s" % value)
        prev.next=current_node.next
        current_node=None
        
        
    def sort(self,reverse=False):
        if self.head is None:
            return
        
        def swap(node1,node2):
            node1.data, node2.data = node2.data, node1.data
            
        is_sorted=False
        while not is_sorted:
            is_sorted=True
            current_node=self.head
            while current_node.next:
                next_node=current_node.next
                if (reverse and current_node.data < next_node.data) or (not reverse and current_node.data > next_node.data):
                    swap(current_node, next_node)
                    is_sorted=False
                current_node=next_node
                
    def indexOf(self,value)->int:
        
        """Returns the index of given value"""
        current_node=self.head
        index=0
        while current_node:
            if current_node.data==value:
                return index
            current_node=current_node.next
            index+=1
        return -1
    
    
    def itemAt(self,index)->int:
        current_node=self.head
        if current_node is None:
            raise ValueError("Empty list")
        if index>self.length()-1:
            raise IndexError("Index out of bounds")
        
        for i in range(index-1):
            current_node=current_node.next
            if current_node is None:
                raise ValueError("Array index out of range")
        return current_node.data
        
    
    def reverse(self):
        """Reverse the list items"""
        current_node=self.head
        if current_node is None:
            return
        prev=None
        while current_node is not None:
            next_node=current_node.next
            current_node.next=prev
            prev=current_node
            current_node=next_node
        self.head=prev
        
        
    def append(self,value):
        
        """append a value  at the end of the list"""
        self.insertAtLast(value)
        
        
    def clear(self):
        """Clear all elements from the list"""
        self.head=None
        
    def get_values(self):
        if self.head is None:
            return list()
        values=[]
        current_node=self.head
        while current_node:
            values.append(current_node.data)
            current_node=current_node.next
        return values
    
    def copy(self):
        new_list=LinkedList()
        current_node=self.head
        while current_node:
            new_list.append(current_node.data)
            current_node=current_node.next
        return new_list
    
        
    def toString(self):
        return str(self.get_values())
    
    def  equal(self, other):
        if not isinstance(other, LinkedList):
            return False
        if self.length()!= other.length():
            return False
        return self.get_values() == other.get_values()
    
    def removeLast(self):
        if self.head is None:
            raise ValueError("List is empty")
        if self.length()==1:
            self.head=None
            return
        current_node=self.head
        if current_node.next is None:
            self.head=None
            return
        while current_node.next.next:
            current_node=current_node.next
        current_node.next=None

        
    def  removeFirst(self):
        if self.head is None:
            raise ValueError("List is empty")
        self.head=self.head.next
        return
    
    
    def  removeValue(self, value):
        self.remove(value)
        
        
    def hasValue(self):
        return self.length()>0
    
    def  hasNext(self):
        return self.head is not None
    

    

    
if __name__=="__main__":
     li=LinkedList()
     li.insertAtFirst(1)
     li.insertAtFirst(2)
     li.insertAtFirst(3)
     li.insertAtLast(4)
     li.insert(5,3)
     li.printList()
     li.reverse()
     l=li.length()
     li.printList()
     li.printList()
     li.remove(2)
     li.printList()
     li.sort(reverse=True)
     li.printList()
     print("Index of 5: ",li.indexOf(3))
     item=li.itemAt(2)
     print("Item at index 2: ",item)
     li.printList()
     print("List after clear: ")
     li.printList()
     
     v=li.get_values()
     print("Values in the list: ",v)
     print("copied data")
     c=li.copy()
     c.printList()
     print("string")
     print(li.toString())
    #  li.clear()
     l=LinkedList()
     l.insertAtFirst(7)
     x=LinkedList()
     x.insertAtFirst(9)
     b=l.equal(x)
     print("Equal: ",b)
     li.printList()
     li.removeLast()
     print("After deleting last item: ")
     li.printList()
     li.removeFirst()
     print("After deleting first item: ")
     li.printList()
    #  li.itemAt(20)
     x.insertAtFirst(67)
     x.insertAtFirst(77)
     x.insertAtFirst(670)
    
 