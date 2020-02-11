""" Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space. """

class Node:
    def __init__(self, data, next_ptr = None):
        self.data = data
        self.next_ptr = next_ptr

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, node):
        if self.head is not None:
            node.next_ptr = self.head
        self.head = node

list_1 = SinglyLinkedList()
list_2 = SinglyLinkedList()

for element in [3, 7, 8, 10]:
    list_1.insert_at_beginning(element)

for element in [99, 1, 8, 10]:
    list_2.insert_at_beginning(element)


