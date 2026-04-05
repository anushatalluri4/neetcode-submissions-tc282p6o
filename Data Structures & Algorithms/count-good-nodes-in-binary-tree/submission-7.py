# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.good = 0
        def dfs(root,maxe):
            if not root:
                return 0
            if root.val >= maxe:
                maxe = root.val
                self.good += 1
            dfs(root.left,maxe)
            dfs(root.right,maxe)
        dfs(root,float("-inf"))
        return self.good

        