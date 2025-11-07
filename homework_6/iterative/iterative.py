import random
from homework_6.compare.compare import time_count
from homework_2.stack_vs_queue.stack import Stack


@time_count
def merge_sort_iterative(array: list) -> list:
    ping_pong_array_merge = [None] * len(array)

    def merge(left, delta):
        nonlocal ping_pong_array_merge
        right_end = min(left + 2 * delta, len(array))
        left_id = left
        right_id = left + delta
        ping_pong_id = left
        while left_id < left + delta and right_id < right_end:
            if array[left_id] <= array[right_id]:
                ping_pong_array_merge[ping_pong_id] = array[left_id]
                left_id += 1
            else:
                ping_pong_array_merge[ping_pong_id] = array[right_id]
                right_id += 1
            ping_pong_id += 1
        left_end = min(len(array), left + delta)
        while left_id < left_end:
            ping_pong_array_merge[ping_pong_id] = array[left_id]
            left_id += 1
            ping_pong_id += 1
        while right_id < right_end:
            ping_pong_array_merge[ping_pong_id] = array[right_id]
            right_id += 1
            ping_pong_id += 1
        return

    # сортируем соседние массивы длины 2,4,8,16...
    current_size_to_sort = 2
    is_array_on_place = True
    while current_size_to_sort < 2 * len(array):
        left = 0
        while left < len(array):
            merge(left, current_size_to_sort // 2)
            left += current_size_to_sort
        current_size_to_sort *= 2
        array, ping_pong_array_merge = (ping_pong_array_merge, array)
        is_array_on_place ^= True
    if not is_array_on_place:
        array, ping_pong_array_merge = ping_pong_array_merge, array
        array[:] = ping_pong_array_merge

    return array


@time_count
def merge_sort_iterative_top_down(array: list) -> list:
    stack = Stack()
    stack.push((0, len(array), False))
    stack_frame_temp_array = []
    while len(stack) != 0:
        left, right, mode = stack.pop()
        if right - left <= 1:
            continue
        middle = (right + left) // 2
        if not mode:
            stack.push((left, right, True))
            stack.push((left, middle, False))
            stack.push((middle, right, False))
        else:
            stack_frame_temp_array.clear()
            left_id = left
            right_id = middle
            while left_id != middle and right_id != right:
                if array[left_id] <= array[right_id]:
                    stack_frame_temp_array.append(array[left_id])
                    left_id += 1
                else:
                    stack_frame_temp_array.append(array[right_id])
                    right_id += 1
            stack_frame_temp_array.extend(array[left_id:middle])
            stack_frame_temp_array.extend(array[right_id:right])
            array[left:right] = stack_frame_temp_array
    return array


@time_count
def quick_sort_iterative(array: list) -> list:
    stack = Stack()
    stack.push((0, len(array)))
    while len(stack) != 0:
        left, right = stack.pop()
        if right - left <= 1:
            continue
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
        stack.push((left, left + count_less_than_pivot))
        stack.push((id_of_smallest_that_bigger_than_pivot + 1, right))
    return array
