class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr,i):
            res.append(curr[:])
            for j in range(i,len(nums)):
                curr.append(nums[j])
                dfs(curr,j+1)
                curr.pop()
        dfs([],0)
        return res