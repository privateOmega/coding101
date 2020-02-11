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

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next


def reverse_linked_list(llist):
    prev_node = None
    current_node = llist.head
    next_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    llist.head = prev_node


def reverse_linked_list_alternative(head):
    if not head or not head.next:
        return head

    rest = reverse_linked_list_alternative(head.next)

    head.next.next = head
    head.next = None

    return rest


def reverse_linked_list_helper(llist):
    llist.head = reverse_linked_list_alternative(llist.head)


if __name__ == "__main__":

    llist = LinkedList()

    for element in [1, 2, 3, 4, 5]:
        llist.insert_at_tail(element)
    print("list")
    llist.print_list()
    print()
    reverse_linked_list(llist)
    print("reversed list")
    llist.print_list()
    print()
    reverse_linked_list_helper(llist)
    print("orginal list")
    llist.print_list()
    print()
