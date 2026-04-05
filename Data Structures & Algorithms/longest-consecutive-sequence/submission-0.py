class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=defaultdict(int)
        res=0
        for i in nums:
            if not d[i]:
                d[i]=d[i-1]+d[i+1]+1
                d[i-d[i-1]]=d[i]
                d[i+d[i+1]]=d[i]
            res=max(res,d[i])
        return res
                    
        