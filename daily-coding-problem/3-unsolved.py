""" Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left' """


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def serialize(root):
    string = ''
    if not root:
        return ' -1'
    string += ' ' + root.data
    string += serialize(root.left)
    string += serialize(root.right)
    return string


# def deserialize(string):
#     try:
#         [left, right] = string.split(' ', 1)
#         print(string, ':', left, ':', right)
#     except:
#         print('exception')
#         return Node(string), ''
#     else:
#         if left == '-1':
#             return None, right
#     root = Node(left)
#     root.left, string = deserialize(right)
#     root.right, string = deserialize(string)
#     return root, string
    
def deserialize(string):
    if string == '':
        return None, string
    try:
        [left, rest] = string.split(' ', 1)
    except:
        return Node(string), ''
    if left == '-1':
        return None, rest
    root = Node(left)
    print('root ->', root.data)
    root.left, string = deserialize(rest)
    print('root.left ->', root.left and root.left.data, ' : ', string)
    root.right, string = deserialize(string)
    print('root.right ->', root.right and root.right.data, ' : ', string)
    # print(root.data, root.left and root.left.data, root.right and root.right.data)
    return root, rest
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node('root', Node('left', Node('left.left')), Node('right'))

string = serialize(root)
string = string.strip()
print(string)
print("--------------")

deserialized_root, _ = deserialize(string)
print("--------------")
inorder(root)
print("--------------")
inorder(deserialized_root)

""" If given Tree is Binary Search Tree?
If the given Binary Tree is Binary Search Tree, we can store it by either storing preorder or postorder traversal.

If given Binary Tree is Complete Tree?
A Binary Tree is complete if all levels are completely filled except possibly the last level and all nodes of last level are as left as possible (Binary Heaps are complete Binary Tree).
For a complete Binary Tree, level order traversal is sufficient to store the tree. We know that the first node is root, next two nodes are nodes of next level, next four nodes are nodes of 2nd level and so on.

If given Binary Tree is Full Tree?
A full Binary is a Binary Tree where every node has either 0 or 2 children. It is easy to serialize such trees as every internal node has 2 children.
We can simply store preorder traversal and store a bit with every node to indicate whether the node is an internal node or a leaf node.

How to store a general Binary Tree?
A simple solution is to store both Inorder and Preorder traversals. This solution requires requires space twice the size of Binary Tree.
We can save space by storing Preorder traversal and a marker for NULL pointers. """