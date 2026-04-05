class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def dfs(path,i,curr):
            if curr == target:
                res.append(path[:])
                return
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j]+curr>target:
                    return
                path.append(candidates[j])
                dfs(path,j+1,curr+candidates[j])
                path.pop()
           
        res=[]
        dfs([],0,0)
        return res
        