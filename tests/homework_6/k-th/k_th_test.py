import pytest
from homework_6.kth.kth import kth

test_cases = [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ([1, 2, 3, 4, 5, 6], 1, 6),
    ([1, 2, 3, 4, 5, 6], 6, 1),
    ([1, 2, 3, 4, 5, 6], 3, 4),
    ([7, 7, 7, 7, 7], 1, 7),
    ([7, 7, 7, 7, 7], 5, 7),
    ([3, 5, 2, 5, 3], 1, 5),
    ([3, 5, 2, 5, 3], 2, 5),
    ([3, 5, 2, 5, 3], 3, 3),
    ([10, 20, 30, 40, 50], 2, 40),
    ([50, 40, 30, 20, 10], 4, 20),
    ([100, 1], 1, 100),
    ([100, 1], 2, 1),
    ([42], 1, 42),
]


@pytest.mark.parametrize("nums, k, expected", test_cases)
def test_kth_with_various_inputs(nums, k, expected):
    nums_copy = list(nums)

    result = kth(nums_copy, k)

    assert result == expected


def test_kth_randomized():
    import random

    for _ in range(100):
        size = random.randint(1, 200)
        nums = [random.randint(-1000, 1000) for _ in range(size)]
        k = random.randint(1, size)

        expected_result = sorted(nums)[-k]

        nums_copy = list(nums)
        actual_result = kth(nums_copy, k)

        assert actual_result == expected_result
