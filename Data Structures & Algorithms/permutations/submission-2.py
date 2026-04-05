class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr,pick):
            if len(curr) == len(nums):
                res.append(curr[:])
            for j in range(len(nums)):
                if not pick[j]:
                    curr.append(nums[j])
                    pick[j] = True
                    dfs(curr,pick)
                    curr.pop()
                    pick[j] = False
        dfs([],[False] * len(nums))
        return res