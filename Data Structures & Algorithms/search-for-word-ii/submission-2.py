class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False
    def addWord(self,word):
        curr=self
        for w in word:
            if w not in curr.children:
                node=TrieNode()
                curr.children[w]=node
            curr=curr.children[w]
        curr.isEndOfWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)
        rows, cols = len(board), len(board[0])
        res=set()
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        def dfs(r,c,node,word):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] not in node.children or visited[r][c]:
                return
            visited[r][c]=True
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isEndOfWord:
                res.add(word)
            dfs(r+1,c,node,word) 
            dfs(r-1,c,node,word) 
            dfs(r,c+1,node,word) 
            dfs(r,c-1,node,word)
            visited[r][c]=False   
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)
