class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        for crc, pre in prerequisites:
            indegree[pre] += 1
            adj[crc].append(pre)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses