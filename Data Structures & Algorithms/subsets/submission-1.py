class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,path,i):
            res.append(path[:])
            for i in range(i,len(nums)):
                path.append(nums[i])
                dfs(nums,path,i+1)
                path.pop()
        res=[]
        dfs(nums,[],0)
        return res

        