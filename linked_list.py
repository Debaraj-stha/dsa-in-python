import heapq


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.bottom = None


class LinkedList:
    def __init__(self, val=None):
        if val is not None or val != 0:
            self.head = Node(val)

    def print(self):
        """
        Print the liist in given order
        """
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")

            if curr.bottom is not None:
                curr = curr.bottom
            else:
                curr = curr.next
        print()

    def append(self, *args):
        """
        Append given values at the end of the list
        """
        for val in args:
            self.insertAtLast(val)

    def reverse(self):
        """
        Reverse the linked list in-place
        """
        prev = None
        curr = self.head
        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        self.head = prev

    def swap_pair(self):
        """
        Swap pair of  itmes

        Args:
            other (_type_): _description_
        """
        # if not other or not other.next:
        #     return
        dummy = LinkedList(0)
        dummy.next = self.head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
        self.head = dummy.next

    def reverse_until(self, k, head=None):
        if not self.head or k <= 1:
            return

        current = self.head if not head else head
        prev = None

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

    def merge_two_sorted_lists(self, other):
        dummy = Node(0)
        current = dummy

        while self.head and other.head:
            if self.head.val <= other.head.val:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other.head
                other.head = other.head.next
            current = current.next

        current.next = self.head if self.head else other.head
        return dummy.next

    def insertAtFirst(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertAtLast(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insertAt(self, value, index: int):
        if index == 0:
            self.insertAtFirst(value)
        elif index == self.length() - 1:
            self.insertAtLast(value)
        else:
            node = Node(value)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def deleteAt(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Index out of range")

        if self.head is None:  # Case: empty list
            raise IndexError("List is empty")

        if index == 0:  # Case: delete the head
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                if current.next is None:  # Prevent invalid traversal
                    raise IndexError("Index out of range")
                current = current.next

            if current.next is None:  # Check if we're at the last valid node
                raise IndexError("Index out of range")

            # Bypass the node to be deleted
            current.next = current.next.next

    def delete(self, value) -> int:
        current_node = self.head

        if current_node and current_node.val == value:
            print("Removing")
            self.head = current_node.next
            return 1
        prev = None
        while current_node and current_node.val != value:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            raise ValueError("value not found : %s" % value)
        prev.next = current_node.next
        current_node = None

    def reverse_into_k_group(self, k):
        dummy = LinkedList(0)
        dummy.next = self.head
        pt = dummy
        while pt is not None:
            for _ in range(k):
                tracer = pt.next
                if tracer is None:
                    return dummy.next
            prev, curr = self.reverse_until(k, pt.next)
            last_node_of_group = prev.next
            last_node_of_group.next = curr
            pt.next = prev
            pt = last_node_of_group
        return dummy.next

    def merge_n_sorted_list(self, lists):
        min_heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))

        dummy = LinkedList(0)
        curr = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

    def swap_first_and_last_node(self):
        if self.head is None or self.head.next is None:
            return  # No change needed for empty list or single node

        prev = None
        second = self.head.next
        last = self.head
        while last.next:
            prev = last
            last = last.next
        last.next = second
        if prev:
            prev.next = self.head
        self.head.next = None
        self.head = last

    def sort(self, reverse=False):
        if self.head is None:
            return

        def swap(node1, node2):
            node1.val, node2.val = node2.val, node1.val

        is_sorted = False
        while not is_sorted:
            is_sorted = True
            current_node = self.head
            while current_node.next:
                next_node = current_node.next
                if (reverse and current_node.val < next_node.val) or (
                    not reverse and current_node.val > next_node.val
                ):
                    swap(current_node, next_node)
                    is_sorted = False
                current_node = current_node.next

    def get_middle_node(self):
        ptr1 = self.head
        ptr2 = self.head
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return ptr1

    def get_nth_from_end(self, n):
        ptr1 = self.head
        ptr2 = self.head
        for _ in range(n):
            ptr2 = ptr2.next
            if ptr2 is None:
                return None
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

    def remove_duplicates(self):
        if not self.head:
            return
        curr = self.head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

    def split(self, key):
        if self.head is None:
            return
        curr = self.head
        prev = None
        while curr:
            if curr.val == key:
                new_head = curr
                break
            prev = curr
            curr = curr.next
        if prev:
            prev.next = None
        return new_head, prev

    def swap(self, index1, index2):
        if self.head is None:
            return
        if (
            index1 < 0
            or index2 < 0
            or index1 >= self.length()
            or index2 >= self.length()
        ):
            raise IndexError("Index out of range")
        current_1 = self.head
        current_2 = self.head
        for _ in range(index1):
            current_1 = current_1.next
        for _ in range(index2):
            current_2 = current_2.next
        current_1.val, current_2.val = current_2.val, current_1.val

    def elementAt(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def index(self, value):
        """
        Returns the index of the first occurrence of the given value in the linked list.

        Args:
            value (int): Value to search for
        Returns:
            int: Index of the first occurrence of the given value, -1 if not found
        """
        try:
            if self.has_loop():
                raise ValueError(
                    "Cannot perform index operation on a linked list with a loop"
                )
            has_value = self.has_value(value)
            if not has_value:
                return -1

            index = 0
            current = self.head
            while current:
                if current.val == value:
                    break
                current = current.next
                index += 1
            return index
        except Exception as e:
            raise e

    def has_value(self, value):
        """
        Returns true if the linked list contains the given value, false otherwise.

        Args:
            value (int): Value to search for
        Returns:
            bool: True if value found, False otherwise
        """
        try:
            current = self.head
            while current:
                if current.val == value:
                    return True
                current = current.next
            return False
        except Exception as e:
            raise e

    def deleteMultiple(self, indices):
        """
        Delete elements from linked list based on given indices

        Args:
            indices (tuple): Indices of items
        """
        # Sort indices in descending order
        indices = sorted(indices, reverse=True)
        for index in indices:
            self.deleteAt(index)

    def insertMultiple(self, indices: tuple, values: tuple):
        """
        Inserts multiple values at given indices in the linked list.

        Args:
            indices (tuple): Indices at which values to be inserted
            values (tuple): Values to be inserted at given indices
        """
        for index, value in zip(indices, values):
            self.insertAt(index, value)

    def has_loop(self):
        """Checks if the linked list contains a loop and finds the loop start index.

        Returns:
            bool: True if a loop exists, False otherwise.
            int: Index of the loop starting node, -1 if no loop.
        """
        if self.head is None:
            return False, -1

        slow = self.head
        fast = self.head

        # Detect if a loop exists using two-pointer technique
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Loop detected

                loop_start = self.head
                index = 0

                while loop_start != slow:
                    loop_start = loop_start.next
                    slow = slow.next
                    index += 1

                return True, index

        return False, -1  # No loop

    def create_loop(self, position):
        """
        Creates a loop in the linked list starting from the given position.

        Args:
            position (int):  Index of list item at which loop to create

        Raises:
            IndexError: _description_


        """
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

    def remove_loop(self):
        try:
            has_loop, index = self.has_loop()
            print(f"Loop detected: {has_loop}, Index: {index}")
            if not has_loop:
                print("No loop found.")
                return
            if index == -1:
                print("Invalid loop index.")
                return

            # Find the loop starting node
            loop_start = self.head
            for _ in range(index):
                loop_start = loop_start.next

            # Find the node pointing to the loop start
            current = loop_start
            while current.next != loop_start:
                current = current.next

            # Break the loop
            current.next = None
            print("Loop removed successfully.")

        except Exception as e:
            raise e

    def sort_items_between(self, index1, index2):
        if not self.head:
            return None
        if (
            index1 < 0
            or index2 < 0
            or index1 >= self.length()
            or index2 >= self.length()
        ):
            raise IndexError("Index out of range")

        # Ensure index1 is smaller
        if index1 > index2:
            index1, index2 = index2, index1

        # Navigate to the start of the range (index1)
        curr = self.head
        for _ in range(index1):
            curr = curr.next

        # Collect values within range [index1, index2]
        values = []
        temp = curr
        for _ in range(index2 - index1 + 1):
            values.append(temp.val)
            temp = temp.next

        # Sort the extracted values
        values.sort()

        # Reassign sorted values back to the nodes
        temp = curr
        for val in values:
            temp.val = val
            temp = temp.next

    def is_palindrome(self):
        if not self.head:
            return True  # An empty list is a palindrome

        origional = self.head
        slow, fast = self.head, self.head

        # Finding the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare the first half and the reversed second half
        # compare first and last item of list

        left, right = self.head, prev
        while right:  # Only check the second half
            if left.val != right.val:
                self.head = origional
                return False
            left = left.next
            right = right.next

        # Restore the second half to its original state
        slow, prev = prev, None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Restore self.head to the original state (optional, as no change happened to self.head)

        self.head = origional

        return True

    def flatten_linked_list(self):
        if not self.head:
            return
        values = []
        curr = self.head

        # Traverse through the main list and collect all values
        while curr is not None:
            values.append(curr.val)
            temp = curr.bottom
            while temp is not None:
                values.append(temp.val)
                temp = temp.next
            curr = curr.next

        # Sort the values to flatten and print them
        values.sort()

        tail, head = None, None
        for value in values:
            new_node = Node(value)
            if head is None:
                head = new_node
                tail = head
            else:
                tail.bottom = new_node  # Correctly connect the nodes
                tail = new_node

        return head

    def divide_linked_lists(self, part: int):
        """
        Divide a linked list items into parts based on given part number

        Args:
            part (int): number of parts

        Raises:
            ValueError: Exception if part value is invaid

        Returns:
            list: Return a list of list of items
        """
        if not self.head:
            return
        length = self.length()
        if part <= 0 or part > length:
            raise ValueError("Invalid part size")
        items_per_part = length // part
        items_per_part_with_remainder = length % part
        curr = self.head
        parts = []
        for i in range(part):
            part_items = []
            part_length = items_per_part + (
                1 if i < items_per_part_with_remainder else 0
            )
            for _ in range(part_length):
                if curr:
                    part_items.append(curr.val)
                    curr = curr.next
            parts.append(part_items)

        return parts

    def reverse_node_in_k_group(self, k):
        if k < 0:
            return


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print()


if __name__ == "__main__":
    ll = LinkedList(5)
    ll.append(8, 92, 922, 10, 2, 9)
    ll.divide_linked_lists(2)
