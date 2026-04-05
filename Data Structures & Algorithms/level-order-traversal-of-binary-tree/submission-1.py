# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = collections.deque()
        d.append(root)
        res=[]
        while d:
            currlevel=[]
            for i in range(len(d)):
                curr = d.popleft()
                if curr:
                    currlevel.append(curr.val)
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            res.append(currlevel)
        return res
            