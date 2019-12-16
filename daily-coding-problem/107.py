""" Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
 """

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def level_order_traversal(root):
    if root is None:
        return
    queue.append(root)
    while(len(queue) > 0):
        item = queue.pop(0)
        print(item.data)
        if item.left is not None:
            queue.append(item.left)
        if item.right is not None:
            queue.append(item.right)

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
queue = []
level_order_traversal(root)
