class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        I model the flights as a directed weighted graph using an adjacency list.

Since the problem restricts the number of stops, I use BFS where each state stores (current_cost, city, stops_used).

For every city, I relax its outgoing edges. If I find a cheaper cost to reach a neighbor, I update the cost and push the new state into the queue with one additional stop.

The stop count prevents exploring paths that exceed k stops, while the prices array prunes more expensive paths.

This gives a time complexity of O(E * K) and avoids the limitations of standard Dijkstra when a stop constraint is present.

Relaxation meaning "I found a better (shorter/cheaper) way to reach a node, so I'll update my best-known cost."
        """
        adj = defaultdict(list)
        for u,v,c in flights:
            adj[u].append((v,c))
        q = deque([(0,src,0)])
        prices = [float("inf")]*n
        while q:
            cost,node,stops = q.popleft()
            if stops>k:
                continue
            for nei, neicost in adj[node]:
                upcost = cost+neicost
                if prices[nei]>upcost:
                    prices[nei]=upcost
                    q.append((upcost,nei,stops+1))
        return prices[dst] if prices[dst]!=float("inf") else -1
                
