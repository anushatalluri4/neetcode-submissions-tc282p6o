# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        if not p and not q:
            return True
        while stack:
            p1, p2 = stack.pop()
            if not p1 or not p2 or p1.val != p2.val:
                return False
            if p1.left or p2.left:
                stack.append((p1.left,p2.left))
            if p1.right or p2.right:
                stack.append((p1.right,p2.right))
        return True
