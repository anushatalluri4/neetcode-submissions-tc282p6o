class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for num in nums:
            d[num]+=1
        freq = [[] for i in range(len(nums)+1)]
        for key in d.keys():
            freq[d[key]].append(key)
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res