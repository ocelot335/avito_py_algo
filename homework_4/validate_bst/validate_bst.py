from homework_4.traversal.bst import BSTNode


def validate(root: BSTNode) -> bool:
    if root is None:
        return True

    def inner_validate(node: BSTNode, less_value, bigger_value) -> bool:
        if node is None:
            return True

        if node.value <= less_value:
            return False
        if node.value >= bigger_value:
            return False

        return inner_validate(
            node.left, less_value, node.value
        ) and inner_validate(node.right, node.value, bigger_value)

    return inner_validate(root, float("-inf"), float("inf"))
