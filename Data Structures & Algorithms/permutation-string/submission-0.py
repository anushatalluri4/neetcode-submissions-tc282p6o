class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in permutations(s1):
            print("".join(i))
            if "".join(i) in s2:
                return True
        return False