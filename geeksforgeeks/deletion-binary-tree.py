class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def delete_deepest_node(root, delete_node):
    queue = []
    queue.append(root)
    while queue:
        temp_node = queue.pop(0)
        if temp_node == delete_node:
            temp_node = None
            return
        if temp_node.left:
            if temp_node.left == delete_node:
                temp_node.left = None
                return
            else:
                queue.append(temp_node.left)
        if temp_node.right:
            if temp_node.right == delete_node:
                temp_node.right = None
                return
            else:
                queue.append(temp_node.right)


def delete(root, data):
    if not root:
        return
    if not root.left or not root.right:
        if root.data == data:
            return
        else:
            return root

    deletion_node = None
    queue = []
    queue.append(root)
    while queue:
        temp_node = queue.pop(0)
        if temp_node.data == data:
            deletion_node = temp_node
        if temp_node.left:
            queue.append(temp_node.left)
        if temp_node.right:
            queue.append(temp_node.right)

    if deletion_node:
        deletion_node.data = temp_node.data
        delete_deepest_node(root, temp_node)
    return root


if __name__ == "__main__":
    root = Node(10, Node(11, Node(7), Node(12)), Node(9, Node(15), Node(8)))

    print("Tree")
    inorder(root)
    print()

    root = delete(root, 11)

    print("Tree")
    inorder(root)
    print()
