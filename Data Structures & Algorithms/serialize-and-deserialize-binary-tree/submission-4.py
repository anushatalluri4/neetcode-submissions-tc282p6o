# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        stack = deque([root])
        if not root:
            return "N"
        while stack:
            node = stack.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        if values[0] == "N":
            return
        root = TreeNode(int(values[0]))
        q = deque([root])
        ind = 1
        while q :
            node = q.popleft()
            if values[ind]!="N":
                node.left = TreeNode(int(values[ind]))
                q.append(node.left)
            ind += 1
            if values[ind]!="N":
                node.right = TreeNode(int(values[ind]))
                q.append(node.right)
            ind+=1
        return root
        