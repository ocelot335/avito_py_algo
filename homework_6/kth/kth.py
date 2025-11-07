import random


def kth(nums: list, k: int) -> int:
    array = nums[:]
    left_edge = 0
    right_edge = len(array)
    k = len(array) - k + 1
    while right_edge - left_edge > 1:
        pivot_id = random.randint(left_edge, right_edge - 1)
        array[pivot_id], array[right_edge - 1] = (
            array[right_edge - 1],
            array[pivot_id],
        )
        pivot = array[right_edge - 1]
        less_cnt = 0
        for i in range(left_edge, right_edge):
            if array[i] <= pivot:
                array[i], array[left_edge + less_cnt] = (
                    array[left_edge + less_cnt],
                    array[i],
                )
                less_cnt += 1
        if less_cnt > k:
            right_edge = left_edge + less_cnt - 1
        elif less_cnt == k:
            return pivot
        else:
            left_edge = left_edge + less_cnt
            k -= less_cnt
    return array[left_edge]


print(kth([3, 2, 1, 5, 6, 4], k=2))
