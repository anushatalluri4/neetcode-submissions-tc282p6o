import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub("\W","",s).lower()
        print(s)
        if s==s[::-1]:
            return True
        else:
            return False