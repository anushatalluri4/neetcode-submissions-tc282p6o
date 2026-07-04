class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        indegree = [0]*numCourses
        for crc,pre in prerequisites:
            graph[pre].append(crc)
            indegree[crc]+=1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish = 0
        while q:
            curr = q.popleft()
            finish += 1
            for nei in graph[curr]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses
