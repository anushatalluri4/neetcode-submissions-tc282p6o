class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def bfs(node):
            q = deque([node])
            while q:
                curr = q.popleft()
                visit.add(curr)
                for nei in adj[curr]:
                    if nei not in visit:
                        q.append(nei)
        res = 0
        for i in range(n):
            if i not in visit:
                bfs(i)
                res += 1
        return res
        
