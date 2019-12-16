""" Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False. """

class Node:
    def __init__(self, data, nextPtr=None):
        self.data = data
        self.nextPtr = nextPtr

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, node):
        if self.head != None:
            node.nextPtr = self.head
        self.head = node

    def print_list(self):
        head = self.head
        while head != None:
            print(head.data)
            head = head.nextPtr

    def palindrome(self):
        stack = []
        head = self.head
        while head != None:
            stack.append(head)
            head = head.nextPtr

        head = self.head
        while head != None:
            item = stack.pop()
            if head.data != item.data:
                return False
            head = head.nextPtr

        return True



arr = [1,2,1]

slist = SinglyLinkedList()

for element in arr:
    slist.insert_at_beginning(Node(element))

print(slist.palindrome())