# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root,float("-inf"),float("inf"))]
        while stack:
            node , leftmin, rightmax = stack.pop()
            if not (leftmin<node.val<rightmax):
                return False
            if node.left:
                stack.append((node.left,leftmin,node.val))
            if node.right:
                stack.append((node.right,node.val,rightmax))
        return True