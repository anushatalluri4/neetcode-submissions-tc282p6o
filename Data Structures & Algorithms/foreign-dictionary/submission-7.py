from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Create graph with all unique characters
        adj = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in adj}

        # Build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Invalid prefix case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Find first different character
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # Avoid duplicate edges
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        # Initialize queue with indegree 0 nodes
        q = deque()

        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        res = []

        while q:
            c = q.popleft()
            res.append(c)

            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # Cycle exists
        if len(res) != len(adj):
            return ""

        return "".join(res)