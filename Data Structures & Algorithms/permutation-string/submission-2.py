class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        countT = [0]*26
        countS = [0]*26
        for i in range(len(s1)):
            countT[ord(s1[i])-ord("a")] += 1
            countS[ord(s2[i])-ord("a")] += 1
        matches = 0
        for i in range(26):
            if countT[i] == countS[i]:
                matches += 1
        l = 0
        for i in range(len(s1),len(s2)):
            if matches == len(countT):
                return True
            ind = ord(s2[i])-ord("a")
            countS[ind] += 1
            if countT[ind] == countS[ind]:
                matches += 1
            elif countT[ind]+1 == countS[ind]:
                matches -= 1
            ind = ord(s2[l])-ord("a")
            countS[ind] -= 1
            if countT[ind] == countS[ind]:
                matches += 1
            elif countT[ind]-1 == countS[ind]:
                matches -= 1
            l += 1
        return matches == 26
            
            
    