class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(curr,total,i):
            if total == target:
                res.append(curr[:])
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if total+candidates[j]>target:
                    return
                curr.append(candidates[j])
                dfs(curr, total+candidates[j],j+1)
                curr.pop()
        dfs([],0,0)
        return res