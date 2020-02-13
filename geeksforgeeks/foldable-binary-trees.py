class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def foldable(left_subtree, right_subtree):
    if not left_subtree and not right_subtree:
        return True
    if not left_subtree or not right_subtree:
        return False

    return foldable(left_subtree.left, right_subtree.right) and foldable(
        left_subtree.right, right_subtree.left
    )


def foldable_helper(root):
    if not root:
        return True

    return foldable(root.left, root.right)


if __name__ == "__main__":
    root = Node(1, Node(2, None, Node(4)), Node(3, Node(5)))

    print(f"Is Foldable {foldable_helper(root)}")
