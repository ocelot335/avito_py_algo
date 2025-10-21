import pytest

from homework_4.traversal.bst import BSTNode
from homework_4.validate_bst.validate_bst import validate


def test_validate_on_empty_and_single_node_trees():
    assert validate(None) is True, "Пустое дерево должно быть валидным"
    root = BSTNode(10)
    assert validate(root) is True


def test_validate_on_correct_bst():
    #       10
    #      /  \
    #     5    15
    #    / \   / \
    #   2   7 12  17
    root = BSTNode(10)
    root.left = BSTNode(5)
    root.right = BSTNode(15)
    root.left.left = BSTNode(2)
    root.left.right = BSTNode(7)
    root.right.left = BSTNode(12)
    root.right.right = BSTNode(17)
    assert validate(root) is True


@pytest.mark.parametrize(
    "values",
    [
        ([10, 20, 30, 40]),
        ([40, 30, 20, 10]),
    ],
)
def test_validate_on_correct_degenerate_trees(values):
    root = BSTNode(values[0])
    current = root
    for val in values[1:]:
        if val > current.value:
            current.right = BSTNode(val)
            current = current.right
        else:
            current.left = BSTNode(val)
            current = current.left
    assert validate(root) is True


def test_validate_with_negative_and_zero_values():
    #        0
    #       / \
    #     -10  10
    #     /    /
    #   -20   5
    root = BSTNode(0)
    root.left = BSTNode(-10)
    root.right = BSTNode(10)
    root.left.left = BSTNode(-20)
    root.right.left = BSTNode(5)
    assert validate(root) is True


def test_invalidate_simple_violations():
    root1 = BSTNode(10)
    root1.left = BSTNode(20)
    assert validate(root1) is False

    root2 = BSTNode(10)
    root2.right = BSTNode(5)
    assert validate(root2) is False


@pytest.mark.parametrize(
    "tree_structure",
    [
        {"root": 10, "right": 10},
        {"root": 10, "left": 10},
        {"root": 10, "left": 5, "left-left": 5},
    ],
)
def test_invalidate_duplicate_values(tree_structure):
    root = BSTNode(tree_structure["root"])
    if "right" in tree_structure:
        root.right = BSTNode(tree_structure["right"])
    if "left" in tree_structure:
        root.left = BSTNode(tree_structure["left"])
    if "left-left" in tree_structure:
        root.left.left = BSTNode(tree_structure["left-left"])

    assert validate(root) is False


def test_invalidate_deep_violation_the_classic_case():
    #       10
    #      /
    #     5
    #      \
    #       12
    root = BSTNode(10)
    root.left = BSTNode(5)
    root.left.right = BSTNode(12)
    assert validate(root) is False


def test_invalidate_deep_violation_in_right_subtree():
    #       20
    #         \
    #          30
    #         /
    #        15
    root = BSTNode(20)
    root.right = BSTNode(30)
    root.right.left = BSTNode(15)
    assert validate(root) is False


def test_invalidate_equal_to_grandparent():
    #       20
    #      /
    #     10
    #       \
    #        20
    root = BSTNode(20)
    root.left = BSTNode(10)
    root.left.right = BSTNode(20)
    assert validate(root) is False


def test_invalidate_on_degenerate_tree():
    #    10
    #      \
    #       20
    #         \
    #          15
    root = BSTNode(10)
    root.right = BSTNode(20)
    root.right.right = BSTNode(15)
    assert validate(root) is False
