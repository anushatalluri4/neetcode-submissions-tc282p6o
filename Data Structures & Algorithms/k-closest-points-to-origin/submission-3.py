class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = x*x + y*y
            heapq.heappush(minHeap,[-dist,x,y])
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res

        
