class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res= []
        def dfs(i,total,curr):
            if total == target:
                res.append(curr[:])
                return
            for j in range(i,len(nums)):
                if total+nums[j]>target:
                    continue
                curr.append(nums[j])
                dfs(j,total+nums[j],curr)
                curr.pop()
        dfs(0,0,[])
        return res