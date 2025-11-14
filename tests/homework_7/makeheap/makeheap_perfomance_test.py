import random
import pytest
from homework_7.makeheap.makeheap import makeheap_n_log_n, makeheap

# TEST_ARRAY_SIZE = 50_000
TEST_ARRAY_SIZE = 5_000

large_random_array = [
    random.randint(0, 1_000_000) for _ in range(TEST_ARRAY_SIZE)
]
array_with_duplicates = [
    random.randint(0, 100) for _ in range(TEST_ARRAY_SIZE)
]
already_sorted_array = list(range(TEST_ARRAY_SIZE))
reverse_sorted_array = list(range(TEST_ARRAY_SIZE, 0, -1))


def parse_time_from_output(captured_output: str) -> float:
    for line in captured_output.strip().split("\n"):
        if line.startswith("Time:"):
            return float(line.split(":")[1].strip())


def verify_heap_is_correct(heap, original_list):
    sorted_original = sorted(original_list)
    popped_elements = []
    while len(heap) > 0:
        popped_elements.append(heap.pop())
    assert popped_elements == sorted_original


@pytest.mark.parametrize(
    "test_name, test_array",
    [
        ("Большой случайный массив", large_random_array),
        ("Массив с большим количеством дубликатов", array_with_duplicates),
        ("Уже отсортированный массив", already_sorted_array),
        ("Массив, отсортированный в обратном порядке", reverse_sorted_array),
    ],
)
def test_heap_build_performance(test_name, test_array, capsys):
    print(f"\n--- Начало теста: {test_name} (размер: {len(test_array)}) ---")

    arr_copy_1 = test_array.copy()
    heap_slow = makeheap_n_log_n(arr_copy_1)
    captured = capsys.readouterr()
    time_slow = parse_time_from_output(captured.out)
    verify_heap_is_correct(heap_slow, test_array)

    arr_copy_2 = test_array.copy()
    heap_fast = makeheap(arr_copy_2)
    captured = capsys.readouterr()
    time_fast = parse_time_from_output(captured.out)
    verify_heap_is_correct(heap_fast, test_array)

    print(f"Результаты для '{test_name}':")
    print(f"  Построение за O(n log n): {time_slow:.6f} c.")
    print(f"  Построение за O(n):        {time_fast:.6f} c.")

    if time_fast > 0:
        print(f"  O(n) быстрее в {time_slow / time_fast:.2f} раз.")
    print("--- Конец теста ---")
