class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(curr,i):
            res.append(curr[:])
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                curr.append(nums[j])
                dfs(curr,j+1)
                curr.pop()
        res=[]
        dfs([],0)
        return res
        