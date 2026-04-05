"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        old = head
        while old:
            copy = Node(old.val)
            copy.next = old.random
            old.random = copy
            old = old.next
        curr = head
        dummy = head.random
        while curr:
            copy = curr.random
            copy.random = copy.next.random if copy.next else None
            curr = curr.next
        curr = head
        while curr:
            node = curr.random.next
            curr.random.next = curr.next.random if curr.next else None
            curr.random = node
            curr = curr.next
        return dummy
        