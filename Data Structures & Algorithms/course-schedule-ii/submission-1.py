class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]
        for crc, pre in prerequisites:
            indegree[pre] += 1
            adj[crc].append(pre)
        q = collections.deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        finish = 0
        res = []
        while q:
            node = q.popleft()
            finish +=  1
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res[::-1] if finish == numCourses else []