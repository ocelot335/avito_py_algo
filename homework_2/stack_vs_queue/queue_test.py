import pytest
from .queue import Queue


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def filled_queue():
    q = Queue()
    q.push("first")
    q.push("second")
    q.push("third")
    return q


def test_queue_creation(empty_queue):
    assert len(empty_queue) == 0
    assert empty_queue.front() is None
    assert empty_queue.back() is None


def test_push_on_empty_queue(empty_queue):
    empty_queue.push(10)
    assert len(empty_queue) == 1
    assert empty_queue.front() == 10
    assert empty_queue.back() == 10


def test_push_on_filled_queue(filled_queue):
    filled_queue.push("fourth")
    assert len(filled_queue) == 4
    assert filled_queue.front() == "first"
    assert filled_queue.back() == "fourth"


def test_pop_fifo_order(filled_queue):
    assert filled_queue.pop() == "first"
    assert len(filled_queue) == 2
    assert filled_queue.front() == "second"

    assert filled_queue.pop() == "second"
    assert len(filled_queue) == 1
    assert filled_queue.front() == "third"

    assert filled_queue.pop() == "third"
    assert len(filled_queue) == 0


def test_pop_until_empty_resets_state(filled_queue):
    filled_queue.pop()
    filled_queue.pop()
    filled_queue.pop()

    assert len(filled_queue) == 0
    assert filled_queue.front_node is None
    assert filled_queue.back_node is None
    assert filled_queue.front() is None
    assert filled_queue.back() is None


def test_pop_from_empty_queue_raises_error(empty_queue):
    with pytest.raises(IndexError, match="pop from empty queue"):
        empty_queue.pop()


def test_peeks_do_not_modify_queue(filled_queue):
    initial_size = len(filled_queue)
    assert filled_queue.front() == "first"
    assert filled_queue.back() == "third"

    assert len(filled_queue) == initial_size
    assert filled_queue.front() == "first"
    assert filled_queue.back() == "third"


def test_len_after_multiple_operations(empty_queue):
    assert len(empty_queue) == 0
    empty_queue.push(1)
    empty_queue.push(2)
    assert len(empty_queue) == 2
    empty_queue.pop()
    assert len(empty_queue) == 1
    empty_queue.push(3)
    assert len(empty_queue) == 2
