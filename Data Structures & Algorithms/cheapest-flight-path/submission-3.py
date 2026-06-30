
from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))

        # dist[city][stops] = minimum cost to reach 'city'
        # using exactly 'stops' flights
        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        q = deque([(src, 0, 0)])  # (city, cost, flights_used)

        while q:
            node, cost, flights_used = q.popleft()

            if flights_used == k + 1:
                continue

            for nei, price in adj[node]:
                newCost = cost + price

                if newCost < dist[nei][flights_used + 1]:
                    dist[nei][flights_used + 1] = newCost
                    q.append((nei, newCost, flights_used + 1))

        ans = min(dist[dst])
        return ans if ans != float("inf") else -1
