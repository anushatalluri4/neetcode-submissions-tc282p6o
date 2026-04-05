class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        freq = [[] for i in range(len(nums)+1)]
        for key in d:
            freq[d[key]].append(key)
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                print(j)
                res.append(j)
                if len(res)==k:
                    return res