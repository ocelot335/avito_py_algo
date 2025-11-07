import random
import sys
import pytest
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

sys.setrecursionlimit(30000)

# TEST_ARRAY_SIZE = 100_000
TEST_ARRAY_SIZE = 10_000

large_random_array = [
    random.randint(0, 1_000_000) for _ in range(TEST_ARRAY_SIZE)
]

array_with_duplicates = [random.randint(0, 10) for _ in range(TEST_ARRAY_SIZE)]

already_sorted_array = list(range(TEST_ARRAY_SIZE))


def parse_time_from_output(captured_output: str) -> float:
    for line in captured_output.strip().split("\n"):
        if line.startswith("Time:"):
            return float(line.split(":")[1].strip())
    pytest.fail("Не удалось извлечь время выполнения из вывода функции.")


@pytest.mark.parametrize(
    "test_name, test_array",
    [
        ("Большой случайный массив", large_random_array),
        ("Массив с большим количеством дубликатов", array_with_duplicates),
        ("Уже отсортированный массив", already_sorted_array),
    ],
)
def test_sorting_performance(test_name, test_array, capsys):
    print(f"\n--- Начало теста: {test_name} (размер: {len(test_array)}) ---")

    expected_sorted = sorted(test_array)

    arr_copy = test_array.copy()
    result_merge = merge_sort(arr_copy)
    captured = capsys.readouterr()
    time_merge = parse_time_from_output(captured.out)
    assert result_merge == expected_sorted, "merge_sort работает некорректно"

    arr_copy = test_array.copy()
    result_merge = merge_sort_iterative_top_down(arr_copy)
    captured = capsys.readouterr()
    time_merge_iterate_top_down = parse_time_from_output(captured.out)
    assert (
        result_merge == expected_sorted
    ), "merge_sort_iterative_top_down работает некорректно"

    arr_copy = test_array.copy()
    result_merge = merge_sort_iterative(arr_copy)
    captured = capsys.readouterr()
    time_merge_iterate = parse_time_from_output(captured.out)
    assert (
        result_merge == expected_sorted
    ), "merge_sort_iterative работает некорректно"

    arr_copy = test_array.copy()
    result_quick = quick_sort(arr_copy)
    captured = capsys.readouterr()
    time_quick = parse_time_from_output(captured.out)
    assert result_quick == expected_sorted, "quick_sort работает некорректно"

    arr_copy = test_array.copy()
    result_quick_iterative = quick_sort_iterative(arr_copy)
    captured = capsys.readouterr()
    time_quick_iterative = parse_time_from_output(captured.out)
    assert (
        result_quick_iterative == expected_sorted
    ), "quick_sort_iterative работает некорректно"

    arr_copy = test_array.copy()
    result_inplace = quick_sort_in_place(arr_copy)
    captured = capsys.readouterr()
    time_inplace = parse_time_from_output(captured.out)
    assert (
        result_inplace == expected_sorted
    ), "quick_sort_in_place работает некорректно"

    arr_copy = test_array.copy()
    result_inplace_russian = quick_sort_in_place_russian(arr_copy)
    captured = capsys.readouterr()
    time_inplace_russian = parse_time_from_output(captured.out)
    assert (
        result_inplace_russian == expected_sorted
    ), "quick_sort_in_place_russian работает некорректно"

    print(f"Результаты для '{test_name}':")
    print(f"  quick_sort:                   {time_quick:.6f} c.")
    print(f"  quick_sort_iterative:         {time_quick_iterative:.6f} c.")
    print(f"  quick_sort_in_place:          {time_inplace:.6f} c.")
    print(f"  quick_sort_in_place_russian:  {time_inplace_russian:.6f} c.")
    print(f"  merge_sort:                   {time_merge:.6f} c.")
    print(f"  merge_sort_iterative:         {time_merge_iterate:.6f} c.")
    print(
        f"  merge_sort_iterative_top_down:{time_merge_iterate_top_down:.6f} c."
    )
    print("--- Конец теста ---")
