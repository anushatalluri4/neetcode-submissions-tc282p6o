# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        q = deque([root])
        while q:
            curr = q.popleft()
            if not curr:
                res.append("N")
            else:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
        return ",".join(res)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return
        values = data.split(",")
        root = TreeNode(values[0])
        q=deque([root])
        i = 1
        while q:
            curr = q.popleft()
            if values[i] != "N":
                curr.left = TreeNode(values[i])
                q.append(curr.left)
            i+=1
            if values[i]!="N":
                curr.right = TreeNode(values[i])
                q.append(curr.right)
            i+=1
        return root

