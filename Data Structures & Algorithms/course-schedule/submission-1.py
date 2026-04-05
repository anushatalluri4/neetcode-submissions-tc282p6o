class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        q = collections.deque()
        for src, dst in prerequisites:
            dep[dst] += 1
            adj[src].append(dst)
        for i in range(numCourses):
            if dep[i] == 0:
                q.append(i)
        print(q)
        finish = 0
        while q:
            node = q.popleft()
            print(node)
            finish += 1
            for nei in adj[node]:
                dep[nei] -= 1
                if dep[nei] == 0:
                    q.append(nei)
        return finish == numCourses

