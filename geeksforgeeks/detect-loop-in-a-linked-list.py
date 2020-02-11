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

    def detect_loop(self) -> bool:
        list_set = set()
        temp_node = self.head

        while temp_node:
            if temp_node.data in list_set:
                return True
            list_set.add(temp_node.data)
            temp_node = temp_node.next

        return False

    def detect_loop_alternative(self) -> bool:
        fast_node = self.head
        slow_node = self.head
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            if fast_node == slow_node:
                return True
        
        return False


if __name__ == "__main__":

    llist = LinkedList()

    for element in [1, 2, 3, 4, 5]:
        llist.insert_at_tail(element)

    llist.head.next.next.next.next.next = llist.head.next

    print(f"Contains Loop {llist.detect_loop()} or {llist.detect_loop_alternative()}")
