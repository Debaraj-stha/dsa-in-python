class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtLast(self, value):
        last = self.head
        if last is None:
            self.head = Node(value)
            return
        while last.next:
            last = last.next
        new_node = Node(value)
        last.next = new_node

    def print(self, message="List"):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        print(f"{message}: {' -> '.join(map(str, result))}")

    def reverse_into_k_group(self,head, k):
        if k <= 1 or not head:
            return head  # No reversal needed if k is 1 or list is empty

        dummy = Node(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head
        while curr:
            group_end= curr
            group_start=curr
            for _ in range(k-1):
                group_end= group_end.next
                if not group_end:
                    return dummy.next
            next_start_node=group_end.next
            group_end.next=None
            prev,current=None,group_start
            while current:
                next_node=current.next
                current.next=prev
                prev=current
                current=next_node
            prev_group_end.next=prev
            group_start.next=next_start_node
            prev_group_end=group_start
            curr=next_start_node



        return dummy.next
                

ll5=LinkedList()
ll5.insertAtLast(9)
ll5.insertAtLast(8)
ll5.insertAtLast(7)
ll5.insertAtLast(6)
ll5.insertAtLast(5)
# ll5.insertAtLast(4)

head=Node(22)
head.next=Node(33)
head.next.next=Node(44)
head.next.next.next=Node(55)
head.next.next.next.next=Node(66)
head.next.next.next.next.next=Node(77)
head.next.next.next.next.next.next=Node(88)
x=ll5.reverse_into_k_group(head,3)
while x.next:
    print(x.value,end=' -> ')
    x=x.next