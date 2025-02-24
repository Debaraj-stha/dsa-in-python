def display(head):
    print("list")
    current=head
    while current:
        print(current.value,end="->")
        current=current.next