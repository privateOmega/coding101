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

    def count_loop_length(self) -> int:
        if not self.head:
            return 0

        fast_node = self.head
        slow_node = self.head
        count = 0
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            count += 1
            if fast_node == slow_node:
                return count

        return 0


if __name__ == "__main__":

    llist = LinkedList()

    for element in [1, 2, 3, 4, 5]:
        llist.insert_at_tail(element)

    llist.head.next.next.next.next.next = llist.head.next

    print(
        f"Loop length {llist.count_loop_length()}")
