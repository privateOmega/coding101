from typing import Optional, Any


class Node:
    def __init__(self, data: Optional[Any] = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data: Any):
        new_node = Node(data)
        temp_node = self.head
        if not self.head:
            self.head = new_node
            return
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node

    def is_palindrome(self) -> bool:
        prev_node = None
        fast_node = self.head
        slow_node = self.head
        while fast_node and fast_node.next:
            prev_node = slow_node
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        print(prev_node.data, slow_node.data, fast_node and fast_node.data)

        prev_node.next = None

        first_half = self.head
        second_half = slow_node.next if fast_node else slow_node

        second_half = reverse(second_half)

        return compare_lists(first_half, second_half)


def print_list(head):
    temp_node = head
    while temp_node:
        print(temp_node.data, end=" ")
        temp_node = temp_node.next


def reverse(head):
    prev_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return head


def compare_lists(first_head, second_head) -> bool:
    first_node = first_head
    second_node = second_head

    while first_node and second_node:
        if first_node.data != second_node.data:
            return False
        first_node = first_node.next
        second_node = second_node.next

    return True


if __name__ == "__main__":

    llist = LinkedList()

    for element in ['a', 'b', 'a', 'c', 'a', 'b', 'a']:
        llist.insert_at_tail(element)

    print("List")
    print_list(llist.head)
    print()

    print(
        f"Palindrome {llist.is_palindrome()}")
