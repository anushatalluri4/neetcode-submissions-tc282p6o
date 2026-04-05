class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l,r = len(temperatures)-2, len(temperatures)-1
        res=[0] * len(temperatures)
        res[len(temperatures)-1]=0
        while(l>=0 and r>l):
            if temperatures[l]<temperatures[r]:
                res[l]=1
                l-=1
                r-=1
            else:
                j=r+1
                while j<len(temperatures):
                    if temperatures[l]<temperatures[j]:
                        res[l]=j-l
                        break
                    else:
                        j+=1
                l -= 1
                r -= 1
        return res
        
                
                

