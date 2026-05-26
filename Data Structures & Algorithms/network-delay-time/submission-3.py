class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        minHeap = [(0,k)]
        res = 0
        visit = set()
        while minHeap:
            w,node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = w
            for nei,wei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,(w+wei,nei))
        return res if len(visit)== n else -1