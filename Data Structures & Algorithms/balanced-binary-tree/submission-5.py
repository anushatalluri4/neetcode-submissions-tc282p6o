# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True,0]
            lefth = dfs(root.left)
            righth = dfs(root.right)
            bal = lefth[0] and righth[0] and abs(lefth[1]-righth[1])<=1
            return [bal,1+max(lefth[1],righth[1])]
        return(dfs(root)[0])
