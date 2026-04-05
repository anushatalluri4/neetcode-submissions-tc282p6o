# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        mp = {None:0}
        if not root:
            return True
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                lefthei = mp[node.left]
                righthei = mp[node.right]
                if abs(lefthei - righthei) > 1:
                    return False
                mp[node] = 1+max(lefthei,righthei)
        return True