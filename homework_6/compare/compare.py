import functools
import random
import time


def time_count(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        time_amount = time.perf_counter() - start_time
        print(f"Time: {time_amount}")
        return result

    return wrapper


@time_count
def merge_sort(array: list) -> list:
    def inner_recursion(array: list):
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left = inner_recursion(array[:middle])
        right = inner_recursion(array[middle:])
        new_array = []
        left_id = 0
        right_id = 0
        while left_id != len(left) and right_id != len(right):
            if left[left_id] <= right[right_id]:
                new_array.append(left[left_id])
                left_id += 1
            else:
                new_array.append(right[right_id])
                right_id += 1
        new_array.extend(left[left_id:])
        new_array.extend(right[right_id:])
        return new_array

    return inner_recursion(array)


@time_count
def quick_sort(array: list) -> list:
    def inner_recursion(array: list):
        if len(array) <= 1:
            return array
        pivot_id = random.randint(0, len(array) - 1)
        pivot = array[pivot_id]
        left = []
        right = []
        middle = []
        for i in range(len(array)):
            if array[i] < pivot:
                left.append(array[i])
            elif array[i] > pivot:
                right.append(array[i])
            else:
                middle.append(array[i])
        left = inner_recursion(left)
        right = inner_recursion(right)
        return left + middle + right

    return inner_recursion(array)


# Голладнский национальный флаг
@time_count
def quick_sort_in_place(array: list) -> list:
    def inner_recursion(array: list, left: int, right: int):
        if right - left <= 1:
            return array
        pivot_index = random.randint(left, right - 1)
        array[pivot_index], array[right - 1] = (
            array[right - 1],
            array[pivot_index],
        )
        pivot = array[right - 1]
        count_less_than_pivot = 0
        id_of_smallest_that_bigger_than_pivot = right - 1
        index = left
        while index <= id_of_smallest_that_bigger_than_pivot:
            if array[index] < pivot:
                array[left + count_less_than_pivot], array[index] = (
                    array[index],
                    array[left + count_less_than_pivot],
                )
                count_less_than_pivot += 1
                index += 1
            elif array[index] > pivot:
                array[id_of_smallest_that_bigger_than_pivot], array[index] = (
                    array[index],
                    array[id_of_smallest_that_bigger_than_pivot],
                )
                id_of_smallest_that_bigger_than_pivot -= 1
            else:
                index += 1

        inner_recursion(array, left, left + count_less_than_pivot)
        inner_recursion(
            array, id_of_smallest_that_bigger_than_pivot + 1, right
        )
        return

    inner_recursion(array, 0, len(array))
    return array


# Русский национальный флаг
@time_count
def quick_sort_in_place_russian(array: list) -> list:
    def inner_recursion(array: list, left: int, right: int):
        if right - left <= 1:
            return array
        pivot_index = random.randint(left, right - 1)
        array[pivot_index], array[right - 1] = (
            array[right - 1],
            array[pivot_index],
        )
        pivot = array[right - 1]
        count_less_than_pivot = 0
        count_equal_pivot = 0
        i = left
        while i < right:
            if array[i] < pivot:
                array[left + count_less_than_pivot], array[i] = (
                    array[i],
                    array[left + count_less_than_pivot],
                )
                count_less_than_pivot += 1
                if array[i] == pivot:
                    count_equal_pivot -= 1
            if array[i] == pivot:
                (
                    array[left + count_less_than_pivot + count_equal_pivot],
                    array[i],
                ) = (
                    array[i],
                    array[left + count_less_than_pivot + count_equal_pivot],
                )
                count_equal_pivot += 1
            i += 1

        inner_recursion(array, left, left + count_less_than_pivot)
        inner_recursion(
            array, left + count_less_than_pivot + count_equal_pivot, right
        )
        return

    inner_recursion(array, 0, len(array))
    return array
