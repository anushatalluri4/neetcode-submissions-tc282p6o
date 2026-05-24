class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(root,i):
            curr = root
            for j in range(i,len(word)):
                if word[j] == ".":
                    for child in curr.children.values():
                        if dfs(child,j+1):
                            return True
                    return False
                else:
                    if word[j] not in curr.children:
                        return False
                    else:
                        curr = curr.children[word[j]]
            return curr.isEnd
        return dfs(self.root,0)


