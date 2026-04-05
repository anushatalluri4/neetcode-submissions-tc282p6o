class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}
        visit=set()
        for crc, pre in prerequisites:
            preMap[crc].append(pre)
        def dfs(crc):
            if crc in visit:
                return False
            if preMap[crc]==[]:
                return True
            visit.add(crc)
            for p in preMap[crc]:
                if not dfs(p):
                    return False
            visit.remove(crc)
            return True
        for crc in range(numCourses):
            if not dfs(crc):
                return False
        return True