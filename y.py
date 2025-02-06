class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def insertAtLast(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def insertAtFirst(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = Node(value)
        node.next = self.head
        self.head = node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # To indicate the end of the linked list


    def insertAt(self,index,value):
        if self.head is None:
            self.insertAtFirst(value)
            return
        if index < 0 or index > self.length():
            raise IndexError("Index out of range")
        curr=self.head
        prev= None
        for _ in range(index):
            prev=curr
            curr=curr.next
        node=Node(value)
        node.next=curr.next
        curr.next=node
    def length(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count
    def deleteAtLast(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head.next is None:
            self.head=None
            return
        curr=self.head
        while curr.next.next:
            curr=curr.next
        curr.next=None
    def deleteAtFirst(self):
        if self.head is None:
            raise IndexError("List is empty")
        self.head=self.head.next

    def deleteAt(self,index):
        if self.head is None:
            raise IndexError("List is empty")
        if index < 0 or index > self.length()-1:
            raise IndexError("Index out of range")
        curr=self.head
        prev=None
        for _ in range(index):
            prev=curr
            curr=curr.next
        prev.next=curr.next
    def insert(self,*args):
        for value in args:
            self.insertAtLast(value)

    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

    def sort(self,reverse=False):
        def swap(node1,node2):
            node1.value, node2.value = node2.value, node1.value
        is_sorted=False
        while not is_sorted:
            is_sorted=True
            current=self.head
            while current.next:
                next_node=current.next
                if (reverse and current.value<next_node.value) or (not reverse and current.value>next_node.value):
                    swap(current, next_node)
                    is_sorted=False
                current=current.next
    def crete_loop(self,index):
        curr=self.head
        position=0
        while curr.next:
            if position==index:
                loop_node=curr
            curr=curr.next
            position+=1
        if loop_node:
            curr.next=loop_node
    def has_loop(self):
        slow=self.head
        fast=self.head
        index=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                loop_node=self.head
                while loop_node!=slow:
                    loop_node=loop_node.next
                    slow=slow.next
                    index+=1
                return index,True
                
        return -1, False
    def remove_loop(self):
        if self.has_loop()[1]:
            loop_index, has_loop=self.has_loop()
            
            loop_start = self.head
            for _ in range(loop_index):
                loop_start = loop_start.next

            # Find the node pointing to the loop start
            current = loop_start
            while current.next != loop_start:
                current = current.next

            # Break the loop
            current.next = None
            print("Loop removed successfully.")
    def swap_pair(self):
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        while prev.next and prev.next.next:

            first=prev.next
            seccond=prev.next.next

            prev.next=seccond
            first.next=seccond.next
            seccond.next=first
            prev=first
        self.head=dummy.next
    def split(self,index):
        curr=self.head
        prev=None
        for _ in range(index):
            prev=curr
            curr=curr.next
        if prev:
            prev.next=None
        return self.head,curr
    
    # Reverse k nodes starting from 'head'
    def reverse_until(self, k, head=None):
        if not self.head or k <= 1:
            return

        current = self.head if not head else head
        prev = None

        # Reverse k nodes
        for _ in range(k):
            if not current:
                break
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        if not head:
            self.head.next = current
            self.head = prev
        else:
            return prev, current

    # Reverse nodes in k-group
    def reverse_into_k_group(self, k):
        dummy = Node(0)
        dummy.next = self.head
        prev_group = dummy

        while True:
            kth = prev_group
            count = 0

            # Find the kth node
            while kth and count < k:
                kth = kth.next
                count += 1

            if not kth:
                break  # Less than k nodes left, no more reversal

            next_group = kth.next
            # Reverse k nodes
            prev, curr = None, prev_group.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect with the previous part
            tail = prev_group.next
            prev_group.next = prev
            tail.next = next_group
            prev_group = tail  # Move prev_group to the tail for the next iteration

        self.head = dummy.next  # Update head

   

    def sort_items_between(self,index1,index2):
        if index1<0 or index2<0 or index1>self.length() or index2>self.length():
            raise IndexError("Invalid indices")
        if index1>index2:
            index1,index2 = index2,index1
        curr=self.head
        for _ in range(index1):
            curr=curr.next
        values=[]
        temp=curr
        for _ in range(index2-index1+1):
            values.append(temp.value)
            temp=temp.next
        values.sort()
        temp=curr
        for i in range(len(values)):
            temp.value=values[i]
            temp=temp.next
        
        

# Example Usage
ll = LinkedList(1)
ll.insertAtLast(2)
ll.insertAtLast(3)
ll.insertAtFirst(0)
ll.insertAt(2, 10)
ll.insert(19,4,7,8,69,32)
ll.print_list()
# ll.deleteAtFirst()
# ll.print_list()
# ll.deleteAtLast()
# ll.deleteAt(4)
# ll.print_list()
# # ll.reverse()
# ll.print_list()
# # ll.sort(False)
# ll.print_list()
# ll.crete_loop(4)
# print(ll.has_loop())
# print(ll.remove_loop())
# ll.print_list()
ll.reverse_into_k_group(5)

# ll.swap_pair()
# ll.print_list()

# head, tail=ll.split(4)
# print("First part:")
# while head:
#     print(head.value, end=" -> ")
#     head=head.next

# print("Second part:")
# while tail:
#     print(tail.value, end=" -> ")
#     tail=tail.next

# ll.sort_items_between(2,6)
ll.print_list()