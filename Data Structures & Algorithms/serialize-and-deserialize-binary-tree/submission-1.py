# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        s = []
        while q:
            node = q.popleft()
            if not node:
                s.append("N")
            else:
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(s)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        q = deque([root])
        ind = 1
        while q:
            node = q.popleft()
            if vals[ind] != "N":
                node.left = TreeNode(int(vals[ind]))
                q.append(node.left)
            ind += 1
            if vals[ind] != "N":
                node.right = TreeNode(int(vals[ind]))
                q.append(node.right)
            ind += 1
        return root
