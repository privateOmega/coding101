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


def seggregate_even_odd_nodes(linked_list):
    odd_start = None
    odd_end = None
    even_start = None
    even_end = None

    temp_node = linked_list.head
    while temp_node:
        if temp_node.data % 2 == 0:
            if not even_start:
                even_start = even_end = temp_node
            else:
                even_end.next = temp_node
                even_end = even_end.next
        else:
            if not odd_start:
                odd_start = odd_end = temp_node
            else:
                odd_end.next = temp_node
                odd_end = odd_end.next

        temp_node = temp_node.next

    if not even_start or not odd_start:
        return

    even_end.next = odd_start
    odd_end.next = None

    linked_list.head = even_start


if __name__ == "__main__":

    llist = LinkedList()

    for element in [1, 2, 3, 4, 5]:
        llist.insert_at_tail(element)

    seggregate_even_odd_nodes(llist)

    llist.print_list()
