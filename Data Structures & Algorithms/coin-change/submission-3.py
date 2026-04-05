class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res = 0
        seen = [False]*(amount+1)
        q = deque([0])
        while q:
            res += 1
            for i in range(len(q)):
                a = q.popleft()
                for c in coins:
                    nxt = c+a
                    if nxt == amount:
                        return res
                    if nxt>amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)
        return -1