class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = max(piles)
        while l<=r:
            mid = (l + r)//2
            eat = 0
            for p in piles:
                eat += math.ceil(p/(mid))
            if eat <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans