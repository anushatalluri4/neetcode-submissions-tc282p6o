class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        if len(edges)!=n-1:
            return False
        adj = [[] for i in range(n)]
        q = deque()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q.append([0,-1])
        visit = set()
        visit.add(0)
        while q:
            node, par = q.popleft()
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append([nei,node])
        return len(visit)==n