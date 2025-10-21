import pytest

from homework_4.traversal.bst import BST, BSTNode
from homework_4.validate_bst.validate_bst import validate


def _check_parents_recursively(node: BSTNode | None, parent: BSTNode | None):
    if node is None:
        return
    assert node.parent == parent, f"Ошибка parent у узла {node.value}"
    _check_parents_recursively(node.left, node)
    _check_parents_recursively(node.right, node)


def assert_is_valid_bst(tree: BST):
    is_bst = validate(tree.root)
    assert is_bst, "Нарушено свойство двоичного дерева поиска!"

    if tree.root is not None:
        assert (
            tree.root.parent is None
        ), "У корня дерева должен быть parent = None"
    _check_parents_recursively(tree.root, None)


@pytest.fixture
def tree() -> BST:
    return BST()


def test_insert_on_empty_tree(tree: BST):
    tree.insert(10)
    assert tree.root.value == 10
    assert_is_valid_bst(tree)


def test_degenerate_tree_right(tree: BST):
    values = [10, 20, 30, 40, 50]
    for v in values:
        tree.insert(v)
    assert_is_valid_bst(tree)

    tree.delete(10)
    assert tree.find(10) is None
    assert_is_valid_bst(tree)

    tree.delete(50)
    assert tree.find(50) is None
    assert_is_valid_bst(tree)


def test_degenerate_tree_left(tree: BST):
    values = [50, 40, 30, 20, 10]
    for v in values:
        tree.insert(v)
    assert_is_valid_bst(tree)

    tree.delete(30)
    assert tree.find(30) is None
    assert_is_valid_bst(tree)


def test_zigzag_tree(tree: BST):
    values = [10, 20, 15, 5, 7]
    for v in values:
        tree.insert(v)
    assert_is_valid_bst(tree)

    tree.delete(10)
    assert tree.find(10) is None
    assert_is_valid_bst(tree)


def test_complex_delete_scenario_successor_deep(tree: BST):
    values = [20, 10, 40, 30, 50, 25, 35, 22, 27, 32, 37]
    for v in values:
        tree.insert(v)
    assert_is_valid_bst(tree)

    tree.delete(20)
    assert tree.find(20) is None
    assert_is_valid_bst(tree)


def test_complex_delete_scenario_successor_has_child(tree: BST):
    values = [20, 10, 40, 30, 50, 25, 35, 27, 32, 37]
    for v in values:
        tree.insert(v)
    assert_is_valid_bst(tree)

    tree.delete(20)
    assert tree.find(20) is None
    assert_is_valid_bst(tree)


def test_multiple_deletes(tree: BST):
    values = [10, 5, 15, 2, 7, 12, 17, 6, 8, 16, 18]
    for v in values:
        tree.insert(v)
    assert_is_valid_bst(tree)

    operations = [10, 12, 7, 18]
    for val in operations:
        tree.delete(val)
        assert tree.find(val) is None
        assert_is_valid_bst(tree)  # Проверка после КАЖДОГО удаления


def test_delete_until_empty(tree: BST):
    values = [10, 5, 15, 2, 7]
    for v in values:
        tree.insert(v)

    delete_order = [5, 10, 2, 15, 7]
    for v in delete_order:
        tree.delete(v)
        assert_is_valid_bst(tree)

    assert tree.root is None


def test_operations_on_single_node_tree(tree: BST):
    tree.insert(10)
    assert_is_valid_bst(tree)

    tree.delete(20)  # Попытка удалить несуществующий
    assert tree.root.value == 10
    assert_is_valid_bst(tree)

    tree.delete(10)  # Удаляем единственный узел
    assert tree.root is None
    assert_is_valid_bst(tree)
