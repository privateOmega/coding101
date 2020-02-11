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

    def remove_duplicates(self) -> int:
        prev_node = self.head
        current_node = self.head

        list_set = set()

        while current_node:
            if current_node.data in list_set:
                prev_node.next = current_node.next
            else:
                list_set.add(current_node.data)
            prev_node = current_node
            current_node = current_node.next


if __name__ == "__main__":

    llist = LinkedList()

    for element in [21, 43, 41, 21, 12, 11, 12]:
        llist.insert_at_tail(element)

    print("List")
    llist.print_list()
    print()

    llist.remove_duplicates()

    print("List after removal")
    llist.print_list()
    print()
