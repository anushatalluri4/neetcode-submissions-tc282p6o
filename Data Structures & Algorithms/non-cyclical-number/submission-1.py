class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow!=fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
        return True if fast == 1 else False

    def sumOfSquares(self,n):
        summ = 0
        while n>0:
            rem = n%10
            summ += rem*rem
            n = n//10
        return summ