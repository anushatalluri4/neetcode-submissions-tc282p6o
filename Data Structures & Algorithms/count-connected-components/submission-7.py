class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def bfs(node):
            q = deque([node])
            visit.add(node)
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
        res = 0
        for i in range(n):
            if i not in visit:
                bfs(i)
                res += 1
        return res   
            