class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            x, y = -1*heapq.heappop(maxHeap), -1*heapq.heappop(maxHeap)
            if x!=y:
                heapq.heappush(maxHeap,-(abs(x-y)))
        print(maxHeap)
        return -1 * maxHeap[0] if maxHeap else 0
