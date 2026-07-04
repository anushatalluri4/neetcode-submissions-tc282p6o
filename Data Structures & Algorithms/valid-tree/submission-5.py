class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        stack = [(0,-1)]
        visit = set()
        while stack:
            curr, par = stack.pop()
            visit.add(curr)
            for nei in adj[curr]:
                if nei == par:
                    continue
                if nei in visit:
                    return False
                if nei not in visit:
                    stack.append((nei,curr))
        return len(visit) == n
        

