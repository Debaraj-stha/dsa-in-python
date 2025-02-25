def display(head):
    current = head
    while current:
        print(current.value,end="->")
        current = current.next
def displayFromTail(tail):
    current = tail
    while current:
        print(current.value,end="->")
        current = current.prev