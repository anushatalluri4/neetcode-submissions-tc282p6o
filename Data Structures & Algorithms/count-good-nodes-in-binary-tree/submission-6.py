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
        def dfs(root, maxseen_sofar):
            if not root:
                return 0
            if root.val >= maxseen_sofar:
                self.good += 1
            newmax = max(maxseen_sofar, root.val)
            dfs(root.left, newmax)
            dfs(root.right,newmax)
        dfs(root,float("-inf"))
        return self.good
        