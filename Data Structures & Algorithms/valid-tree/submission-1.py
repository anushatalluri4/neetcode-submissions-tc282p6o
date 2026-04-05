class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        if len(edges) != n-1:
            return False
        adj = [[] for i in range(n)]
        visit = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node,prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        return dfs(0,-1) and n == len(visit) 
