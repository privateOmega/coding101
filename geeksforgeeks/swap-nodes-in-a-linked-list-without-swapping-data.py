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

    def swap_nodes(self):
        temp_node = self.head

        while temp_node and temp_node.next:
            temp_node.data, temp_node.next.data = temp_node.next.data, temp_node.data

            temp_node = temp_node.next.next


if __name__ == "__main__":

    llist = LinkedList()

    for element in [7, 6, 5, 4, 3, 2, 1]:
        llist.push(element)

    print("List")
    llist.print_list()
    print()

    llist.swap_nodes()

    print("List after swap")
    llist.print_list()
    print()
