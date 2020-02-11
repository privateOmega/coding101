class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next


def list_intersection(first_list_head, second_list_head):
    intersection_list = LinkedList()

    while first_list_head and second_list_head:
        if first_list_head.data == second_list_head.data:
            intersection_list.push(first_list_head.data)
            first_list_head = first_list_head.next
            second_list_head = second_list_head.next
        elif first_list_head.data < second_list_head.data:
            first_list_head = first_list_head.next
        else:
            second_list_head = second_list_head.next

    print("intersection list")
    intersection_list.print()


if __name__ == "__main__":
    first_list = LinkedList()
    second_list = LinkedList()

    for element in [6, 4, 3, 2, 1]:
        first_list.push(element)

    for element in [8, 6, 4, 2]:
        second_list.push(element)

    list_intersection(first_list.head, second_list.head)
