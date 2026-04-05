class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        count=0
        for i in s:
            if i == '{' or i=='[' or i=='(':
                stack.append(i)
                count+=1
            elif i==')':
                if len(stack)==0:
                    return False
                a=stack.pop()
                count-=1
                if a!='(':
                    return False
            elif i==']':
                if len(stack)==0:
                    return False
                b=stack.pop()
                count-=1
                if b!='[':
                    return False
            elif i=='}':
                if len(stack)==0:
                    return False
                c=stack.pop()
                count-=1
                if c!='{':
                    return False
        if count==0:
            return True
        else:
            return False