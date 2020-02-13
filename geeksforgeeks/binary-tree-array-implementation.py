class Tree:
    def __init__(self):
        self.tree_array = [-1] * 10

    def set_root(self, data):
        if self.tree_array[0] != -1:
            print("Tree has root already")
        else:
            self.tree_array[0] = data

    def set_left(self, parent_index, data):
        if self.tree_array[parent_index] == -1:
            print(f"Parent is absent at {parent_index} for {data}")
        else:
            self.tree_array[(2 * parent_index) + 1] = data

    def set_right(self, parent_index, data):
        if self.tree_array[parent_index] == -1:
            print(f"Parent is absent at {parent_index} for {data}")
        else:
            self.tree_array[(2 * parent_index) + 2] = data

    def print_tree(self):
        for node in self.tree_array:
            print(node, end=" ")


if __name__ == "__main__":
    tree = Tree()

    tree.set_root("A")
    tree.set_right(0, "C")
    tree.set_left(1, "D")
    tree.set_right(1, "E")
    tree.set_right(2, "F")

    print("Tree")
    tree.print_tree()
    print()
