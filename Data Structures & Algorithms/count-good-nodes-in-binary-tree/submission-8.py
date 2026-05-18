# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def dfs(root,maxwei):
            if not root:
                return 0
            if root.val>=maxwei:
                maxwei = root.val
                self.good+=1
            dfs(root.left,maxwei)
            dfs(root.right,maxwei)
        dfs(root,float("-inf"))
        return self.good