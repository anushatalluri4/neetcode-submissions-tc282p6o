# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and root:
            return True
        if not root and subRoot:
            return False
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr.val == subRoot.val:
                if self.isSameTree(curr,subRoot):
                    return True
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        q = deque([(p,q)])
        while q:
            p1,q1 = q.popleft()
            if not p1 and not q1:
                continue
            if not p1 or not q1 or p1.val!=q1.val:
                return False
            q.append((p1.left,q1.left))
            q.append((p1.right,q1.right))
        return True