import pytest
import math

from homework_5.permutations.permutations import permutations


@pytest.mark.parametrize(
    "input_list, expected_permutations",
    [
        ([], [[]]),
        ([1], [[1]]),
        (["a", "b"], [["a", "b"], ["b", "a"]]),
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ),
        ([1, 1], [[1, 1], [1, 1]]),
    ],
)
def test_permutations_results(input_list, expected_permutations):
    result = permutations(input_list)

    assert sorted(result) == sorted(expected_permutations)

    result_set = set(tuple(p) for p in result)
    expected_set = set(tuple(p) for p in expected_permutations)
    assert result_set == expected_set


def test_permutations_count():
    input_list = [1, 2, 3, 4]
    n = len(input_list)
    expected_count = math.factorial(n)

    result = permutations(input_list)

    assert len(result) == expected_count


def test_permutations_empty_list():
    assert permutations([]) == [[]]


def test_permutations_single_element_list():
    assert permutations(["test"]) == [["test"]]
