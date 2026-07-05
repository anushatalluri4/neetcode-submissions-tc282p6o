class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(curr,pick):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for j in range(len(nums)):
                if not pick[j]:
                    pick[j] = True
                    curr.append(nums[j])
                    dfs(curr,pick)
                    pick[j] = False
                    curr.pop()
        dfs([],[False]*len(nums))
        return res