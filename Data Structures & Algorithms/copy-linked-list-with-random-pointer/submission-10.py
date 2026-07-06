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
        curr=head
        while curr:
            copy = Node(curr.val)
            copy.next=curr.random
            curr.random=copy
            curr=curr.next
        curr = head
        copyhead = head.random
        while curr:
            curr.random.random = curr.random.next.random if curr.random.next else None
            curr=curr.next
        curr=head
        while curr:
            temp = curr.random.next
            curr.random.next = curr.next.random if curr.next else None
            curr.random = temp
            curr=curr.next
        return copyhead
