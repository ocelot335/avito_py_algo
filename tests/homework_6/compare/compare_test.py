import pytest
import random

from homework_6.compare.compare import (
    merge_sort,
    quick_sort,
    quick_sort_in_place,
    quick_sort_in_place_russian,
)
from homework_6.iterative.iterative import (
    merge_sort_iterative_top_down,
    merge_sort_iterative,
    quick_sort_iterative,
)

SORTING_FUNCTIONS = [
    merge_sort,
    quick_sort,
    quick_sort_in_place,
    quick_sort_in_place_russian,
    merge_sort_iterative_top_down,
    merge_sort_iterative,
    quick_sort_iterative,
]

TEST_CASES = [
    [],
    [1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [3, 1, 4, 1, 5, 9, 2, 6, 5],
    [-5, 0, 10, -15, 3],
    [7, 7, 7, 7, 7],
]


@pytest.mark.parametrize("sort_function", SORTING_FUNCTIONS)
@pytest.mark.parametrize("input_list", TEST_CASES)
def test_sorting_on_various_cases(sort_function, input_list):
    list_copy = input_list.copy()

    expected = sorted(input_list)

    result = sort_function(list_copy)

    assert (
        result == expected
    ), f"Ошибка в {sort_function.__name__} для списка {input_list}"


@pytest.mark.parametrize("sort_function", SORTING_FUNCTIONS)
def test_sorting_large_random_list(sort_function):
    random_list = [random.randint(-1000, 1000) for _ in range(500)]
    list_copy = random_list.copy()

    expected = sorted(random_list)
    result = sort_function(list_copy)

    assert (
        result == expected
    ), f"Ошибка в {sort_function.__name__} для большого случайного списка"


@pytest.mark.parametrize(
    "sort_function, is_inplace",
    [
        (merge_sort, False),
        (quick_sort, False),
        (quick_sort_in_place, True),
    ],
)
def test_list_modification_behavior(sort_function, is_inplace):
    original_list = [3, 1, 2]
    list_to_sort = original_list.copy()

    sorted_result = sort_function(list_to_sort)

    assert sorted_result == [1, 2, 3]

    if is_inplace:
        assert (
            sorted_result is list_to_sort
        ), f"{sort_function.__name__} должна возвращать тот же объект списка"
        assert (
            list_to_sort != original_list
        ), f"{sort_function.__name__} должна была изменить список"
    else:
        assert (
            sorted_result is not list_to_sort
        ), f"{sort_function.__name__} должна возвращать новый объект списка"
        assert (
            list_to_sort == original_list
        ), f"{sort_function.__name__} не должна была изменять исходный список"
