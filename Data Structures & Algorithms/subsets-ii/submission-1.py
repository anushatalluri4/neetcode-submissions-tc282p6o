class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
        def dfs(curr,i):
            res.append(curr[:])
            for j in range(i,len(nums)):
                if j>i and nums[j-1]==nums[j]:
                    continue
                curr.append(nums[j])
                dfs(curr,j+1)
                curr.pop()
        dfs([],0)
        return res