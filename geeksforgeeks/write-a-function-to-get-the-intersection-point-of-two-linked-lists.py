class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_node(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def print(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next

    def length(self):
        temp_node = self.head
        count = 0
        while temp_node:
            count += 1
            temp_node = temp_node.next


def find_intersection_point(first_list, second_list):
    first_list_head = first_list.head
    second_list_head = second_list.head
    first_temp_node = first_list_head
    while first_temp_node:
        second_temp_node = second_list_head
        while second_temp_node:
            if first_temp_node == second_temp_node:
                return first_temp_node.data
            second_temp_node = second_temp_node.next
        first_temp_node = first_temp_node.next


def find_intersection_point_alternative(larger_list_head, smaller_list_head, length_difference):
    for _ in range(length_difference):
        larger_list_head = larger_list_head.next

    while larger_list_head and smaller_list_head:
        if larger_list_head == smaller_list_head:
            return larger_list_head.data
        larger_list_head = larger_list_head.next
        smaller_list_head = smaller_list_head.next


def find_intersection_point_helper(first_list, second_list):
    first_length = first_list.length()
    second_length = second_list.length()
    length_difference = abs(first_length - second_length)
    if first_length > second_length:
        return find_intersection_point_alternative(first_list.head, second_list.head, length_difference)
    else:
        return find_intersection_point_alternative(second_list.head, first_list.head, length_difference)


def find_intersection_point_second_alternative(first_list, second_list):
    first_node = first_list.head
    second_node = second_list.head

    while first_node and second_node and first_node != second_node:
        first_node = first_node.next
        second_node = second_node.next

        if first_node == second_node:
            return first_node.data

        if not first_node:
            first_node = second_list.head
        if not second_node:
            second_node = first_list.head

    return first_node.data


if __name__ == "__main__":
    first_list = LinkedList()
    second_list = LinkedList()

    node_30 = Node(30)
    node_15 = Node(15)
    node_10 = Node(10)
    node_9 = Node(9)
    node_6 = Node(6)
    node_3 = Node(3)

    for element in [node_30, node_15, node_9, node_6, node_3]:
        first_list.push_node(element)

    for element in [node_30, node_15, node_10]:
        second_list.push_node(element)

    print(find_intersection_point(first_list, second_list))
    print(find_intersection_point(first_list, second_list))
    print(find_intersection_point_second_alternative(first_list, second_list))
