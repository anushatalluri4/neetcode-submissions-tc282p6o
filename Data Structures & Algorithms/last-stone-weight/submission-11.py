class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)<=1:
            return stones[0]
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if x!=y:
                heapq.heappush(maxHeap,-abs(x-y))
        return -maxHeap[0] if maxHeap else 0
