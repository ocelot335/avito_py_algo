import pytest
from homework_7.kth_minheap.kth_minheap import (
    kth,
    kth_heapq,
    kth_heapq_replace,
)

all_kth_functions = [kth, kth_heapq, kth_heapq_replace]


@pytest.mark.parametrize("func", all_kth_functions)
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([7, 6, 5, 4, 3, 2, 1], 1, 7),
        ([7, 6, 5, 4, 3, 2, 1], 7, 1),
        ([-1, -5, 2, 0], 2, 0),
        ([3, 3, 3, 3, 3], 3, 3),
        ([10, 20, 20, 30], 2, 20),
        ([42], 1, 42),
    ],
)
def test_kth_correctness(func, nums, k, expected):
    assert (
        func(nums, k) == expected
    ), f"Функция {func.__name__} провалилась на данных {nums}, k={k}"


def test_functions_give_identical_results():
    import random

    nums = [random.randint(0, 1000) for _ in range(100)]
    k = 150

    expected = kth_heapq_replace(nums, k)

    assert kth(nums, k) == expected
    assert kth_heapq(nums, k) == expected
