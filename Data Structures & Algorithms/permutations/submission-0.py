class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr,pick):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for j in range(len(nums)):
                if not pick[j]:
                    curr.append(nums[j])
                    pick[j]=True
                    dfs(curr,pick)
                    curr.pop()
                    pick[j]=False
        res = []
        dfs([],[False]*len(nums))
        return res