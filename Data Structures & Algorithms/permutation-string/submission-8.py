class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        chars1, chars2 = [0]*26, [0]*26
        for i in range(len(s1)):
            chars1[ord(s1[i])-ord("a")]+=1
            chars2[ord(s2[i])-ord("a")]+=1
        matches = 0
        l=0
        for i in range(26):
            if chars1[i]==chars2[i]:
                matches+=1
        for j in range(len(s1),len(s2)):
            if matches == 26:
                return True
            index = ord(s2[j])-ord("a")
            chars2[index]+=1
            if chars1[index]==chars2[index]:
                matches+=1
            elif chars1[index]+1==chars2[index]:
                matches-=1
            index = ord(s2[l])-ord("a")
            chars2[index]-=1
            if chars2[index]==chars1[index]:
                matches+=1
            if chars2[index]==chars1[index]-1:
                matches-=1
            l+=1
        return matches==26
