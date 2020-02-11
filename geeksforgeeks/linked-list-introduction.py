from typing import Optional, Any


class Node:
    def __init__(self, data: Optional[Any] = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data: Any):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, data: Any, node_data: Any):
        new_node = Node(data)
        temp_node = self.head
        while temp_node.next and temp_node.data != node_data:
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node

    def insert_at_tail(self, data: Any):
        new_node = Node(data)
        temp_node = self.head
        if not self.head:
            self.head = new_node
            return
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node

    def remove_from_head(self) -> Optional[Any]:
        temp_node = self.head
        if temp_node:
            self.head = temp_node.next
            return temp_node.data

    def remove_from_tail(self) -> Optional[Any]:
        temp_node = self.head
        if not temp_node:
            return
        prev_node = None
        while temp_node.next:
            prev_node = temp_node
            temp_node = temp_node.next
        prev_node.next = None
        return temp_node

    def remove_from_index(self, index: int) -> Optional[Any]:
        temp_node = self.head
        if not temp_node:
            return
        if index == 0:
            self.head = temp_node.next
            return temp_node
        prev_node = None
        count = 0
        while temp_node.next and count < index:
            prev_node = temp_node
            temp_node = temp_node.next
            count += 1

        if index > count:
            return

        prev_node.next = temp_node.next
        return temp_node

    def remove_particular_node(self, node_data: Any) -> Optional[Any]:
        temp_node = self.head
        prev_node = None
        while temp_node.next:
            prev_node = temp_node
            temp_node = temp_node.next
            if temp_node.data == node_data:
                break

        prev_node.next = temp_node.next
        return temp_node

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next

    def delete_list(self):
        self.head = None

    def length_iterative(self) -> int:
        temp_node = self.head
        count = 0
        while temp_node:
            count += 1
            temp_node = temp_node.next

        return count

    def length_recursive(self, head) -> int:
        if not head:
            return 0
        return 1 + self.length_recursive(head.next)

    def search_iterative(self, search_element: Any) -> bool:
        temp_node = self.head
        while temp_node:
            if temp_node.data == search_element:
                return True
            temp_node = temp_node.next

        return False

    def search_recursive(self, search_element: Any, head) -> bool:
        if not head:
            return False
        if head.data == search_element:
            return True

        return self.search_recursive(search_element, head.next)

    def find_nth_node(self, n: int) -> Optional[Any]:
        if n < 1:
            return
        temp_node = self.head
        count = 0
        while temp_node:
            if count == n - 1:
                return temp_node.data
            temp_node = temp_node.next
            count += 1

    def find_nth_node_from_end(self, n: int) -> Optional[Any]:
        if n < 1:
            return
        fast_node = self.head
        slow_node = self.head
        count = 0
        while fast_node and count < n:
            fast_node = fast_node.next
            count += 1

        while fast_node:
            fast_node = fast_node.next
            slow_node = slow_node.next

        return slow_node.data

    def find_middle_node(self) -> Optional[Any]:
        if not self.head:
            return
        fast_node = self.head
        slow_node = self.head
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        return slow_node.data

    def find_middle_node_alternative(self) -> Optional[Any]:
        fast_node = self.head
        slow_node = self.head
        count = 0
        while fast_node:
            if count % 2 == 0:
                slow_node = slow_node.next
            count += 1
            fast_node = fast_node.next

        return slow_node.data

    def count_node_iterative(self, data: Any) -> int:
        temp_node = self.head
        count = 0
        while temp_node:
            if temp_node.data == data:
                count += 1
            temp_node = temp_node.next

        return count

    def count_node_recursive(self, head, data: Any) -> int:
        if not head:
            return 0

        if head.data == data:
            return 1 + self.count_node_recursive(head.next, data)

        return self.count_node_recursive(head.next, data)


if __name__ == "__main__":
    llist = LinkedList()

    for data in [3, 2, 1]:
        llist.insert_at_head(data)
    for data in [5, 6, 7, 8]:
        llist.insert_at_tail(data)
    llist.insert_after_node(4, 3)

    llist.remove_from_head()
    llist.remove_from_tail()
    llist.remove_particular_node(3)
    llist.remove_from_index(0)

    print("List")
    llist.print_list()
    print()

    print(
        f"List length: {llist.length_iterative()} or {llist.length_recursive(llist.head)}")

    print(
        f"Is 5 present {llist.search_iterative(5)} or {llist.search_recursive(5, llist.head)}")
    print(
        f"Is 8 present {llist.search_iterative(8)} or {llist.search_recursive(8, llist.head)}")

    print(f"2nd node: {llist.find_nth_node(2)}")
    print(f"2nd node from end: {llist.find_nth_node_from_end(2)}")

    print(
        f"middle node: {llist.find_middle_node()} or {llist.find_middle_node_alternative()}")

    print(
        f"count 6: {llist.count_node_iterative(6)} or {llist.count_node_recursive(llist.head, 6)}")

    llist.delete_list()
