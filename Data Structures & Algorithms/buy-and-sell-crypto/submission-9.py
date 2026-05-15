class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0
        for r in range(len(prices)):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                maxp = max(maxp,profit)
            else:
                l = r
        return maxp

