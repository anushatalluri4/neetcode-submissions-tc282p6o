# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node,maxseen):
            if not node:
                return 0
            if node.val>=maxseen:
                self.count+=1
            dfs(node.left,max(node.val,maxseen))
            dfs(node.right,max(node.val,maxseen)) 
        dfs(root,float("-inf"))
        return self.count
        