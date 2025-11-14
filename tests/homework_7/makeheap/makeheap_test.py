# test_minheap.py

import pytest
from homework_7.makeheap.makeheap import (
    MinHeap,
)  # Предполагаем, что класс в файле minheap.py

# --- Тесты для конструктора (__init__) и heapify ---


def test_init_empty():
    """Тест: создание пустой кучи."""
    h = MinHeap()
    assert len(h) == 0


def test_init_does_not_modify_original_list():
    """Тест: конструктор не должен изменять исходный список."""
    original_list = [5, 3, 1, 4, 2]
    _ = MinHeap(original_list)
    assert original_list == [5, 3, 1, 4, 2], "Исходный список был изменен!"


def test_heapify_property():
    h = MinHeap([5, 3, 8, 1, 4])
    assert h.top() == 1


# --- Тесты для top() ---


def test_top_on_empty_heap():
    """Тест: top() на пустой куче должен возвращать None."""
    h = MinHeap()
    assert h.top() is None


def test_top_does_not_remove_element():
    """Тест: top() не должен удалять элемент из кучи."""
    h = MinHeap([3, 1, 2])
    assert h.top() == 1
    assert len(h) == 3


# --- Тесты для insert() ---


def test_insert_into_empty():
    """Тест: вставка в пустую кучу."""
    h = MinHeap()
    h.insert(10)
    assert h.top() == 10
    assert len(h) == 1


def test_insert_new_minimum():
    """Тест: вставка элемента, который должен стать новым минимумом."""
    h = MinHeap([10, 20, 30])
    h.insert(5)
    assert h.top() == 5
    assert len(h) == 4


def test_insert_maintains_heap_property():
    """Тест: серия вставок сохраняет свойство кучи."""
    h = MinHeap()
    elements = [5, 3, 8, 1, 4]
    for el in elements:
        h.insert(el)

    # Проверяем, что после всех вставок корень - минимальный элемент
    assert h.top() == 1


# --- Тесты для pop() ---


def test_pop_from_empty_heap():
    """Тест: pop() на пустой куче должен возвращать None."""
    h = MinHeap()
    assert h.pop() is None


def test_pop_from_single_element_heap():
    """Тест: pop() на куче из одного элемента."""
    h = MinHeap([42])
    assert h.pop() == 42
    assert len(h) == 0
    assert h.top() is None


# --- Комплексные тесты (самые важные) ---


@pytest.mark.parametrize(
    "input_list",
    [
        ([5, 8, 3, 1, 9, 4, 2, 7, 6]),  # Случайный порядок
        ([1, 2, 3, 4, 5, 6, 7, 8, 9]),  # Уже отсортированный
        ([9, 8, 7, 6, 5, 4, 3, 2, 1]),  # Обратный порядок
        ([3, 1, 4, 1, 5, 9, 2, 6]),  # С дубликатами
        ([-5, 0, 10, -10, 5]),  # С отрицательными числами
        ([42]),  # Один элемент
        ([]),  # Пустой список
    ],
)
def test_heap_sort_property(input_list):
    h = MinHeap(input_list)
    sorted_result = sorted(input_list)

    popped_elements = []
    while len(h) > 0:
        popped_elements.append(h.pop())

    assert popped_elements == sorted_result


def test_mixed_operations():
    """Тест: имитация смешанного использования вставки и извлечения."""
    h = MinHeap()
    h.insert(5)
    h.insert(3)
    assert h.top() == 3

    assert h.pop() == 3  # Извлекаем 3, в куче остается [5]
    assert h.top() == 5

    h.insert(1)
    h.insert(8)
    assert h.top() == 1  # Куча примерно [1, 8, 5]

    assert h.pop() == 1
    assert h.pop() == 5
    assert h.pop() == 8

    assert h.pop() is None
    assert len(h) == 0
