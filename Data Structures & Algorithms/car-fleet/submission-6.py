class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = [(p,s) for p, s in zip(position,speed)]
        stack = []
        for p, s in sorted(d)[::-1]:
            stack.append((target-p)/s)
            if stack and len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
