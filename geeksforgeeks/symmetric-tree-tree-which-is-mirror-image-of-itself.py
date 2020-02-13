class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def symetric(first_root, second_root):
    if not first_root and not second_root:
        return True

    if first_root and second_root:
        if first_root.data == second_root.data:
            return symetric(first_root.left, second_root.right) and symetric(first_root.right, second_root.left)

    return False

def symetric_helper(root):
    return symetric(root, root)

if __name__ == "__main__":
    root = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))

    print(symetric_helper(root))
