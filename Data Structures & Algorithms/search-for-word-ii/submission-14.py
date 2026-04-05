class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.ind = -1
        self.refs = 0
    def addWord(self,word,i):
        curr = self
        curr.refs += 1
        for c in word:
            index = ord(c)-ord("a")
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.refs += 1
        curr.ind = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i],i)
        rows, cols = len(board), len(board[0])
        res = []
        def getIndex(w):
            return (ord(w)-ord("a"))
        def dfs(r,c,node):
            if r not in range(rows) or c not in range(cols) or board[r][c] == "#" or not node.children[getIndex(board[r][c])] :
                return 
            tmp = board[r][c]
            board[r][c] = "#"
            prev = node
            node = node.children[getIndex(tmp)]
            if node.ind != -1:
                res.append(words[node.ind])
                node.ind = -1
                node.refs -= 1
                if node.refs == 0:
                    prev.children[getIndex(tmp)] = None
                    node = None
                    board[r][c] = tmp
                    return
            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)
            board[r][c] = tmp
        for row in range(rows):
            for col in range(cols):
                dfs(row,col,root)
        return res