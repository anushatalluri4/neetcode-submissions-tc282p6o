class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        minHeap = [(0,k)]
        res = 0
        visit = set()
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            res = t
            for nei, time in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,(t+time,nei))
        return res if len(visit) == n else -1

