import pytest

from homework_5.avl.avl import AVL, AVLNode
from homework_4.validate_bst.validate_bst import validate
from homework_4.valid_balanced.valid_balanced import is_balanced


def _is_avl_satisfied(node: AVLNode) -> bool:
    return validate(node) and is_balanced(node)


@pytest.fixture
def tree():
    return AVL()


def test_initialization(tree):
    assert tree.root is None


def test_insert_first_node(tree):
    tree.insert(10)
    assert tree.root.value == 10
    assert tree.root.height == 0
    assert tree.root.left is None
    assert tree.root.right is None


def test_find_existing(tree):
    values = [10, 5, 15]
    for v in values:
        tree.insert(v)

    node = tree.find(5)
    assert node is not None
    assert node.value == 5


def test_find_non_existing(tree):
    values = [10, 5, 15]
    for v in values:
        tree.insert(v)

    assert tree.find(100) is None
    assert tree.find(0) is None


def test_insert_duplicate(tree):
    tree.insert(10)
    tree.insert(5)
    tree.insert(10)

    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right is None
    assert tree.root.height == 1


def test_insert_triggers_rr_rotation(tree):
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)

    assert tree.root.value == 20
    assert tree.root.height == 1
    assert tree.root.left.value == 10
    assert tree.root.right.value == 30
    assert _is_avl_satisfied(tree.root)


def test_insert_triggers_ll_rotation(tree):
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)

    assert tree.root.value == 20
    assert tree.root.height == 1
    assert tree.root.left.value == 10
    assert tree.root.right.value == 30
    assert _is_avl_satisfied(tree.root)


def test_insert_triggers_rl_rotation(tree):
    tree.insert(10)
    tree.insert(30)
    tree.insert(20)

    assert tree.root.value == 20
    assert tree.root.height == 1
    assert tree.root.left.value == 10
    assert tree.root.right.value == 30
    assert _is_avl_satisfied(tree.root)


def test_insert_triggers_lr_rotation(tree):
    tree.insert(30)
    tree.insert(10)
    tree.insert(20)

    assert tree.root.value == 20
    assert tree.root.height == 1
    assert tree.root.left.value == 10
    assert tree.root.right.value == 30
    assert _is_avl_satisfied(tree.root)


def test_delete_leaf_node(tree):
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)

    tree.delete(5)

    assert tree.root.value == 10
    assert tree.root.left is None
    assert tree.root.right.value == 15
    assert _is_avl_satisfied(tree.root)


def test_delete_node_with_one_child(tree):
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)

    tree.delete(5)

    assert tree.root.value == 10
    assert tree.root.left.value == 3
    assert tree.root.right.value == 15
    assert _is_avl_satisfied(tree.root)


def test_delete_node_with_two_children(tree):
    values = [20, 10, 30, 5, 15, 25, 35, 12, 17]
    for v in values:
        tree.insert(v)

    tree.delete(10)

    assert tree.find(10) is None
    node = tree.find(12)
    assert node.left.value == 5
    assert node.right.value == 15
    assert _is_avl_satisfied(tree.root)


def test_delete_root_with_two_children(tree):
    values = [20, 10, 30]
    for v in values:
        tree.insert(v)

    tree.delete(20)

    assert tree.root.value == 10
    assert tree.root.right.value == 30
    assert tree.root.left is None
    assert _is_avl_satisfied(tree.root)


def test_delete_triggers_rotation(tree):
    values = [10, 5, 20, 3, 7, 15, 25, 22]
    for v in values:
        tree.insert(v)

    tree = AVL()
    tree.insert(10)
    tree.insert(5)
    tree.insert(20)
    tree.insert(25)

    tree.delete(5)

    assert tree.root.value == 20
    assert tree.root.left.value == 10
    assert tree.root.right.value == 25
    assert _is_avl_satisfied(tree.root)


def test_stress_insert_delete(tree):
    size = 100
    for i in range(size):
        tree.insert(i)
        assert _is_avl_satisfied(tree.root)

    for i in range(size - 1, -1, -1):
        tree.delete(i)
        assert _is_avl_satisfied(tree.root)

    assert tree.root is None
