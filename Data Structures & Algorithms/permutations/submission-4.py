class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False]*len(nums)
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for j in range(len(nums)):
                if not pick[j]:
                    curr.append(nums[j])
                    pick[j] = True
                    dfs(curr)
                    curr.pop()
                    pick[j]=False
        dfs([])
        return res