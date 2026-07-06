class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k
        while l<=r:
            mid = (l+r)//2
            time = 0
            for i in piles:
                time+=math.ceil(i/mid)
            if time<=h:
                r=mid-1
            else:
                l=mid+1
        return l