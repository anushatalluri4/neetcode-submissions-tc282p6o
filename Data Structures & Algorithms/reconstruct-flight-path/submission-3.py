class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        stack = ["JFK"]
        res = []
        while stack:
            node = stack[-1]
            if not adj[node]:
                res.append(stack.pop())
            else:
                stack.append(adj[node].pop())
        return res[::-1]
                