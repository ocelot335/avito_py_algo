class BSTNode:
    def __init__(self, value):
        self.value = value
        self.parent: BSTNode | None = None
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BST:
    def __init__(self):
        self.root = None

    def find(self, value) -> BSTNode:
        if self.root is None:
            return None
        current_nearest = self.root

        while True:
            if current_nearest.value > value:
                if current_nearest.left is None:
                    return None
                else:
                    current_nearest = current_nearest.left
            elif current_nearest.value < value:
                if current_nearest.right is None:
                    return None
                else:
                    current_nearest = current_nearest.right
            else:
                return current_nearest

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return

        current_nearest = self.root

        while True:
            if current_nearest.value > value:
                if current_nearest.left is None:
                    current_nearest.left = BSTNode(value)
                    current_nearest.left.parent = current_nearest
                    return
                else:
                    current_nearest = current_nearest.left
            elif current_nearest.value < value:
                if current_nearest.right is None:
                    current_nearest.right = BSTNode(value)
                    current_nearest.right.parent = current_nearest
                    return
                else:
                    current_nearest = current_nearest.right
            else:
                return

    def delete(self, value):
        node_to_delete = self.find(value)
        if node_to_delete is None:
            return

        def change_son_for_parent(
            current_son: BSTNode, new_son: BSTNode | None
        ):
            if new_son is not None:
                new_son.parent = current_son.parent

            if current_son == self.root:
                self.root = new_son
            elif current_son.parent.left == current_son:
                current_son.parent.left = new_son
            elif current_son.parent.right == current_son:
                current_son.parent.right = new_son

        if node_to_delete.left is None and node_to_delete.right is None:
            change_son_for_parent(node_to_delete, None)
        elif node_to_delete.left is None and node_to_delete.right is not None:
            change_son_for_parent(node_to_delete, node_to_delete.right)
        elif node_to_delete.left is not None and node_to_delete.right is None:
            change_son_for_parent(node_to_delete, node_to_delete.left)
        else:
            next_node = node_to_delete.right
            while next_node.left is not None:
                next_node = next_node.left
            node_to_delete.value, next_node.value = (
                next_node.value,
                node_to_delete.value,
            )
            change_son_for_parent(next_node, next_node.right)
