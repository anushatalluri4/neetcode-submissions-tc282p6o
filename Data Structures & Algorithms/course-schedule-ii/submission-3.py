class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses
        for crc, pre in prerequisites:
            indegree[pre]+=1
            adj[crc].append(pre)
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res = []
        finish = 0
        while q:
            node = q.popleft()
            finish+=1
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return res[::-1] if finish == numCourses else []