import pytest
from validate import validate

test_cases = [
    ([1, 2, 3, 4, 5], [1, 3, 5, 4, 2], True),
    ([1, 2, 3], [3, 1, 2], False),
    ([1, 2, 3, 4], [4, 3, 2, 1], True),
    ([1, 2], [1, 2], True),  # push(1), pop(1), push(2), pop(2)
    ([1, 2, 3, 4, 5], [4, 5, 3, 1, 2], False),
    ([], [], True),
    ([10], [10], True),
    ([*range(5)], [*range(4, -1, -1)], True),
    ([1, 0], [0, 1], True),  # push(1), push(0), pop(0), pop(1)
    ([1, 0], [1, 0], True),  # push(1), pop(1), push(0), pop(0)
]


@pytest.mark.parametrize("pushed, popped, expected", test_cases)
def test_validate_sequences(pushed, popped, expected):
    assert validate(pushed, popped) == expected
