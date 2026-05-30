class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        minHeap = [(0,0)]
        visit = set()
        minwei = 0
        while len(visit)<len(points):
            dist,node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            minwei += dist
            for dist2,nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,(dist2,nei))
        return minwei