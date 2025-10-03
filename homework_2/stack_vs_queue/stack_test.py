import pytest
from .stack import Stack


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def filled_stack():
    stack = Stack()
    stack.push(10)
    stack.push("twenty")
    stack.push(True)
    return stack


def test_stack_creation(empty_stack):
    assert len(empty_stack) == 0
    assert empty_stack.top() is None


def test_push(empty_stack):
    empty_stack.push(100)
    assert len(empty_stack) == 1
    assert empty_stack.top() == 100

    empty_stack.push("hello")
    assert len(empty_stack) == 2
    assert empty_stack.top() == "hello"


def test_pop(filled_stack):
    assert len(filled_stack) == 3

    assert filled_stack.pop() is True
    assert len(filled_stack) == 2
    assert filled_stack.top() == "twenty"

    assert filled_stack.pop() == "twenty"
    assert len(filled_stack) == 1

    assert filled_stack.pop() == 10
    assert len(filled_stack) == 0


def test_pop_from_empty_stack_raises_error(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.pop()


def test_peek(filled_stack):
    initial_size = len(filled_stack)
    assert filled_stack.top() is True
    assert len(filled_stack) == initial_size
    assert filled_stack.top() is True
