class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        adj = [[] for i in range(n+1)]
        indegree = [0]*(n+1)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        q = deque()
        for i in range(n+1):
            if indegree[i] == 1:
                q.append(i)
        while q:
            curr = q.popleft()
            indegree[curr]-=1
            for nei in adj[curr]:
                indegree[nei]-=1
                if indegree[nei] == 1:
                    q.append(nei)
        for u, v in edges[::-1]:
            if indegree[u]>0 and indegree[v]>0:
                return [u,v]
        return []
        