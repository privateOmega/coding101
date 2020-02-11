""" A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1 """


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def helper(root):
    if not root:
        return 0, True
    lcount, is_left_unival = helper(root.left)
    rcount, is_right_unival = helper(root.right)
    count = lcount + rcount
    if is_left_unival and is_right_unival:
        if root.left is not None and root.left.data != root.data:
            return count, False
        if root.right is not None and root.right.data != root.data:
            return count, False
        return count + 1, True
    return count, False

def count_unival(root):
    count, _ = helper(root)
    return count

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print(count_unival(root))