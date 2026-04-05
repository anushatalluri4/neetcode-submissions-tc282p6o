class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1) 
        # bits(i >> 1) → number of 1s in i without the last bit
        # (i & 1) → add 1 if the last bit is 1

        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)

        return res