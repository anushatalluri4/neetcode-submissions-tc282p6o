import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for point in points:
            x, y = point
            dis = math.sqrt((0-x)*(0-x) + (0-y)*(0-y))
            print(dis)
            heapq.heappush(minHeap, [-dis,point])
            print(minHeap)
            while len(minHeap)>k:
                heapq.heappop(minHeap)
        res = []
        for p in minHeap:
            res.append(p[1])
        return res
            