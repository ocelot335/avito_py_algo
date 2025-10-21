from homework_4.traversal.bst import BSTNode


def is_balanced(root: BSTNode) -> bool:
    if root is None:
        return True
    is_valid = True

    def inner_validate(node: BSTNode) -> int:
        nonlocal is_valid

        if node is None:
            return 0

        left_height = inner_validate(node.left)
        right_height = inner_validate(node.right)
        if abs(left_height - right_height) > 1:
            is_valid = False

        return 1 + max(left_height, right_height)

    inner_validate(root)
    return is_valid
