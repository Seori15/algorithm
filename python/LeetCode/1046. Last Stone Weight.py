import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
		# [1] To make max heap, put minus on stones
        heap_stones = [-stone for stone in stones]
        heapq.heapify(heap_stones)

		# [2] calculate first - second
        while len(heap_stones) >= 2:
            first = heapq.heappop(heap_stones)
            second = heapq.heappop(heap_stones)
            heapq.heappush(heap_stones, first-second)
        
        # [3] return final one value with minus
        return -heap_stones[0]
