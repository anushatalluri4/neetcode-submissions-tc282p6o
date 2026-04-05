class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        adj = defaultdict(list)
        for s, d, c in flights:
            adj[s].append([d,c])
        q = deque([(0,src, 0)]) # cost, source, stops
        while q:
            cost, s, stops = q.popleft()
            if stops>k:
                continue
            for nei, neicost in adj[s]:
                upcost = neicost+cost
                if upcost < prices[nei]:
                    prices[nei] = upcost
                    q.append((upcost,nei,stops+1))
        return -1 if prices[dst] == float("inf") else prices[dst]