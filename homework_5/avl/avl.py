class AVLNode:
    def __init__(self, value):
        self.value = value
        self.height: int = 0
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None

    def left_height(self) -> int:
        return self.left.height if self.left is not None else -1

    def right_height(self) -> int:
        return self.right.height if self.right is not None else -1

    def update_height(self) -> int:
        self.height = 1 + max(self.left_height(), self.right_height())


class AVL:
    def __init__(self):
        self.root: AVLNode | None = None

    def find(self, value) -> AVLNode | None:
        if self.root is None:
            return None
        current = self.root

        while True:
            if current is None:
                return None
            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                return current

    def _rotate_clockwise(self, node: AVLNode):
        left_node = node.left
        node.left = left_node.right
        left_node.right = node
        node.update_height()
        left_node.update_height()
        return left_node

    def _rotate_counter_clockwise(self, node: AVLNode):
        right_node = node.right
        node.right = right_node.left
        right_node.left = node
        node.update_height()
        right_node.update_height()
        return right_node

    def _balance(self, node: AVLNode):
        if node is None:
            return None
        left = node.left
        right = node.right
        node.update_height()
        left_val = node.left_height()
        right_val = node.right_height()

        if abs(left_val - right_val) < 2:
            return node
        if left_val > right_val:
            if left.right_height() < left.left_height():
                node = self._rotate_clockwise(node)
            else:
                node.left = self._rotate_counter_clockwise(node.left)
                node = self._rotate_clockwise(node)
        else:
            if right.left_height() < right.right_height():
                node = self._rotate_counter_clockwise(node)
            else:
                node.right = self._rotate_clockwise(node.right)
                node = self._rotate_counter_clockwise(node)
        return node

    def insert(self, value):
        if self.root is None:
            self.root = AVLNode(value)
            return

        def _inner_insert(node: AVLNode, value) -> AVLNode:
            if node is None:
                return AVLNode(value)
            if node.value > value:
                child = _inner_insert(node.left, value)
                node.left = child
            elif node.value < value:
                child = _inner_insert(node.right, value)
                node.right = child
            else:
                return node
            return self._balance(node)

        self.root = _inner_insert(self.root, value)

    def delete(self, value):
        if self.root is None:
            return

        def _inner_delete(node: AVLNode, value) -> AVLNode:
            if node is None:
                return None
            if node.value > value:
                child = _inner_delete(node.left, value)
                node.left = child
            elif node.value < value:
                child = _inner_delete(node.right, value)
                node.right = child
            else:
                if node.height == 0:
                    return None
                next_node = None
                if node.left_height() < node.right_height():
                    next_node = node.right
                    while next_node.left is not None:
                        next_node = next_node.left
                    node.right = _inner_delete(node.right, next_node.value)
                else:
                    next_node = node.left
                    while next_node.right is not None:
                        next_node = next_node.right
                    node.left = _inner_delete(node.left, next_node.value)
                node.value = next_node.value
            return self._balance(node)

        self.root = _inner_delete(self.root, value)
