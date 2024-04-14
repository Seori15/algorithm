class Solution:
		# [A] Covert list to max heap
    def max_heapify(self, arr: List[int]) -> None:
        last = len(arr) // 2 - 1
        for current in range(last, -1, -1):
            while current <= last:
                child = current * 2 + 1
                sibling = child + 1
                if sibling < len(arr) and arr[child] < arr[sibling]:
                    child = sibling
                if arr[current] < arr[child]:
                    arr[current], arr[child] = arr[child], arr[current]
                    current = child
                else:
                    break

		# [B] Pop from max heap
    def heappop(self, heap: List[int]) -> int:
        if len(heap) == 1:
            return heap.pop()

        pop_data, heap[0] = heap[0], heap.pop()
        current, child = 0, 1
        while child < len(heap):
            sibling = child + 1
            if sibling < len(heap) and heap[child] < heap[sibling]:
                child = sibling
            if heap[current] < heap[child]:
                heap[current], heap[child] = heap[child], heap[current]
                current = child
                child = current * 2 + 1
            else:
                break
        return pop_data

		# [1] return kth heappop from max heap(nums).
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.max_heapify(nums)
        for i in range(k-1):
            self.heappop(nums)
        return self.heappop(nums)