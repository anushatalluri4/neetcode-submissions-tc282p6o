class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,p in flights:
            adj[u].append((v,p))
        dist = [[float("inf")]*(k+2) for i in range(n)] 
        dist[src][0] = 0
        q = deque([(src,0,0)])
        while q:
            node,price,flights_used = q.popleft()
            if flights_used == k+1:
                continue
            for nei,nei_price in adj[node]:
                cost = price + nei_price
                if cost<dist[nei][flights_used+1]:
                    dist[nei][flights_used+1] = cost
                    q.append((nei,cost,flights_used+1))
        ans = min(dist[dst])
        return ans if ans!=float("inf") else -1
