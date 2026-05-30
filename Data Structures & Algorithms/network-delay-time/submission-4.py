class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        adj = [[] for i in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        minHeap = [(0,k)]
        minw = 0
        while minHeap:
            wei, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            minw = wei
            for nei,nwei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,(nwei+wei,nei))
        return minw if len(visit)==n else -1