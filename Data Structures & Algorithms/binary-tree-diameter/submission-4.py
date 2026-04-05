# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None:(0,0)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftdia, lefthei = mp[node.left]
                rightdia, righthei = mp[node.right]
                mp[node] = (max(lefthei+righthei,leftdia,rightdia),1+max(lefthei,righthei))
            
        return mp[root][0]

