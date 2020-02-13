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


def is_operator(character):
    return True if character in ["+", "-", "*", "/", "^"] else False


def construct_tree(postfix):
    stack = []

    for character in postfix:
        if not is_operator(character):
            node = Node(character)
            stack.append(node)
        else:
            node = Node(character)
            node.right = stack.pop()
            node.left = stack.pop()

            stack.append(node)

    return stack.pop()


def evaluate(left_value, right_value, operator):
    switcher = {
        "+": int(left_value) + int(right_value),
        "-": int(left_value) - int(right_value),
        "*": int(left_value) * int(right_value),
        "/": int(left_value) / int(right_value),
    }
    return switcher.get(operator)


def solve_expression(root):
    if not is_operator(root.data):
        return root.data
    left_value = solve_expression(root.left)
    right_value = solve_expression(root.right)
    return evaluate(left_value, right_value, root.data)


if __name__ == "__main__":
    postfix = "12+34*5*-"

    root = construct_tree(postfix)

    inorder(root)
    print()

    print(solve_expression(root))
