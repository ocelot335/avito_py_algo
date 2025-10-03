from typing import List
import pytest

from .merge import LinkedListNode, merge_lists, merge_lists_dummy


def create_list(values: List[int]) -> LinkedListNode:
    if not values:
        return None

    head = LinkedListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = LinkedListNode(val)
        current = current.next
    return head


def list_to_values(head: LinkedListNode) -> List[int]:
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values


merge_functions_to_test = [merge_lists, merge_lists_dummy]

test_cases = [
    pytest.param([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4], id="basic_case"),
    pytest.param([], [], [], id="both_empty"),
    pytest.param([], [0], [0], id="first_empty"),
    pytest.param([1, 3, 5], [], [1, 3, 5], id="second_empty"),
    pytest.param([1], [2], [1, 2], id="single_elements"),
    pytest.param([2], [1], [1, 2], id="single_elements_swapped"),
    pytest.param([5, 6, 7], [1, 2, 3], [1, 2, 3, 5, 6, 7], id="no_overlap"),
    pytest.param([1, 2], [3, 4, 5], [1, 2, 3, 4, 5], id="first_list_shorter"),
]


@pytest.mark.parametrize("merge_function", merge_functions_to_test)
@pytest.mark.parametrize("first_vals, second_vals, expected_vals", test_cases)
def test_merge_lists(merge_function, first_vals, second_vals, expected_vals):
    first_list = create_list(first_vals)
    second_list = create_list(second_vals)

    merged_head = merge_function(first_list, second_list)

    result_vals = list_to_values(merged_head)
    # print(result_vals, " !! ", expected_vals)
    assert result_vals == expected_vals
