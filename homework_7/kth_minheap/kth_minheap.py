from homework_7.makeheap.makeheap import MinHeap
import heapq


def kth(nums: list, k: int) -> int:
    heap = MinHeap()
    for num in nums:
        if len(heap) == k:
            if num > heap.top():
                heap.pop()
                heap.insert(num)
        else:
            heap.insert(num)
    return heap.top()


def kth_heapq(nums: list, k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) == k:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        else:
            heapq.heappush(heap, num)
    return heap[0]


def kth_heapq_replace(nums: list, k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) == k:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        else:
            heapq.heappush(heap, num)
    return heap[0]
