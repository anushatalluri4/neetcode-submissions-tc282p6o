class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def dfs(node):
            for nei in adj[node]:
                if not nei in visit:
                    visit.add(nei)
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                res += 1 
        return res