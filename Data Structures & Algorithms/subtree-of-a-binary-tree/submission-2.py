# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.isSubTree(node,subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
    def isSubTree(self,p,q):
        stack = [(p,q)]
        while stack:
            p1,q1 = stack.pop()
            if not p1 and not q1:
                continue
            if not p1 or not q1 or p1.val != q1.val:
                return False
            stack.append((p1.left,q1.left))
            stack.append((p1.right,q1.right))
        return True