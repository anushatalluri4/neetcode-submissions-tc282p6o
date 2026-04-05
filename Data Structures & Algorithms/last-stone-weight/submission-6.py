class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-i for i in stones]
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            x, y = -1*heapq.heappop(minHeap), -1*heapq.heappop(minHeap)
            if x!=y:
                heapq.heappush(minHeap, -abs(x-y))
        return -1*minHeap[0] if minHeap else 0

