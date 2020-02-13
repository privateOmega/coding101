class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def continuous(root):
    if root:
        return True
    if not root.left and not root.right:
        return True

    if not root.left:
        return abs(root.data - root.right.data) == 1 and continuous(root.right)

    if not root.right:
        return abs(root.data - root.left.data) == 1 and continuous(root.left)

    return (
        abs(root.data - root.left.data) == 1
        and abs(root.data - root.right.data) == 1
        and continuous(root.left)
        and continuous(root.right)
    )


if __name__ == "__main__":
    root = Node(3, Node(2, Node(1), Node(3)), Node(4, None, Node(5)))

    print(f"Tree continuous? {continuous(root)}")
