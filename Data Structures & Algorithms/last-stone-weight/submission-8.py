class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        print(heap)
        while len(heap)>1:
            x,y = -heapq.heappop(heap), -heapq.heappop(heap)
            print(x,y)
            if x!=y:
                heapq.heappush(heap,-abs(y-x))
        return -heap[0] if heap else 0


