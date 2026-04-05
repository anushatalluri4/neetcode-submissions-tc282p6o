# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = { val:ind for ind, val in enumerate(inorder)}
        self.pre = 0
        def dfs(l,r):
            if l>r:
                return
            root = preorder[self.pre]
            self.pre += 1
            mid = indices[root]
            root = TreeNode(root)
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        return dfs(0,len(inorder)-1)