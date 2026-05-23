class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(curr,currSum,i):
            if currSum == target:
                res.append(curr[:])
            for j in range(i,len(nums)):
                if currSum+nums[j]<=target:
                    curr.append(nums[j])
                    dfs(curr,currSum+nums[j],j)
                    curr.pop()
        dfs([],0,0)
        return res