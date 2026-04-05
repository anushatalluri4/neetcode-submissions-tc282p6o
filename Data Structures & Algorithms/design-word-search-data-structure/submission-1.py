class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for w in word:
            if w not in curr.children:
                node=TrieNode()
                curr.children[w]=node
            curr=curr.children[w]
        curr.isEndOfWord=True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            curr=root
            for i in range(j,len(word)):
                c=word[i]
                if c=='.':
                    for w in curr.children.values():
                        if dfs(i+1,w):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr=curr.children[c]
            return curr.isEndOfWord
        return dfs(0,self.root)
