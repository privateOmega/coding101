from typing import Optional, Any


class Node:
    def __init__(self, data: Optional[Any] = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next

    def move_to_front(self):
        prev_node = None
        current_node = self.head

        while current_node and current_node.next:
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = None
        current_node.next = self.head
        self.head = current_node


if __name__ == "__main__":

    llist = LinkedList()

    for element in [5, 4, 3, 2, 1]:
        llist.push(element)

    print("List")
    llist.print_list()
    print()

    llist.move_to_front()

    print("List after swap")
    llist.print_list()
    print()
