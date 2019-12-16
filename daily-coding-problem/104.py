""" Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False. """

class Node:
    def __init__(self, data, prevPtr=None, nextPtr=None):
        self.data = data
        self.prevPtr = prevPtr
        self.nextPtr = nextPtr

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, node):
        if self.head == None:
            self.tail = node
        else:
            node.nextPtr = self.head
            self.head.prevPtr = node
        self.head = node

    def insert_at_end(self, node):
        if self.tail == None:
            self.head = node
        else:
            node.prevPtr = self.tail
            self.tail.nextPtr = node
        self.tail = node

    def print_list(self):
        head = self.head
        while head != None:
            print(head.data)
            head = head.nextPtr

    def palindrome(self):
        head = self.head
        tail = self.tail
        while head != None and tail != None:
            if head.data != tail.data:
                return False
            head = head.nextPtr
            tail = tail.prevPtr

        return True



arr = [1,2,24,1]

dlist = DoublyLinkedList()

for element in arr:
    dlist.insert_at_end(Node(element))

print(dlist.palindrome())