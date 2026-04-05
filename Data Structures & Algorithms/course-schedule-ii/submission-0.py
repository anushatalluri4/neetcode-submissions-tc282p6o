class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i:[] for i in range(numCourses)}
        visit=set()
        cycle =set()
        res=[]
        for crc, pre in prerequisites:
            preMap[crc].append(pre)
        def dfs(crc):
            if crc in visit:
                return True
            if crc in cycle:
                return False
            cycle.add(crc)
            for p in preMap[crc]:
                if not dfs(p):
                    return False
            cycle.remove(crc)
            visit.add(crc)
            res.append(crc)
            return True
        for crc in range(numCourses):
            if not dfs(crc):
                return []
        return res