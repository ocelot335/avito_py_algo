# tests/homework_4/test_is_balanced.py

import pytest
from homework_4.traversal.bst import BSTNode
from homework_4.valid_balanced.valid_balanced import is_balanced

# ====================================================================
# Часть 1: Тесты на СБАЛАНСИРОВАННЫХ деревьях (ожидаем True)
# ====================================================================


@pytest.mark.parametrize(
    "description, root_node",
    [
        ("Пустое дерево", None),
        ("Дерево из одного узла", BSTNode(10)),
    ],
)
def test_balanced_on_trivial_cases(description, root_node):
    assert (
        is_balanced(root_node) is True
    ), f"{description} должно быть сбалансированным"


def test_balanced_perfectly_symmetric_tree():
    #    10
    #   /  \
    #  5    15
    root = BSTNode(10)
    root.left = BSTNode(5)
    root.right = BSTNode(15)
    assert is_balanced(root) is True


def test_balanced_at_the_limit():
    #    10
    #   /  \
    #  5    15
    # /
    # 2
    root = BSTNode(10)
    root.left = BSTNode(5)
    root.right = BSTNode(15)
    root.left.left = BSTNode(2)
    assert is_balanced(root) is True


def test_balanced_full_three_levels():
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
    assert is_balanced(root) is True


def test_balanced_long_but_balanced_path():
    #       40
    #      /  \
    #     20   60
    #    / \   / \
    #   10 30 50 70
    #  /
    # 5
    root = BSTNode(40)
    root.left = BSTNode(20)
    root.right = BSTNode(60)
    root.left.left = BSTNode(10)
    root.left.right = BSTNode(30)
    root.right.left = BSTNode(50)
    root.right.right = BSTNode(70)
    root.left.left.left = BSTNode(5)
    assert is_balanced(root) is True


@pytest.mark.parametrize(
    "description, values",
    [
        ("Палка вправо", [10, 20, 30]),
        ("Палка влево", [30, 20, 10]),
    ],
)
def test_unbalanced_degenerate_trees(description, values):
    root = BSTNode(values[0])
    current = root
    for val in values[1:]:
        if val > current.value:
            current.right = BSTNode(val)
            current = current.right
        else:
            current.left = BSTNode(val)
            current = current.left
    assert is_balanced(root) is False


def test_unbalanced_at_root():
    #    10
    #   /
    #  5
    # /
    # 2
    root = BSTNode(10)
    root.left = BSTNode(5)
    root.left.left = BSTNode(2)
    assert is_balanced(root) is False


def test_unbalanced_deep_inside_right_subtree():
    #         10
    #        /  \
    #       5    20
    #      / \      \
    #     2   7      30
    #                 \
    #                  40
    root = BSTNode(10)
    root.left = BSTNode(5)
    root.right = BSTNode(20)
    root.left.left = BSTNode(2)
    root.left.right = BSTNode(7)
    root.right.right = BSTNode(30)
    root.right.right.right = BSTNode(40)
    assert is_balanced(root) is False


def test_unbalanced_deep_inside_left_subtree():
    #         50
    #        /  \
    #       20   60
    #      / \
    #     10  30
    #    /
    #   5
    #  /
    # 2
    root = BSTNode(50)
    root.right = BSTNode(60)
    root.left = BSTNode(20)
    root.left.right = BSTNode(30)
    root.left.left = BSTNode(10)
    root.left.left.left = BSTNode(5)
    root.left.left.left.left = BSTNode(2)
    assert is_balanced(root) is False


def test_unbalanced_looks_symmetric_but_isnt():
    #       50
    #      /  \
    #     40   60
    #    /  \
    #   30  45
    #  /
    # 20
    root = BSTNode(50)
    root.right = BSTNode(60)
    root.left = BSTNode(40)
    root.left.left = BSTNode(30)
    root.left.right = BSTNode(45)
    root.left.left.left = BSTNode(20)
    assert is_balanced(root) is False
