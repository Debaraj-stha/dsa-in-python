class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
def swap(node1,node2):
        node1.value, node2.value = node2.value, node1.value
def display_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.value))
        current = current.next
    print(" -> ".join(result))

class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtFirst(self,value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
            return
       
        self.head = new_node

    def insertAtLast(self, value):
        last=self.head
        if last is None:
            self.head=Node(value)
            return
        while last.next:
            last=last.next
        new_node=Node(value)
        last.next=new_node
    def insert(self,*args):
        for arg in args:
            self.insertAtLast(arg)
        return 
    
    def insertAt(self,value,index):
        if index==0:
            return self.insertAtFirst(value)
        elif index==self.length()+1:
            return self.insertAtLast(value)
        elif index<0:
            raise IndexError("Index is negative")
        else:
            current=self.head
            for i in range(index-1):
                current=current.next
            new_node=Node(value)
            new_node.next=current.next
            current.next=new_node
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def deleteFirst(self):
        if self.head is None:
            raise IndexError("List is empty")
        else:
            self.head = self.head.next
            return True
    def deleteLast(self):
        if self.head is None:
            raise IndexError("List is empty")
        current = self.head
        previous=None
        while current.next is not None:
            previous = current
            current = current.next
        if previous is not None:
            previous.next = None
        else:
            self.head = None
    def deleteAt(self,index):
        if index <0 or index >=self.length()+1:
            raise IndexError("Index out of range")
    
        elif  index==0:
            self.head=self.head.next
            return
        elif index==self.length():
            self.deleteLast()
            return
        current=self.head
        for i in range(index-1):
            current=current.next
        current.next=current.next.next
        
    def delete(self,value):
        if self.head is None:
            raise IndexError("List is empty")
        elif self.head.value==value:
            self.head=self.head.next
            return True
        current=self.head
        previous=None
        while current.value!=value:
            previous=current
            current=current.next
        if current is None:
            raise ValueError("Element not found")
        else:
            previous.next=current.next
            return True
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev

    def sort(self,reverse=False):
        if self.head is None:
            return
        is_sorted=False
        while not is_sorted:
            is_sorted=True
            curr=self.head
            while curr.next:
                next_node=curr.next
                if (reverse and curr.value<next_node.value) or (not reverse and curr.value>next_node.value):
                    swap(curr, next_node)
                    is_sorted=False
                curr=curr.next

    def print(self,message="List item"):
        print(message)
        current = self.head
        while current:
            print(current.value, end="->")
            current = current.next
        print()

    def head(self):
        if self.head is None:
            raise ValueError("List is empty")
        return self.head.value

    def middle_node(self):
        if self.head is None:
            raise ValueError("List is empty")
        slow=self.head
        fast=self.head
        while slow and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def get_nth_node_from_end(self,n):
        if self.head is None:
            raise ValueError("List is empty")
        slow=self.head
        fast=self.head
        for _ in range(n):
            fast=fast.next
            if fast is None:
                raise IndexError("Index out of range")
        while fast:
            slow=slow.next
            fast=fast.next
        return slow


    @staticmethod
    def merge_sorted_linked_list(list1,list2):
        dummy=Node(0)
        current=dummy
        while list1.head and list2.head:
            if list1.head.value<list2.head.value:
                current.next=list1.head
                list1.head=list1.head.next
            else:
                current.next=list2.head
                list2.head=list2.head.next
            current=current.next
        if list1.head:
            current.next=list1.head
        if list2.head:
            current.next=list2.head
        return dummy.next
    def create_loop(self,position):
        try:
            if self.head is None:
                return
            if position < 0 or position >= self.length():
                raise IndexError("Index out of range")
            current = self.head
            index = 0
            loop_node = None
            while current.next:
                if index == position:
                    loop_node = current
                current = current.next
                index += 1
            if loop_node:
                current.next = loop_node
        except IndexError as e:
            print(e)
    def has_loop(self):
        if self.head is None:
            raise IndexError("List is empty")
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                loop_start=self.head
                index=0
                
                while loop_start != slow:
                    print("ddd")
                    loop_start = loop_start.next
                    slow = slow.next
                    index += 1
                return True,index
        return False,-1
    def remove_loop(self):
        if self.head is None:
            return None
        has_loop,index=self.has_loop()
        if not has_loop:
            return "No loop found"
        if index ==-1:
            raise IndexError("Index out of range")
        loop_start=self.head
        for i in range(index):
            loop_start=loop_start.next
        curr=loop_start
        while curr.next!=loop_start:
            curr=curr.next
        curr.next=None
        return True
    def sort_items_between(self,low,high):
        if self.head is None:
            raise IndexError("List is empty")
        if low<0 or high>=self.length() or low>self.length():
            raise IndexError("Index out of range")
        if low>high:
            high,low=low,high
        curr=self.head
        for _ in range(low):
            curr=curr.next
        temp=curr
        values=[]
        for i in range(high-low+1):
            values.append(temp.value)
            temp=temp.next
        temp=curr
        values.sort()
        for i in range(high-low+1):
            temp.value=values[i]
            temp=temp.next
        return True
    def reverse_nodes_between(self,index1,index2):
        if self.head is None:
            raise IndexError("List is empty")
        if index1<0 or index2<0 or index1>self.length() or index2>self.length():
            raise IndexError("Index out of range")
        if index1>index2:
            index2,index1=index1,index2
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        for _ in range(index1):

            prev=prev.next
           
        curr=prev.next
        for _ in range(index2-index1):
            next_node=curr.next
            curr.next=next_node.next
            next_node.next=prev.next
            prev.next=next_node
            print(f"After iteration {_ + 1}:")
            display_list(dummy.next)
           
        if index1==0:
            self.head=prev.next
        return True
    
    def reverse_until(self,k):
        if self.head is None:
            raise IndexError("list is empty")
        current=self.head
        prev=None
        for _ in range(k+1):
            if not current:
                break
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head.next=current
        self.head=prev

    def reverse_into_k_group(self, k):
        if k <= 1 or not self.head:
            return self.head  # No reversal needed if k is 1 or list is empty

        dummy = Node(0)
        dummy.next = self.head
        prev_group_end = dummy
        curr = self.head

        while curr:
            group_start = curr
            group_end = curr

            # Traverse k nodes to check if we have a complete group
            for _ in range(k - 1):
                group_end = group_end.next
                if not group_end:  # If fewer than k nodes, do not reverse
                    return dummy.next

            # Prepare for reversing
            next_group_start = group_end.next
            group_end.next = None  # Temporarily break the group

            # Reverse the current group
            prev, current = None, group_start
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Connect the reversed group back to the main list
            prev_group_end.next = prev  # New head of the reversed group
            group_start.next = next_group_start  # Connect the group's tail to the next group

            # Update pointers
            prev_group_end = group_start
            curr = next_group_start  # Move to the next group

        self.head = dummy.next

    def swap_pair(self):
        if self.head is None:
            return self.head
        dummy=Node(0)
        dummy.next=self.head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            self.head = dummy.next
    def split(self, index):
        if self.head is None:
            raise IndexError("List is empty")
        if index < 0 or index > self.length():
            raise IndexError("Index out of range")
        
        current = self.head
        if index == 0:
            self.head = None  
            return None, current 
        
        prev = None
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = None 
        return self.head, current
    
    def itemAt(self,index):
        if index<0 or index>=self.length():
            raise IndexError("Index out of range")
        current=self.head
        for _ in range(index):
            current=current.next
        return current.value
    
    def indexOf(self,value):
        current=self.head
        index=0
        while current:
            if current.value==value:
                return index
            current=current.next
            index+=1
        return -1

        
    def deleteMany(self,indices):
        if self.head is None:
            return False
        if not indices:
            return False
        for index in sorted(indices,reverse=True):
            self.deleteAt(index)
        return True
    
    def deleteAll(self):
        self.head=None
        return True
    
    def __iter__(self):
        self._current=self.head
        return self
    def __next__(self):
        
        if self._current is None:
                raise StopIteration
        value=self._current.value
        self._current=self._current.next
        return value
    
    def __len__(self):
        return self.length()
    
    def __str__(self):
        return str(self.to_list())
    
    def to_list(self):
        result=[]
        current=self.head
        while current:
            result.append(current.value)
            current=current.next
        return result
    
    def has(self,element):
        if self.head is None:
            return False
        current=self.head
        while current:
            if current.value==element:
                return True
            current=current.next
        return False
    
    def is_empty(self):
        return self.head is None
    
    def is_palindrome(self):
        if not self.head:
            return True  # An empty list is a palindrome
        
        def reverse(head):
            prev, current = None, head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev  
        slow=self.head
        fast=self.head
        origional=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second_half=reverse(slow)
        reversed_second_half= second_half
        first_half=self.head
        while second_half:
            if second_half.value !=first_half.value:
                reverse(reversed_second_half)
                return False
            second_half=second_half.next
            first_half=first_half.next
        reverse(reversed_second_half)
        return True

    
        
                

ll5=LinkedList()
ll5.insertAtLast(9)
ll5.insertAtLast(8)
ll5.insertAtLast(7)
ll5.insertAtLast(6)
ll5.insertAtLast(5)
# ll5.insertAtLast(4)
# ll5.print()

# ll5.swap_pair()
# ll5.print("Swapped pair")
# head,tail=ll5.split(4)
# print("First part:")
# display_list(head)
# print("Second part:")
# display_list(tail)
# print(ll5.itemAt(3))
# print(ll5.indexOf(7))
# print(ll5.deleteMany([1,2,3]))
# ll5.print()
# ll5.deleteAll()
# ll5.print()
values=iter(ll5)
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(len(ll5))
print(str(ll5))
ll6=LinkedList()
ll6.insert(1,4,2,2,4,5)
ll6.print()
print(ll6.is_palindrome())

