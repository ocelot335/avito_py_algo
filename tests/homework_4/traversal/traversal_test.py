import pytest
from homework_4.traversal.bst import BST
from homework_4.traversal.traversal import (
    pre_order,
    pre_order_wo_recursion,
    post_order,
    post_order_wo_recursion,
    in_order,
    in_order_wo_recursion,
    reverse_pre_order,
    reverse_pre_order_wo_recursion,
    reverse_post_order,
    reverse_post_order_wo_recursion,
    reverse_in_order,
    reverse_in_order_wo_recursion,
)


@pytest.fixture
def empty_tree() -> BST:
    return BST()


@pytest.fixture
def single_node_tree() -> BST:
    tree = BST()
    tree.insert(10)
    return tree


@pytest.fixture
def populated_tree() -> BST:
    tree = BST()
    values = [10, 5, 15, 2, 7, 12, 17]
    for value in values:
        tree.insert(value)
    #       10
    #      /  \
    #     5    15
    #    / \   / \
    #   2   7 12  17
    return tree


def test_all_traversals_on_empty_tree(empty_tree: BST):
    all_functions = [
        pre_order,
        pre_order_wo_recursion,
        post_order,
        post_order_wo_recursion,
        in_order,
        in_order_wo_recursion,
        reverse_pre_order,
        reverse_pre_order_wo_recursion,
        reverse_post_order,
        reverse_post_order_wo_recursion,
        reverse_in_order,
        reverse_in_order_wo_recursion,
    ]
    for func in all_functions:
        assert (
            func(empty_tree) == []
        ), f"Функция {func.__name__} не прошла тест на пустом дереве"


def test_all_traversals_on_single_node_tree(single_node_tree: BST):
    all_functions = [
        pre_order,
        pre_order_wo_recursion,
        post_order,
        post_order_wo_recursion,
        in_order,
        in_order_wo_recursion,
        reverse_pre_order,
        reverse_pre_order_wo_recursion,
        reverse_post_order,
        reverse_post_order_wo_recursion,
        reverse_in_order,
        reverse_in_order_wo_recursion,
    ]
    for func in all_functions:
        assert func(single_node_tree) == [
            10
        ], f"Функция {func.__name__} не прошла тест на одном узле"


def test_in_order_versions(populated_tree: BST):
    expected = [2, 5, 7, 10, 12, 15, 17]
    recursive_result = in_order(populated_tree)
    iterative_result = in_order_wo_recursion(populated_tree)

    assert (
        recursive_result == iterative_result
    ), "Рекурсивная и итеративная in_order не совпадают!"
    assert iterative_result == expected, "Итеративная in_order неверна!"


def test_pre_order_versions(populated_tree: BST):
    expected = [10, 5, 2, 7, 15, 12, 17]
    recursive_result = pre_order(populated_tree)
    iterative_result = pre_order_wo_recursion(populated_tree)

    assert recursive_result == iterative_result
    assert iterative_result == expected


def test_post_order_versions(populated_tree: BST):
    expected = [2, 7, 5, 12, 17, 15, 10]
    recursive_result = post_order(populated_tree)
    iterative_result = post_order_wo_recursion(populated_tree)

    assert recursive_result == iterative_result
    assert iterative_result == expected


def test_reverse_in_order_versions(populated_tree: BST):
    expected = [17, 15, 12, 10, 7, 5, 2]
    recursive_result = reverse_in_order(populated_tree)
    iterative_result = reverse_in_order_wo_recursion(populated_tree)

    assert recursive_result == iterative_result
    assert iterative_result == expected


def test_reverse_pre_order_versions(populated_tree: BST):
    expected = [10, 15, 17, 12, 5, 7, 2]
    recursive_result = reverse_pre_order(populated_tree)
    iterative_result = reverse_pre_order_wo_recursion(populated_tree)

    assert recursive_result == iterative_result
    assert iterative_result == expected


def test_reverse_post_order_versions(populated_tree: BST):
    expected = [17, 12, 15, 7, 2, 5, 10]
    recursive_result = reverse_post_order(populated_tree)
    iterative_result = reverse_post_order_wo_recursion(populated_tree)

    assert recursive_result == iterative_result
    assert iterative_result == expected
