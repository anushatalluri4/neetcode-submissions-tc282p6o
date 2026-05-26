class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for i in range(n)]
        for u, v, cost in flights:
                adj[u].append((v,cost))
        q = deque([(0,src,0)]) # cost, src, stops
        prices = [float("inf")]*n
        while q:
            cost, src, stops = q.popleft()
            if stops>k:
                continue
            for nei, neicost in adj[src]:
                upcost = neicost+cost
                if upcost<prices[nei]:
                    prices[nei] = upcost
                    q.append((upcost,nei,stops+1))
        return prices[dst] if prices[dst]!=float("inf") else -1