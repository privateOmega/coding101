""" An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses. """

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, node):
        if self.head is not None:
            node.next_ptr = self.head
        self.head = node

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.both = left | right
    
    def add(self, element):


    def get(self, index):


