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
        curr = head
        if not head:
            return None
        while curr:
            node = Node(curr.val)
            node.next = curr.random
            curr.random = node
            curr = curr.next
        dummy = head.random
        curr = head
        while curr:
            node = curr.random
            node.random = node.next.random if node.next else None
            curr = curr.next
        curr = head
        while curr:
            node = curr.random.next

            curr.random.next = curr.next.random if curr.next else None
            curr.random = node
            curr = curr.next
        return dummy
