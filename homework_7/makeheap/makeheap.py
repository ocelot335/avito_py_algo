from homework_6.compare.compare import time_count


class MinHeap:
    def __init__(self, arr: list = []):
        self.heap = arr.copy()
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._sift_down(i)

    def top(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _sift_down(self, current_node):
        while True:
            left_node = 2 * current_node + 1
            right_node = 2 * current_node + 2
            have_left = left_node < len(self.heap)
            have_right = right_node < len(self.heap)
            left_value = self.heap[left_node] if have_left else float("inf")
            right_value = self.heap[right_node] if have_right else float("inf")
            if not have_left and not have_right:
                break

            if not (
                left_value >= self.heap[current_node]
                and right_value >= self.heap[current_node]
            ):
                if right_value <= left_value:
                    self.heap[right_node], self.heap[current_node] = (
                        self.heap[current_node],
                        self.heap[right_node],
                    )
                    current_node = right_node
                else:
                    self.heap[left_node], self.heap[current_node] = (
                        self.heap[current_node],
                        self.heap[left_node],
                    )
                    current_node = left_node
            else:
                break
        return

    def pop(self):
        if not self.heap:
            return None
        min_value = self.heap[0]
        to_swap = self.heap.pop()
        if len(self.heap) == 0:
            return min_value
        self.heap[0] = to_swap
        self._sift_down(0)
        return min_value

    def _sift_up(self, current_node):
        while current_node != 0:
            parent_node = (current_node - 1) // 2
            if self.heap[parent_node] > self.heap[current_node]:
                self.heap[parent_node], self.heap[current_node] = (
                    self.heap[current_node],
                    self.heap[parent_node],
                )
                current_node = parent_node
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        current_node = len(self.heap) - 1
        self._sift_up(current_node)
        return

    def __len__(self):
        return len(self.heap)


@time_count
def makeheap_n_log_n(arr: list) -> MinHeap:
    heap = MinHeap()
    for elem in arr:
        heap.insert(elem)
    return heap


@time_count
def makeheap(arr: list) -> MinHeap:
    heap = MinHeap(arr)
    return heap
